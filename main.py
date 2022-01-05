from fastapi import FastAPI
from fastapi import File
import uvicorn
from prediction import predict

app = FastAPI()

@app.post('/predict_size')
async def predict_size(img_front: bytes = File(...), img_side: bytes= File(...), height: int=160):

    #Predict
    res = predict(img_front, img_side, height)

    return res

if __name__ == "__main__":
    uvicorn.run(app, debug=True)
