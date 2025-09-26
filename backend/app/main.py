from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import init_db
from .routers import users, menu, orders

app = FastAPI(title="Cafe Web System API")

# CORS (щоб фронт на 5500 міг звертатися)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # для локальної розробки ок
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ініціалізація БД
init_db()

# Підключення роутерів (єдиний префікс /api)
app.include_router(users.router,  prefix="/api")
app.include_router(menu.router,   prefix="/api")
app.include_router(orders.router, prefix="/api")

@app.get("/", tags=["health"])
def health():
    return {"status": "ok"}
