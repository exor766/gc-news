# 🌐 Golden Commander — High-Impact News Feed

Автоматический шлюз экономического календаря (USD / EUR) для советников **Golden Commander** (MT4 / MT5).
Обновляется каждые 30 минут через GitHub Actions.

- **JSON Feed:** `https://raw.githubusercontent.com/exor766/gc-news/main/news.json`
- **CSV Feed (Рекомендуется для MT4):** `https://raw.githubusercontent.com/exor766/gc-news/main/news.csv`
- **Последнее обновление:** `2026.11.20 12:30:21 UTC`
- **Активных событий в базе:** `26`

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
| `2026.11.06 13:30` | **USD** | 🔴 High | Average Hourly Earnings m/m |
| `2026.11.06 13:30` | **USD** | 🔴 High | Non-Farm Employment Change |
| `2026.11.06 13:30` | **USD** | 🔴 High | Unemployment Rate |
| `2026.11.06 15:00` | **USD** | 🟠 Medium | Prelim UoM Consumer Sentiment |
| `2026.11.06 15:00` | **USD** | 🟠 Medium | Prelim UoM Inflation Expectations |
| `2026.11.10 09:00` | **USD** | 🟠 Medium | FOMC Member Waller Speaks |
| `2026.11.10 13:30` | **USD** | 🔴 High | Core CPI m/m |
| `2026.11.10 13:30` | **USD** | 🔴 High | CPI m/m |
| `2026.11.11 09:45` | **EUR** | 🟠 Medium | ECB President Lagarde Speaks |
| `2026.11.12 13:30` | **USD** | 🟠 Medium | Unemployment Claims |
| `2026.11.12 19:30` | **EUR** | 🟠 Medium | ECB President Lagarde Speaks |
| `2026.11.13 13:30` | **USD** | 🔴 High | Core PPI m/m |
| `2026.11.13 13:30` | **USD** | 🔴 High | PPI m/m |
| `2026.11.16 17:00` | **USD** | 🔴 High | Fed Chairman Warsh Speaks |
| `2026.11.17 13:30` | **USD** | 🔴 High | Core Retail Sales m/m |
| `2026.11.17 13:30` | **USD** | 🔴 High | Retail Sales m/m |
| `2026.11.18 09:00` | **EUR** | 🟠 Medium | ECB Financial Stability Review |
| `2026.11.18 14:25` | **EUR** | 🟠 Medium | ECB President Lagarde Speaks |
| `2026.11.18 19:00` | **USD** | 🔴 High | FOMC Meeting Minutes |
| `2026.11.19 13:30` | **EUR** | 🟠 Medium | ECB President Lagarde Speaks |
| `2026.11.19 13:30` | **USD** | 🟠 Medium | Philly Fed Manufacturing Index |
| `2026.11.19 13:30` | **USD** | 🟠 Medium | Unemployment Claims |
| `2026.11.20 08:15` | **EUR** | 🟠 Medium | ECB President Lagarde Speaks |
| `2026.11.20 13:25` | **USD** | 🟠 Medium | FOMC Member Waller Speaks |
| `2026.11.20 15:00` | **USD** | 🟠 Medium | Revised UoM Consumer Sentiment |
| `2026.11.20 15:00` | **USD** | 🟠 Medium | Revised UoM Inflation Expectations |
