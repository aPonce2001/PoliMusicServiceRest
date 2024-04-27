from fastapi import FastAPI

from routes.song import song

app = FastAPI()
app.include_router(song)
print("App started...")
