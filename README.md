# 🌐 Golden Commander — High-Impact News Feed

Автоматический шлюз экономического календаря (USD / EUR) для советников **Golden Commander** (MT4 / MT5).
Обновляется каждые 30 минут через GitHub Actions.

- **JSON Feed:** `https://raw.githubusercontent.com/exor766/gc-news/main/news.json`
- **CSV Feed (Рекомендуется для MT4):** `https://raw.githubusercontent.com/exor766/gc-news/main/news.csv`
- **Последнее обновление:** `2026.09.24 21:58:23 UTC`
- **Активных событий в базе:** `29`

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
| `2026.09.11 12:30` | **USD** | 🔴 High | Core CPI m/m |
| `2026.09.11 12:30` | **USD** | 🔴 High | Core CPI y/y |
| `2026.09.11 12:30` | **USD** | 🔴 High | CPI m/m |
| `2026.09.11 12:30` | **USD** | 🔴 High | CPI y/y |
| `2026.09.11 14:00` | **EUR** | 🟠 Medium | ECB President Lagarde Speaks |
| `2026.09.11 14:00` | **USD** | 🟠 Medium | Prelim UoM Consumer Sentiment |
| `2026.09.11 14:00` | **USD** | 🟠 Medium | Prelim UoM Inflation Expectations |
| `2026.09.14 15:15` | **EUR** | 🟠 Medium | ECB President Lagarde Speaks |
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
| `2026.09.25 14:00` | **USD** | 🟠 Medium | Revised UoM Consumer Sentiment |
| `2026.09.25 14:00` | **USD** | 🟠 Medium | Revised UoM Inflation Expectations |
