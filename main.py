from fastapi import FastAPI
from fastapi.responses import JSONResponse
import base64

app = FastAPI()

@app.get("/")
async def root():
    return {"Hello": "World"}

@app.get("/gender")
async def gender(gender: str):
    return {"Gender": gender}

@app.get("/send-image")
async def send_image():
    # 1. 이미지를 읽고 Base64로 인코딩
    with open("download_test_image.png", "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode('utf-8')

    # 2. JSON 형태로 응답
    return JSONResponse(content={"image_data": base64_image})