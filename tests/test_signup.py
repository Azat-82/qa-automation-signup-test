import pytest


class TestAuthSignup:
    """Класс для тестов операции регистрации нового пользователя."""

    def test_successful_signup(
        self, api_session, base_url, random_user_payload
    ):
        """Успешное создание аккаунта с валидными данными."""
        # Arrange (Подготовка)
        endpoint = f"{base_url}/api/Auth/signup"
        payload = random_user_payload

        # Act (Действие)
        response = api_session.post(endpoint, json=payload)

        # Assert (Проверка)
        assert response.status_code == 200, (
            f"Неожиданный статус код: {response.status_code}. "
            f"Ответ сервера: {response.text}"
        )

        response_text = response.text
        assert response_text, "Сервер вернул пустой ответ"

    @pytest.mark.parametrize(
        "payload_modifier, expected_status, error_keyword",
        [
            ({"email": "not_an_email_at_all.com"}, 409, "error"),
            ({"email": 12345}, 409, "error"),
            (None, 409, "error"),
        ],
        ids=["invalid_email", "numeric_email", "empty_body"],
    )
    def test_signup_validation_errors(
        self,
        api_session,
        base_url,
        random_user_payload,
        payload_modifier,
        expected_status,
        error_keyword,
    ):
        endpoint = f"{base_url}/api/Auth/signup"

        if payload_modifier is None:
            payload = {}
        else:
            payload = random_user_payload.copy()
            payload.update(payload_modifier)

        # Act
        response = api_session.post(endpoint, json=payload)

        assert response.status_code == expected_status, (
            f"Ожидался статус ошибки {expected_status}, но получен "
            f"{response.status_code}. Ответ: {response.text}"
        )

        if error_keyword:
            error_text = response.text.lower()
            assert error_keyword in error_text, (
                f"В тексте ответа сервера нет упоминания "
                f"ключевого слова: '{error_keyword}'. Ответ: {response.text}"
            )

    def test_signup_duplicate_email_error(
        self, api_session, base_url, random_user_payload
    ):
        endpoint = f"{base_url}/api/Auth/signup"
        payload = random_user_payload

        first_resp = api_session.post(endpoint, json=payload)
        assert first_resp.status_code == 200, (
            f"Не удалось создать базового пользователя для теста. "
            f"Код: {first_resp.status_code}, Ответ: {first_resp.text}"
        )

        second_resp = api_session.post(endpoint, json=payload)

        assert second_resp.status_code in (400, 409, 429), (
            f"Ожидался статус 400, 409 или 429 для дубликата, "
            f"получен {second_resp.status_code}. Ответ: {second_resp.text}"
        )

        error_text = second_resp.text.lower()

        has_dup_words = any(
            word in error_text for word in [
                "exist", "already", "duplicate", "error", "sent", "token"
            ]
        )
        assert has_dup_words, (
            f"Текст ошибки не указывает на проблему: {second_resp.text}"
        )
