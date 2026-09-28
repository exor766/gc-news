# 🌐 Golden Commander — High-Impact News Feed

Автоматический шлюз экономического календаря (USD / EUR) для советников **Golden Commander** (MT4 / MT5).
Обновляется каждые 30 минут через GitHub Actions.

- **JSON Feed:** `https://raw.githubusercontent.com/exor766/gc-news/main/news.json`
- **CSV Feed (Рекомендуется для MT4):** `https://raw.githubusercontent.com/exor766/gc-news/main/news.csv`
- **Последнее обновление:** `2026.09.28 22:24:22 UTC`
- **Активных событий в базе:** `40`

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
| `2026.09.15 14:00` | **USD** | 🟠 Medium | Treasury Sec Bessent Speaks |
| `2026.09.16 12:30` | **USD** | 🟠 Medium | Core Retail Sales m/m |
| `2026.09.16 12:30` | **USD** | 🟠 Medium | Retail Sales m/m |
| `2026.09.16 18:00` | **USD** | 🔴 High | Federal Funds Rate |
| `2026.09.16 18:00` | **USD** | 🔴 High | FOMC Economic Projections |
| `2026.09.16 18:00` | **USD** | 🔴 High | FOMC Statement |
| `2026.09.16 18:30` | **USD** | 🔴 High | FOMC Press Conference |
| `2026.09.17 12:30` | **USD** | 🟠 Medium | Philly Fed Manufacturing Index |
| `2026.09.17 12:30` | **USD** | 🟠 Medium | Unemployment Claims |
| `2026.09.18 10:30` | **EUR** | 🟠 Medium | ECB President Lagarde Speaks |
| `2026.09.21 15:00` | **EUR** | 🟠 Medium | ECB President Lagarde Speaks |
| `2026.09.22 11:00` | **EUR** | 🟠 Medium | ECB President Lagarde Speaks |
| `2026.09.22 13:55` | **USD** | 🟠 Medium | President Trump Speaks |
| `2026.09.23 07:15` | **EUR** | 🟠 Medium | French Flash Manufacturing PMI |
| `2026.09.23 07:15` | **EUR** | 🟠 Medium | French Flash Services PMI |
| `2026.09.23 07:30` | **EUR** | 🟠 Medium | German Flash Manufacturing PMI |
| `2026.09.23 07:30` | **EUR** | 🟠 Medium | German Flash Services PMI |
| `2026.09.24 12:30` | **USD** | 🟠 Medium | Unemployment Claims |
| `2026.09.24 14:15` | **USD** | 🟠 Medium | President Trump Speaks |
| `2026.09.24 23:55` | **USD** | 🟠 Medium | President Trump Speaks |
| `2026.09.25 14:00` | **USD** | 🟠 Medium | Revised UoM Consumer Sentiment |
| `2026.09.25 14:00` | **USD** | 🟠 Medium | Revised UoM Inflation Expectations |
| `2026.09.28 13:30` | **EUR** | 🟠 Medium | ECB President Lagarde Speaks |
| `2026.09.29 11:00` | **EUR** | 🟠 Medium | ECB President Lagarde Speaks |
| `2026.09.29 14:00` | **USD** | 🟠 Medium | CB Consumer Confidence |
| `2026.09.29 14:00` | **USD** | 🟠 Medium | JOLTS Job Openings |
| `2026.09.30 06:29` | **EUR** | 🟠 Medium | German Prelim CPI m/m |
| `2026.09.30 12:15` | **USD** | 🟠 Medium | ADP Non-Farm Employment Change |
| `2026.09.30 12:30` | **USD** | 🔴 High | Core PCE Price Index m/m |
| `2026.09.30 12:30` | **USD** | 🔴 High | Final GDP q/q |
| `2026.09.30 12:30` | **USD** | 🟠 Medium | Final GDP Price Index q/q |
| `2026.10.01 12:30` | **USD** | 🟠 Medium | Unemployment Claims |
| `2026.10.01 13:30` | **EUR** | 🟠 Medium | ECB President Lagarde Speaks |
| `2026.10.01 14:00` | **USD** | 🟠 Medium | FOMC Member Waller Speaks |
| `2026.10.01 14:00` | **USD** | 🟠 Medium | ISM Manufacturing PMI |
| `2026.10.02 09:00` | **EUR** | 🟠 Medium | Core CPI Flash Estimate y/y |
| `2026.10.02 09:00` | **EUR** | 🟠 Medium | CPI Flash Estimate y/y |
| `2026.10.02 12:30` | **USD** | 🔴 High | Average Hourly Earnings m/m |
| `2026.10.02 12:30` | **USD** | 🔴 High | Non-Farm Employment Change |
| `2026.10.02 12:30` | **USD** | 🔴 High | Unemployment Rate |
