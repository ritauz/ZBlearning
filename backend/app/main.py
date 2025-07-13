from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/hello")
def hello():
    return {"message": "Hello from FastAPI"}

handler = Mangum(app)

# ローカル開発用の起動
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
