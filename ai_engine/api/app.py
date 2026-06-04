from fastapi import FastAPI

app = FastAPI(
    title="Campus Guardian AI",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Campus Guardian AI API Running"
    }