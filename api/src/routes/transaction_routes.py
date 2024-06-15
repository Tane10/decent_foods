from fastapi import APIRouter
from services.transactions_service import TransactionsService

router = APIRouter()
transaction_service = TransactionsService()


@router.get('/transactions')
def get_users():
    return transaction_service.get_transactions()


@router.post('/transactions')
def create_user():
    return transaction_service.create_transaction()


@router.get('/transactions/{id}')
def get_user_by_id(id: str):
    return transaction_service.get_transaction_by_id(id)
