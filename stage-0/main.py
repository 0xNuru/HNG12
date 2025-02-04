from datetime import datetime, timezone

from fastapi import FastAPI, status
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/stage-0", status_code=status.HTTP_200_OK)
def read_root():
    return {
        "email": "0xnuru@gmail.com",
        "current_datetime": datetime.now(timezone.utc).isoformat(),
        "github_url": "https://github.com/0xNuru/HNG12/tree/main/stage-0",
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
