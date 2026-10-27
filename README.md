# Автоматизация тестирования API: Эндпоинт Регистрации

## Описание проекта
Данный проект содержит набор автоматизированных тестов на Python для проверки операции
регистрации пользователя (`POST /api/Auth/signup`).

### Особенности архитектуры:
* **Паттерн AAA (Arrange, Act, Assert):** Обеспечивает структуру тестов.
* **requests.Session:** Переиспользует TCP-соединение для всех тестов.
* **Идемпотентность:** `faker` генерирует случайные валидные данные.

---

## Структура проекта
```text
project/
│
├── tests/
│   ├── __init__.py
│   ├── test_signup.py    # Тесты для эндпоинта /api/Auth/signup
│   └── conftest.py       # Фикстуры и настройки для тестов
├── requirements.txt      # Зависимости проекта
├── README.md             # Инструкции по проекту
└── .gitignore            # Игнорируемые файлы
```

---

## Назначение файлов
* `tests/conftest.py` — конфигурация `pytest`. Хранит базовый URL API,
  сессию `requests.Session` и генератор динамических данных.
* `tests/test_signup.py` — класс `TestAuthSignup`, объединяющий позитивный
  сценарий, параметризованную валидацию и тест на дубликаты (5 тестов).
* `requirements.txt` — используемые пакеты с жестким указанием версий.

---

## Инструкция по установке

1. Клонируйте репозиторий с проектом и перейдите в его директорию.
2. Создайте и активируйте виртуальное окружение:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Для Linux/macOS
   venv\Scripts\activate     # Для Windows
   ```
3. Установите все зависимости одной командой:
   ```bash
   pip install -r requirements.txt
   ```

---

## Инструкция по запуску тестов

Для запуска тестов в подробном (verbose) режиме выполните:
```bash
pytest tests/ -v
```

---

## Пример ожидаемого вывода тестов

При успешном прохождении сценариев вы увидите следующий вывод:

```text
============================== test session starts ==============================
collected 5 items                                                                               

tests/test_signup.py::TestAuthSignup::test_successful_signup PASSED        [ 20%]
tests/test_signup.py::TestAuthSignup::test_signup_val_errors[weak_pass] PASSED [ 40%]
tests/test_signup.py::TestAuthSignup::test_signup_val_errors[inv_email] PASSED [ 60%]
tests/test_signup.py::TestAuthSignup::test_signup_val_errors[empty] PASSED [ 80%]
tests/test_signup.py::TestAuthSignup::test_signup_duplicate_error PASSED  [100%]

=============================== 5 passed in 0.84s ===============================
```
