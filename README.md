# 🌐 Golden Commander — High-Impact News Feed

Автоматический шлюз экономического календаря (USD / EUR) для советников **Golden Commander** (MT4 / MT5).
Обновляется каждые 30 минут через GitHub Actions.

- **JSON Feed:** `https://raw.githubusercontent.com/exor766/gc-news/main/news.json`
- **CSV Feed (Рекомендуется для MT4):** `https://raw.githubusercontent.com/exor766/gc-news/main/news.csv`
- **Последнее обновление:** `2026.09.04 20:55:26 UTC`
- **Активных событий в базе:** `12`

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
| `2026.08.31 06:29` | **EUR** | 🟠 Medium | German Prelim CPI m/m |
| `2026.09.01 09:00` | **EUR** | 🟠 Medium | Core CPI Flash Estimate y/y |
| `2026.09.01 09:00` | **EUR** | 🟠 Medium | CPI Flash Estimate y/y |
| `2026.09.01 14:00` | **USD** | 🔴 High | ISM Manufacturing PMI |
| `2026.09.01 14:00` | **USD** | 🟠 Medium | ISM Manufacturing Prices |
| `2026.09.01 14:00` | **USD** | 🟠 Medium | JOLTS Job Openings |
| `2026.09.02 12:15` | **USD** | 🟠 Medium | ADP Non-Farm Employment Change |
| `2026.09.03 12:30` | **USD** | 🟠 Medium | Unemployment Claims |
| `2026.09.03 14:00` | **USD** | 🟠 Medium | ISM Services PMI |
| `2026.09.04 12:30` | **USD** | 🔴 High | Average Hourly Earnings m/m |
| `2026.09.04 12:30` | **USD** | 🔴 High | Non-Farm Employment Change |
| `2026.09.04 12:30` | **USD** | 🔴 High | Unemployment Rate |
