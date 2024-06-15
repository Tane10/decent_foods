from fastapi import FastAPI
from routes import user_routes, transaction_routes
from models import db

app = FastAPI()
db.connect()
app.include_router(user_routes.router)
app.include_router(transaction_routes.router)

# what we need to run to get it working
# fastapi dev main.py
