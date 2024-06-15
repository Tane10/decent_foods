from fastapi import APIRouter
from services.users_service import UserService

router = APIRouter()
user_service = UserService()


@router.get('/user')
def get_users():
    return user_service.get_users()


@router.post('/user')
def create_user():
    return user_service.create_user()


@router.get('/user/{user_id}')
def get_user_by_id(user_id: str):
    return user_service.get_user_by_id(user_id)
