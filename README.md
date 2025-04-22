# 🔎 Playwright Python Automation Framework – Amazon Example

This is a scalable automation framework built with **Playwright**, **Python**, and **Pytest**.  
It uses **Page Object Model (POM)** design and supports **Allure reports**, **Docker**, and **UI+API test integration**.

---

## 📁 Folder Structure

```
playwright_amazon/
│
├── tests/                  # Test cases
├── pages/                  # Page Objects (POM)
├── utils/                  # Logger & config utils
├── data/                   # Test data
├── conftest.py             # Fixtures
├── requirements.txt
├── pytest.ini
├── Dockerfile
├── docker-compose.yml
├── .github/
│   └── workflows/
│       └── playwright.yml
└── README.md
```

---

## ✅ Features

- 🚀 Scalable POM-based structure
- 🧪 Pytest test runner with parametrization
- 🌐 Playwright browser automation
- 🔗 UI + API combined test example
- 📊 Allure reporting support
- 🐳 Docker support for test execution

---

## 🧰 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/<your-username>/playwright-amazon.git
cd playwright-amazon
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
playwright install
```

### 3. Run Tests

```bash
pytest tests/
```

### 4. View Allure Reports

```bash
pytest --alluredir=allure-results
allure serve allure-results
```

### 5. Run via Docker

```bash
docker-compose up --build
```

---

## 🧪 Sample Test Command

```bash
pytest tests/test_amazon_search.py -v
```

---

## 👨‍💻 Author

Viplove Bisen | [YouTube](https://www.youtube.com/@viplovebisen) | [LinkedIn](https://linkedin.com/in/viplovebisen)
