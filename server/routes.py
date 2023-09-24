from typing import Annotated

from fastapi import Form, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import io

from utils.model import Model

router = APIRouter()

model = Model()


import base64


@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.post("/check_health")
async def check_plant_health(file: Annotated[str, Form()]):
    image_binary = base64.b64decode(file.split(",")[1])
    myImage = Image.open(io.BytesIO(image_binary))
    img = myImage.resize((256, 256))
    return {"result": model.isPlantHealthy(img)}
