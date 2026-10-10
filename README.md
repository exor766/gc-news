# 🌐 Golden Commander — High-Impact News Feed

Автоматический шлюз экономического календаря (USD / EUR) для советников **Golden Commander** (MT4 / MT5).
Обновляется каждые 30 минут через GitHub Actions.

- **JSON Feed:** `https://raw.githubusercontent.com/exor766/gc-news/main/news.json`
- **CSV Feed (Рекомендуется для MT4):** `https://raw.githubusercontent.com/exor766/gc-news/main/news.csv`
- **Последнее обновление:** `2026.10.10 01:05:50 UTC`
- **Активных событий в базе:** `28`

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
| `2026.09.28 13:30` | **EUR** | 🟠 Medium | ECB President Lagarde Speaks |
| `2026.09.29 11:00` | **EUR** | 🟠 Medium | ECB President Lagarde Speaks |
| `2026.09.29 14:00` | **USD** | 🟠 Medium | CB Consumer Confidence |
| `2026.09.29 14:00` | **USD** | 🟠 Medium | JOLTS Job Openings |
| `2026.09.30 06:29` | **EUR** | 🟠 Medium | German Prelim CPI m/m |
| `2026.09.30 12:15` | **USD** | 🟠 Medium | ADP Non-Farm Employment Change |
| `2026.09.30 12:30` | **USD** | 🔴 High | Core PCE Price Index m/m |
| `2026.09.30 12:30` | **USD** | 🔴 High | Final GDP q/q |
| `2026.09.30 12:30` | **USD** | 🟠 Medium | Final GDP Price Index q/q |
| `2026.09.30 19:30` | **USD** | 🟠 Medium | President Trump Speaks |
| `2026.09.30 22:00` | **USD** | 🟠 Medium | FOMC Member Kashkari Speaks |
| `2026.10.01 12:30` | **USD** | 🟠 Medium | Unemployment Claims |
| `2026.10.01 13:30` | **EUR** | 🟠 Medium | ECB President Lagarde Speaks |
| `2026.10.01 14:00` | **USD** | 🟠 Medium | FOMC Member Waller Speaks |
| `2026.10.01 14:00` | **USD** | 🟠 Medium | ISM Manufacturing PMI |
| `2026.10.02 09:00` | **EUR** | 🟠 Medium | Core CPI Flash Estimate y/y |
| `2026.10.02 09:00` | **EUR** | 🟠 Medium | CPI Flash Estimate y/y |
| `2026.10.02 12:30` | **USD** | 🔴 High | Average Hourly Earnings m/m |
| `2026.10.02 12:30` | **USD** | 🔴 High | Non-Farm Employment Change |
| `2026.10.02 12:30` | **USD** | 🔴 High | Unemployment Rate |
| `2026.10.04 09:15` | **ALL** | 🟠 Medium | OPEC-JMMC Meetings |
| `2026.10.05 14:00` | **USD** | 🟠 Medium | ISM Services PMI |
| `2026.10.07 17:00` | **USD** | 🟠 Medium | President Trump Speaks |
| `2026.10.07 18:00` | **USD** | 🔴 High | FOMC Meeting Minutes |
| `2026.10.08 08:30` | **USD** | 🟠 Medium | FOMC Member Waller Speaks |
| `2026.10.08 12:30` | **USD** | 🟠 Medium | Unemployment Claims |
| `2026.10.09 14:00` | **USD** | 🟠 Medium | Prelim UoM Consumer Sentiment |
| `2026.10.09 14:00` | **USD** | 🟠 Medium | Prelim UoM Inflation Expectations |
