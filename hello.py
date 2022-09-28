from fastapi import FastAPI
app = FastAPI()
@app.get("/")
async def root(mahasiswa: dict):
  return mahasiswa