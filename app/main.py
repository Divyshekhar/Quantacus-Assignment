from fastapi import FastAPI
from app.db.database import create_db_and_tables
from app.routes.upload_routes import router as upload_router
from app.routes.product_routes import router as product_router
from app.routes.dashboard_routes import router as dashboard_router
from app.routes.alert_routes import router as alert_router
from app.routes.competitor_routes import router as competitor_router
from app.routes.job_routes import router as job_router

app = FastAPI(
    title = "Product Intelligence Dashboard API"
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    

app.include_router(upload_router)
app.include_router(product_router)
app.include_router(dashboard_router)
app.include_router(alert_router)
app.include_router(competitor_router)
app.include_router(job_router)


@app.get("/")
async def root():
    return {"message": "Server is running"}

@app.get("/health")
async def health():
    return {"message": "Server is running and healthy"}