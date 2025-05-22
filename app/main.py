from typing import Dict

from fastapi import FastAPI

from app.routers import routers_products, routers_users


MESSAGE_HOME: str = "Welcome to API of Product's Recomendatinos"
app = FastAPI()
app.include_router(routers_products.router)
app.include_router(routers_users.router)


@app.get('/')
def home() -> Dict[str, str]:
    global MESSAGE_HOME

    return {'message': MESSAGE_HOME}
