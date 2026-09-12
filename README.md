# 🌐 Golden Commander — High-Impact News Feed

Автоматический шлюз экономического календаря (USD / EUR) для советников **Golden Commander** (MT4 / MT5).
Обновляется каждые 30 минут через GitHub Actions.

- **JSON Feed:** `https://raw.githubusercontent.com/exor766/gc-news/main/news.json`
- **CSV Feed (Рекомендуется для MT4):** `https://raw.githubusercontent.com/exor766/gc-news/main/news.csv`
- **Последнее обновление:** `2026.09.12 08:03:33 UTC`
- **Активных событий в базе:** `15`

---

## ⚙️ Инструкция для MetaTrader 4:
1. В терминале MT4 откройте меню: **Сервис** → **Настройки** → **Советники** (`Ctrl+O`).
2. Поставьте галочку **«Разрешить WebRequest для следующих URL»**.
3. Добавьте URL в список:
   ```text
   https://raw.githubusercontent.com
   ```
4. В настройках советника `Golden_Commander` параметр **`NewsURL`** оставьте по умолчанию:
   `https://raw.githubusercontent.com/exor766/gc-news/main/news.csv`

---

## 📅 Текущее расписание High / Medium Impact новостей:

| Время (UTC) | Валюта | Важность | Событие |
|---|---|---|---|
| `2026.09.10 01:15` | **USD** | 🟠 Medium | President Trump Speaks |
| `2026.09.10 12:15` | **EUR** | 🔴 High | Main Refinancing Rate |
| `2026.09.10 12:15` | **EUR** | 🔴 High | Monetary Policy Statement |
| `2026.09.10 12:30` | **USD** | 🔴 High | Core PPI m/m |
| `2026.09.10 12:30` | **USD** | 🔴 High | PPI m/m |
| `2026.09.10 12:30` | **USD** | 🟠 Medium | Unemployment Claims |
| `2026.09.10 12:45` | **EUR** | 🔴 High | ECB Press Conference |
| `2026.09.11 12:30` | **USD** | 🔴 High | Core CPI m/m |
| `2026.09.11 12:30` | **USD** | 🔴 High | Core CPI y/y |
| `2026.09.11 12:30` | **USD** | 🔴 High | CPI m/m |
| `2026.09.11 12:30` | **USD** | 🔴 High | CPI y/y |
| `2026.09.11 14:00` | **EUR** | 🟠 Medium | ECB President Lagarde Speaks |
| `2026.09.11 14:00` | **USD** | 🟠 Medium | Prelim UoM Consumer Sentiment |
| `2026.09.11 14:00` | **USD** | 🟠 Medium | Prelim UoM Inflation Expectations |
| `2026.09.12 08:00` | **EUR** | 🟠 Medium | ECB President Lagarde Speaks |
