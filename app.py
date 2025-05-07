from fastapi import FastAPI, Form, Request, UploadFile
from fastapi.responses import FileResponse
app = FastAPI()


import boto3
s3 = boto3.resource("s3")
BUCKET_NAME = "hamgym"


@app.get("/")
async def get_index(request:Request):
  return FileResponse("./static/index.html", media_type="text/html")

from models.rdb import *
@app.post("/article")
async def post_article(text:str=Form(), image:UploadFile=Form()):
  if image.size==0 or image.filename=="":
    return {"text": text, "imageURL": None}
  s3.Bucket(BUCKET_NAME).put_object(Key=image.filename, Body=image.file)
  image_url = f"https://d2j1hqbdhu9zhx.cloudfront.net/{image.filename}"
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