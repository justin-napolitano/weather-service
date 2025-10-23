import os
from fastapi import FastAPI, Query
import httpx
from dotenv import load_dotenv
load_dotenv()
app=FastAPI(title="weather-service",version="0.1.0")
CITY=os.getenv("CITY","Orlando"); STATE=os.getenv("STATE","FL")
NOTIFY_URL=os.getenv("NOTIFY_URL","http://notifier-gateway:8787/notify")
GATEWAY_TOKEN=os.getenv("GATEWAY_TOKEN",""); SIGNAL_NUMBER=os.getenv("SIGNAL_NUMBER","")
PORT=int(os.getenv("PORT","8789")); CRON_SCHEDULE=os.getenv("CRON_SCHEDULE","")
if CRON_SCHEDULE:
    with open("/app/crontab","w") as f: f.write(f"{CRON_SCHEDULE} curl -fsS http://127.0.0.1:{PORT}/push > /proc/1/fd/1 2>/proc/1/fd/2\n")
def get_weather_text(city:str)->str:
    try: return httpx.get(f"https://wttr.in/{city}?format=3",timeout=8).text.strip()
    except Exception as e: return f"Weather error: {e}"
@app.get("/run")
async def run(city: str=Query(default=None)):
    c=city or CITY; return {"ok":True,"city":c,"weather":get_weather_text(c)}
@app.get("/push")
async def push():
    if not (GATEWAY_TOKEN and SIGNAL_NUMBER): return {"ok":False,"error":"Missing GATEWAY_TOKEN or SIGNAL_NUMBER"}
    msg=f"☀️ Good morning! {CITY}, {STATE}: {get_weather_text(CITY)}"
    headers={"Authorization":f"Bearer {GATEWAY_TOKEN}","Content-Type":"application/json"}
    async with httpx.AsyncClient(timeout=10) as client:
        r=await client.post(NOTIFY_URL,headers=headers,json={"to":SIGNAL_NUMBER,"message":msg}); r.raise_for_status()
    return {"ok":True,"sent":True}
@app.get("/healthz")
def health(): return {"ok":True}
