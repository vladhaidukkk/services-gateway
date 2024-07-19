import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from libs.commons.lib import print_hello_app

app = FastAPI(title="NCL Supplier Gateway")


@app.get("/", include_in_schema=False)
def index() -> RedirectResponse:
    print_hello_app("NCL")
    return RedirectResponse("/docs")


if __name__ == "__main__":
    uvicorn.run("apps.ncl.app.main:app", host="127.0.0.1", port=8003, reload=True)
