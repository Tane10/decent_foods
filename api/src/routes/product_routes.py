from fastapi import APIRouter
from services.products_service import ProductService

router = APIRouter()
product_service = ProductService()


@router.get('/product')
def get_users():
    return product_service.get_users()


@router.post('/product')
def create_user():
    return product_service.create_user()


@router.get('/product/{product_id}')
def get_user_by_id(user_id: str):
    return product_service.get_user_by_id(user_id)
