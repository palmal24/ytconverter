from fastapi import FastAPI
from routes import converter_router
import uvicorn


app = FastAPI()
app.include_router(converter_router)


if __name__ == "__main__":
    config = uvicorn.Config("main:app", port=8000, log_level="info")
    server = uvicorn.Server(config)
    server.run()
