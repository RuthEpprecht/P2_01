from fastapi import FastAPI, HTTPException, Request 
from fastapi.openapi.docs import get_swagger_ui_html
from starlette.responses import RedirectResponse, JSONResponse

from task_manager.controllers.controller_task import task_router

app = FastAPI(
    title="Task API",
    description="API para gerenciamento de tarefas.",
    version="0.1",
    openapi_url="/openapi.json",
    docs_url=None,
    redoc_url=None,
    contact={
        "name": "Matheus de Almeida Cantarutti",
        "email": "cantaruttim@outlook.com"
    },
    license_info={
        "name": "Development Server - API",
        "url": "http://localhost:8000"
    }
)

# Inclui o roteador para as rotas de tarefas
app.include_router(task_router)

# Manipulador de exceções HTTP
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail}
    )

# Manipulador de exceções gerais
@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": "An unexpected error occurred"}
    )

# Redireciona a raiz para a documentação
@app.get("/", tags=["Redirect"], include_in_schema=False)
async def redirect_to_docs():
    return RedirectResponse(url="/docs")

# Configura a documentação do Swagger UI
@app.get("/docs", tags=["Redirect"], include_in_schema=False)
async def get_swagger_ui():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title="Swagger UI"
    )

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

    