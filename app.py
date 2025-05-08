from fastapi import FastAPI, Form, Request, UploadFile
from fastapi.responses import FileResponse
from models.bucket import upload
from models.rdb import CRUD
app = FastAPI()


@app.get("/")
async def get_index(request:Request):
  return FileResponse("./static/index.html", media_type="text/html")


@app.post("/article")
async def post_article(text:str=Form(), image:UploadFile=Form()):
  if image.size==0 or image.filename=="":
    return {"text": text, "imageURL": None}
  image_url = upload(image)
  CRUD.create_article(text, image_url)
  return {"text": text, "imageURL": image_url}
@app.get("/article")
async def get_article():
  rows = CRUD.read_article()
  return rows
@app.delete("/article")
async def delete_article():
  CRUD.delete_article()
  return {"message": "OK"}