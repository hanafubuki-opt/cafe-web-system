from fastapi import FastAPI
from .database import init_db
from .routers import users, menu, orders

app = FastAPI(title="Cafe Web System API")


init_db()


app.include_router(users.router, prefix="/api", tags=["users"])
app.include_router(menu.router,  prefix="/api", tags=["menu"])
app.include_router(orders.router, prefix="/api", tags=["orders"])

@app.get("/", tags=["health"])
def health():
    return {"status": "ok"}
