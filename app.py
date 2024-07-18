from fastapi import FastAPI
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import RedirectResponse, FileResponse
from main import main

import os
import shutil
import uuid

IMAGEDIR = 'images/'
RESULTS = 'results/'
os.makedirs(IMAGEDIR, exist_ok=True)
os.makedirs(RESULTS, exist_ok=True)

app = FastAPI()

@app.post('/upload/')
async def upload_file(file: UploadFile = File(...)):
    file.filename = f'{uuid.uuid4()}.jpg'
    contents = await file.read()

    with open(f'{IMAGEDIR}{file.filename}', 'wb') as f:
        f.write(contents)
    return RedirectResponse(url=f"/compliance/?filename={IMAGEDIR}{file.filename}", status_code=303)

@app.get("/compliance/", include_in_schema=False)
async def check_compliance(filename:str):
    main(filename)
    file = filename.split("/")[-1]
    return RedirectResponse(url=f"/display/?file={RESULTS}{file}", status_code=303)

@app.get("/display/", include_in_schema=False)
async def display_image(file:str):
    file_location = f'{file}'

    return FileResponse(file_location)