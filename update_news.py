import json
import urllib.request
import datetime
from email.utils import parsedate_to_datetime

URL = "https://nfs.faireconomy.media/ff_calendar_thisweek.json"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "Accept": "application/json"
}

def fetch_calendar():
    req = urllib.request.Request(URL, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=15) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    return data

def main():
    raw_events = fetch_calendar()
    filtered = []
    
    for item in raw_events:
        impact = item.get("impact", "").strip()
        country = item.get("country", "").strip().upper()
        title = item.get("title", "").strip()
        date_str = item.get("date", "").strip()
        
        # Keep High & Medium for USD and EUR
        if impact in ["High", "Medium"] and country in ["USD", "EUR", "ALL"]:
            try:
                # ISO format e.g. 2026-08-30T19:50:00-04:00
                dt = datetime.datetime.fromisoformat(date_str)
                # Convert to UTC
                dt_utc = dt.astimezone(datetime.timezone.utc)
                ts = int(dt_utc.timestamp())
                time_utc_str = dt_utc.strftime("%Y.%m.%d %H:%M")
                
                filtered.append({
                    "timestamp": ts,
                    "time_utc": time_utc_str,
                    "currency": country,
                    "impact": impact,
                    "title": title
                })
            except Exception as e:
                continue

    # Sort by timestamp
    filtered.sort(key=lambda x: x["timestamp"])
    
    now_utc = datetime.datetime.now(datetime.timezone.utc).strftime("%Y.%m.%d %H:%M:%S UTC")
    
    # 1. Output news.json
    result_json = {
        "updated_at": now_utc,
        "count": len(filtered),
        "events": filtered
    }
    with open("news.json", "w", encoding="utf-8") as f:
        json.dump(result_json, f, ensure_ascii=False, indent=2)
        
    # 2. Output news.csv
    with open("news.csv", "w", encoding="utf-8") as f:
        f.write("# timestamp;time_utc;currency;impact;title\n")
        for ev in filtered:
            f.write(f"{ev['timestamp']};{ev['time_utc']};{ev['currency']};{ev['impact']};{ev['title']}\n")
            
    # 3. Output README.md
    readme_content = f"""# 🌐 Golden Commander — High-Impact News Feed

Автоматический шлюз экономического календаря (USD / EUR) для советников **Golden Commander** (MT4 / MT5).
Обновляется каждые 30 минут через GitHub Actions.

- **JSON Feed:** `https://raw.githubusercontent.com/exor766/gc-news/main/news.json`
- **CSV Feed (Рекомендуется для MT4):** `https://raw.githubusercontent.com/exor766/gc-news/main/news.csv`
- **Последнее обновление:** `{now_utc}`
- **Активных событий в базе:** `{len(filtered)}`

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
"""
    for ev in filtered:
        badge = "🔴 High" if ev["impact"] == "High" else "🟠 Medium"
        readme_content += f"| `{ev['time_utc']}` | **{ev['currency']}** | {badge} | {ev['title']} |\n"

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)
        
    print(f"Successfully generated news.json, news.csv and README.md with {len(filtered)} events!")

if __name__ == "__main__":
    main()