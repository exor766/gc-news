# 🌐 Golden Commander — High-Impact News Feed

Автоматический шлюз экономического календаря (USD / EUR) для советников **Golden Commander** (MT4 / MT5).
Обновляется каждые 30 минут через GitHub Actions.

- **JSON Feed:** `https://raw.githubusercontent.com/exor766/gc-news/main/news.json`
- **CSV Feed (Рекомендуется для MT4):** `https://raw.githubusercontent.com/exor766/gc-news/main/news.csv`
- **Последнее обновление:** `2026.10.21 20:17:52 UTC`
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
| `2026.10.08 08:30` | **USD** | 🟠 Medium | FOMC Member Waller Speaks |
| `2026.10.08 12:30` | **USD** | 🟠 Medium | Unemployment Claims |
| `2026.10.09 14:00` | **USD** | 🟠 Medium | Prelim UoM Consumer Sentiment |
| `2026.10.09 14:00` | **USD** | 🟠 Medium | Prelim UoM Inflation Expectations |
| `2026.10.14 02:10` | **EUR** | 🟠 Medium | ECB President Lagarde Speaks |
| `2026.10.14 08:30` | **EUR** | 🟠 Medium | ECB President Lagarde Speaks |
| `2026.10.14 10:15` | **EUR** | 🟠 Medium | EU Economic Summit |
| `2026.10.14 12:30` | **USD** | 🔴 High | Core CPI m/m |
| `2026.10.14 12:30` | **USD** | 🔴 High | Core CPI y/y |
| `2026.10.14 12:30` | **USD** | 🔴 High | CPI m/m |
| `2026.10.14 12:30` | **USD** | 🔴 High | CPI y/y |
| `2026.10.15 10:15` | **EUR** | 🟠 Medium | EU Economic Summit |
| `2026.10.15 12:30` | **USD** | 🔴 High | Core PPI m/m |
| `2026.10.15 12:30` | **USD** | 🔴 High | Core Retail Sales m/m |
| `2026.10.15 12:30` | **USD** | 🔴 High | PPI m/m |
| `2026.10.15 12:30` | **USD** | 🔴 High | Retail Sales m/m |
| `2026.10.15 12:30` | **USD** | 🟠 Medium | Philly Fed Manufacturing Index |
| `2026.10.15 12:30` | **USD** | 🟠 Medium | Unemployment Claims |
| `2026.10.16 03:30` | **USD** | 🔴 High | Fed Chairman Warsh Speaks |
| `2026.10.22 12:30` | **USD** | 🟠 Medium | Unemployment Claims |
| `2026.10.23 07:15` | **EUR** | 🟠 Medium | French Flash Manufacturing PMI |
| `2026.10.23 07:15` | **EUR** | 🟠 Medium | French Flash Services PMI |
| `2026.10.23 07:30` | **EUR** | 🟠 Medium | German Flash Manufacturing PMI |
| `2026.10.23 07:30` | **EUR** | 🟠 Medium | German Flash Services PMI |
| `2026.10.23 13:45` | **USD** | 🟠 Medium | Flash Manufacturing PMI |
| `2026.10.23 13:45` | **USD** | 🟠 Medium | Flash Services PMI |
| `2026.10.23 14:00` | **USD** | 🟠 Medium | Revised UoM Consumer Sentiment |
| `2026.10.23 14:00` | **USD** | 🟠 Medium | Revised UoM Inflation Expectations |
