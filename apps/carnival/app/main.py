import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from libs.commons.lib import print_hello_app

app = FastAPI(title="Carnival Supplier Gateway")


@app.get("/", include_in_schema=False)
def index() -> RedirectResponse:
    print_hello_app("Carnival")
    return RedirectResponse("/docs")


if __name__ == "__main__":
    uvicorn.run("apps.carnival.app.main:app", host="127.0.0.1", port=8001, reload=True)