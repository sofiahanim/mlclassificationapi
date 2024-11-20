"""from fastapi import FastAPI
import joblib
import numpy as np

model = joblib.load('app/model.joblib')

class_names = np.array(['setosa', 'versicolor', 'virginica'])

app = FastAPI()

@app.get('/')
def read_root():
    return {'message': 'Iris model API'}

@app.post('/predict')
def predict(data: dict):
            
    features = np.array(data['features']).reshape(1, -1)
    prediction = model.predict(features)
    class_name = class_names[prediction][0]
    return {'predicted_class': class_name}
"""

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import joblib
import numpy as np
import os

model = joblib.load('app/model.joblib')
class_names = np.array(['setosa', 'versicolor', 'virginica'])

app = FastAPI()

# Mount a static file directory
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get('/')
def read_root():
    return FileResponse('static/index.html')

@app.post('/predict')
async def predict(request: Request):
    try:
        data = await request.json()
        features = data['features']
        np_features = np.array(features).reshape(1, -1)
        prediction = model.predict(np_features)
        class_name = class_names[prediction][0]
        return {'predicted_class': class_name}
    except Exception as e:
        return JSONResponse(status_code=400, content={"detail": str(e)})

