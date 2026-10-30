# 🌐 Golden Commander — High-Impact News Feed

Автоматический шлюз экономического календаря (USD / EUR) для советников **Golden Commander** (MT4 / MT5).
Обновляется каждые 30 минут через GitHub Actions.

- **JSON Feed:** `https://raw.githubusercontent.com/exor766/gc-news/main/news.json`
- **CSV Feed (Рекомендуется для MT4):** `https://raw.githubusercontent.com/exor766/gc-news/main/news.csv`
- **Последнее обновление:** `2026.10.30 19:50:43 UTC`
- **Активных событий в базе:** `24`

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
| `2026.10.22 12:30` | **USD** | 🟠 Medium | Unemployment Claims |
| `2026.10.23 07:15` | **EUR** | 🟠 Medium | French Flash Manufacturing PMI |
| `2026.10.23 07:15` | **EUR** | 🟠 Medium | French Flash Services PMI |
| `2026.10.23 07:30` | **EUR** | 🟠 Medium | German Flash Manufacturing PMI |
| `2026.10.23 07:30` | **EUR** | 🟠 Medium | German Flash Services PMI |
| `2026.10.23 13:45` | **USD** | 🟠 Medium | Flash Manufacturing PMI |
| `2026.10.23 13:45` | **USD** | 🟠 Medium | Flash Services PMI |
| `2026.10.23 14:00` | **USD** | 🟠 Medium | Revised UoM Consumer Sentiment |
| `2026.10.23 14:00` | **USD** | 🟠 Medium | Revised UoM Inflation Expectations |
| `2026.10.27 14:00` | **USD** | 🟠 Medium | CB Consumer Confidence |
| `2026.10.28 18:00` | **USD** | 🔴 High | Federal Funds Rate |
| `2026.10.28 18:00` | **USD** | 🔴 High | FOMC Statement |
| `2026.10.28 18:30` | **USD** | 🔴 High | FOMC Press Conference |
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
