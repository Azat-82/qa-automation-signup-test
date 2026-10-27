import pytest
import requests
from faker import Faker

fake = Faker()


@pytest.fixture(scope="session")
def base_url():
    return "https://automation.tivaliclub.com/fcle"


@pytest.fixture(scope="session")
def api_session():
    session = requests.Session()
    session.headers.update({
        "Content-Type": "application/json",
        "Accept": "*/*"
    })

    yield session

    session.close()


@pytest.fixture
def random_user_payload():
    return {
        "email": fake.email(),
        "lang": "en",
        "utm": (
            "{\n  \"utm_id\": \"12345\",\n  "
            "\"utm_source\": \"google\",\n  "
            "\"utm_medium\": \"cpc\",\n  "
            "\"utm_campaign\": \"summer_sale\",\n  "
            "\"utm_content\": \"banner_1\",\n  "
            "\"utm_term\": \"english_course\",\n  "
            "\"referral_code\": \"123456\"\n}"
        )
    }
