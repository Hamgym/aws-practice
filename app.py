from fastapi import FastAPI, Form, Request, UploadFile
from fastapi.responses import FileResponse
app = FastAPI()


import boto3
s3 = boto3.resource('s3')
BUCKET_NAME = "hamgym"


@app.get("/")
async def get_index(request:Request):
  return FileResponse("./static/index.html", media_type="text/html")


@app.post("/article")
async def post_article(text:str=Form(), image:UploadFile=Form()):
  s3.Bucket(BUCKET_NAME).put_object(Key=image.filename, Body=image.file)
  return {"text": text}