import uvicorn
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import HTMLResponse

app = FastAPI()


@app.get('/', summary="获取IP", description="获取远程调用者ip", response_class=HTMLResponse)
async def api_ip_auth(request: Request):
    return request.client.host


@app.get("/version", include_in_schema=False, description='获取后端版本号', response_class=HTMLResponse)
async def version():
    return app.version


if __name__ == '__main__':
    uvicorn.run(app=app,
                host="0.0.0.0",
                port=80,
                reload=False,
                # debug=True,
                # log_config=log.service_log(),
                # ssl_keyfile=server_ssl() + para('server', 'ssl_keyfile'),
                # ssl_certfile=server_ssl() + para('server', 'ssl_certfile')
                )
