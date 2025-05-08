from dotenv import load_dotenv
load_dotenv()

import boto3, os, uuid
s3 = boto3.client(
  "s3",
  aws_access_key_id = os.getenv("AWS_ID"),
  aws_secret_access_key = os.getenv("AWS_KEY"),
  region_name = os.getenv("AWS_REGION")
)

BUCKET_NAME = "hamgym"

def upload(image):
  rnd_name = uuid.uuid4().hex[:8]
  image.filename = rnd_name
  s3.upload_fileobj(
    image.file,
    BUCKET_NAME,
    image.filename,
    ExtraArgs={"ContentType": image.content_type}
  )
  image_url = f"https://d2j1hqbdhu9zhx.cloudfront.net/{image.filename}"
  return image_url