from bb_chicken.app import SITE_DOMAIN, SITE_NAME, app, welcome_message


def test_welcome_message() -> None:
    assert welcome_message() == f"Welcome to {SITE_NAME}!"


def test_index_route_shows_metadata() -> None:
    client = app.test_client()

    response = client.get("/")
    assert response.status_code == 200
    assert SITE_NAME.encode() in response.data
    assert b"Next" in response.data

    # Story is combined with Boxing Chicken image.
    response = client.get("/?index=1")
    assert response.status_code == 200
    assert b"Story" in response.data
    assert b"big belly chicken vs big black cat" in response.data
    assert b"<img" in response.data
    assert b"73c75b27-cd64-461b-9ee7-1cf879c0ef82" in response.data


def test_index_route_shows_image_and_video() -> None:
    client = app.test_client()

    # First pure gallery image (after Title, Story+image).
    response = client.get("/?index=2")
    assert response.status_code == 200
    assert b"<img" in response.data
    assert b"github.com/user-attachments/assets" in response.data
    assert b"Belly Busting Chicken" in response.data
    # URL must not appear as visible page text (only as media src).
    assert b'<h1 class="value">https://' not in response.data

    # First gallery video.
    response = client.get("/?index=3")
    assert response.status_code == 200
    assert b"<video" in response.data
    assert b"github.com/user-attachments/assets" in response.data
    assert b"video" in response.data.lower()
    assert b'<h1 class="value">https://' not in response.data


def test_healthz() -> None:
    client = app.test_client()
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.data == b"ok"


def test_branding_meta() -> None:
    client = app.test_client()
    response = client.get("/")
    assert SITE_NAME.encode() in response.data
    assert b"Step 1 of" in response.data
    # Domain string must not appear in the step chrome / body copy.
    assert b"cotycoots-tech.github.io/bb-chicken" not in response.data
    assert b'property="og:url"' in response.data


def test_final_slide_is_bucket_chicken_image() -> None:
    client = app.test_client()

    # 10 steps after combining Boxing image into Story; final is index 9.
    response = client.get("/?index=9")
    assert response.status_code == 200
    assert b"<img" in response.data
    assert b"Big Bucket Chicken" in response.data
    assert b"Start over" in response.data
    assert b"Step 10 of 10" in response.data
    assert b'<h1 class="value">https://' not in response.data

    # Past the end clamps onto the same final image slide.
    response = client.get("/?index=99")
    assert response.status_code == 200
    assert b"<img" in response.data
    assert b"Start over" in response.data
    assert b"Complete" not in response.data
