# 🌐 Golden Commander — High-Impact News Feed

Автоматический шлюз экономического календаря (USD / EUR) для советников **Golden Commander** (MT4 / MT5).
Обновляется каждые 30 минут через GitHub Actions.

- **JSON Feed:** `https://raw.githubusercontent.com/exor766/gc-news/main/news.json`
- **CSV Feed (Рекомендуется для MT4):** `https://raw.githubusercontent.com/exor766/gc-news/main/news.csv`
- **Последнее обновление:** `2026.11.11 21:45:09 UTC`
- **Активных событий в базе:** `32`

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
| `2026.10.29 12:30` | **USD** | 🔴 High | Advance GDP q/q |
| `2026.10.29 12:30` | **USD** | 🔴 High | Core PCE Price Index m/m |
| `2026.10.29 12:30` | **USD** | 🟠 Medium | Advance GDP Price Index q/q |
| `2026.10.29 12:30` | **USD** | 🟠 Medium | Unemployment Claims |
| `2026.10.29 13:15` | **EUR** | 🔴 High | Main Refinancing Rate |
| `2026.10.29 13:15` | **EUR** | 🔴 High | Monetary Policy Statement |
| `2026.10.29 13:45` | **EUR** | 🔴 High | ECB Press Conference |
| `2026.10.30 06:29` | **EUR** | 🟠 Medium | German Prelim CPI m/m |
| `2026.10.30 07:29` | **EUR** | 🟠 Medium | German Prelim CPI m/m |
| `2026.10.30 09:00` | **EUR** | 🟠 Medium | German Prelim GDP q/q |
| `2026.10.30 12:30` | **USD** | 🟠 Medium | Employment Cost Index q/q |
| `2026.11.02 15:00` | **USD** | 🟠 Medium | ISM Manufacturing PMI |
| `2026.11.03 15:00` | **USD** | 🟠 Medium | JOLTS Job Openings |
| `2026.11.03 15:16` | **USD** | 🔴 High | Congressional Elections |
| `2026.11.04 10:00` | **EUR** | 🟠 Medium | Core CPI Flash Estimate y/y |
| `2026.11.04 10:00` | **EUR** | 🟠 Medium | CPI Flash Estimate y/y |
| `2026.11.04 15:00` | **USD** | 🟠 Medium | ISM Services PMI |
| `2026.11.05 13:30` | **USD** | 🟠 Medium | Unemployment Claims |
| `2026.11.05 18:00` | **EUR** | 🟠 Medium | ECB President Lagarde Speaks |
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
