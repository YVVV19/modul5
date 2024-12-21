from fastapi import FastAPI, Path, Header, Query
from datetime import datetime

app=FastAPI()

@app.get("/data/")
async def get_data(
    user_id: int = Path(...),
    timestamp: str = Query(default=None),
    client: str = Header(...),
    ):
    if not timestamp:
        timestamp == datetime.timestamp()
        return{"Hello":client,
            "user_id:":user_id,
            "time:":timestamp,}
    else:
        return{"Hello":client,
            "user_id:":user_id,
            "time:":timestamp,}