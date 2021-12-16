from fastapi import FastAPI, File, UploadFile
from fastapi.staticfiles import StaticFiles

app = FastAPI()

@app.get("/hello")
def read_hello():
  return {"Hello": "World"}

@app.post('/api/detect')
async def delect_image(file: UploadFile = File(...)):
  return {"file": file.filename}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
  return {"item_id": item_id, "q": q}

app.mount("/", StaticFiles(directory="html", html=True), name="html")

## uvicorn main:app --reload
## http://localhost:8000/docs
## http://localhost:8000/redoc
