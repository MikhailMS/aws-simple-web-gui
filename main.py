import httpx

from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
def read_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})


@app.post("/process")
async def process_form(request: Request, token: str = Form(...), method: str = Form(...), aws_url: str = Form(...)):
    async with httpx.AsyncClient() as client:
        try:
            headers = {
                "Authorization": token,
                "CalledMethod":  method
            }

            response = await client.get(f'{aws_url}/{method}', headers=headers)
            response.raise_for_status()

            response_data = response.text
            if len(response_data) == 0:
                response_data = response.json()

            return templates.TemplateResponse("result.html", {"request": request, "method": method, "data": response_data})

        except httpx.HTTPStatusError as err:
            return templates.TemplateResponse("result.html", {"request": request, "method": method, "data": f"Response to AWS failed with error code: {err.response.status_code}"})
        except httpx.ConnectError as err:
            return templates.TemplateResponse("result.html", {"request": request, "method": method, "data": f"Response to AWS failed with error code: {err}"})


# if __name__ == "__main__":
#     import uvicorn

#     uvicorn.run(app, host="127.0.0.1", port=8000)
