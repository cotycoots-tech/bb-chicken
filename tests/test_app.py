from bb_chicken.app import SITE_DOMAIN, SITE_NAME, app, welcome_message


def test_welcome_message() -> None:
    assert welcome_message() == f"Welcome to {SITE_NAME}!"


def test_index_route_shows_metadata() -> None:
    client = app.test_client()

    response = client.get("/")
    assert response.status_code == 200
    assert SITE_NAME.encode() in response.data
    assert b"Next" in response.data

    response = client.get("/?index=1")
    assert response.status_code == 200
    assert SITE_DOMAIN.encode() in response.data or b"Domain" in response.data


def test_index_route_shows_image_and_video() -> None:
    client = app.test_client()

    # First gallery image (after Title, Domain, Version, Author, Story).
    response = client.get("/?index=5")
    assert response.status_code == 200
    assert b"<img" in response.data
    assert b"github.com/user-attachments/assets" in response.data
    assert b"Belly Busting Chicken" in response.data
    # URL must not appear as visible page text (only as media src).
    assert b'<h1 class="value">https://' not in response.data

    # First gallery video.
    response = client.get("/?index=6")
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
    assert SITE_DOMAIN.encode() in response.data
    assert b'property="og:url"' in response.data
