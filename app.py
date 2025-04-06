import pandas as pd
from fastapi import FastAPI
import httpx
import sqlite3
import asyncio
from datetime import datetime

app = FastAPI()

#Secure credentials
sr_api_key = ''
ot_api_key = ''
sr_url = 'https://api.sevenrooms.com/v1/reservations'
ot_url = 'https://platform.opentable.com/v2/reservations'


#async function to fetch data from each API
async def fetch_data(url: str, headers: dict):
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        response.raise_for_status()
        return response.json()


async def get_raw_data():
    sr_headers = {}
    ot_headers = {'Authorization': 'bearer '}

    sr_fetch = fetch_data(sr_url, sr_headers)
    ot_fetch = fetch_data(ot_url, ot_headers)


def transform_data(sr_data, ot_data):
    sr_df = pd.DataFrame(sr_data[''])
    ot_df = pd.DataFrame(ot_data[''])

    sr_df = sr_df.rename(columns={})
    ot_df = ot_df.rename(columns={})

    sr_df['Origin'] = 'SevenRooms'
    ot_df['Origin'] = 'OpenTable'

    comb_df = pd.concat([sr_df, ot_df]).drop_duplicates(subset=['ID', 'datetime'], keep='last')
    return comb_df


def store_data(df):
    conn = sqlite3.connect('reservations.db')
    df.to_sql('reservations', conn, if_exists='replace', index=False)
    conn.close()


async def sync_data(df: pd.DataFrame):
    async with httpx.AsyncClient() as client:
        for _, row in df.iterrows():
            payload = {
                'ID': row['ID'],
                'Name': row['Name'],
                'datetime': row['datetime'],
                'Origin': row['Origin']
            }

            if row["source"] != "sevenrooms":
                await client.post(sr_url, json=payload,
                                  headers={"Authorization": f"Bearer {SEVENROOMS_API_KEY}"})
            if row["source"] != "opentable":
                await client.post(ot_url, json=payload, headers={"Authorization": f"Bearer {OPENTABLE_API_KEY}"})

@app.get("/sync")
async def sync_reservations():
    sr_data, ot_data = await get_raw_data()
    comb_df = transform_data(sr_data, ot_data)
    store_data(comb_df)
    await sync_data(comb_df)
    return {"message": "Data synced successfully", "timestamp": datetime.now().isoformat()}


@app.get("/reservations")
def get_reservations():
    conn = sqlite3.connect("reservations.db")
    df = pd.read_sql_query("SELECT * FROM reservations", conn)
    conn.close()
    return df.to_dict(orient="records")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)



