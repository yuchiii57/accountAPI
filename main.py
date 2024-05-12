import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from router import account

def create_app():
    app = FastAPI()

    origins = [
        'http://localhost',
        'http://localhost:3000'
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins = origins,
        allow_methods = ['*'],
        allow_headers = ['*']
    )
    return app

app = create_app()
app.include_router(account.router)

@app.get("/")
def index():
    return {"Hello": "FastAPI"}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)