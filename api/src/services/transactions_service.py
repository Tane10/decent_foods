from models import Transactions


class TransactionsService:

    def get_transactions(self):
        transactions = Transactions.select()

        transactions_list = []

        for t in transactions:
            transactions_list.append({
                'id': t.id,
                'timestamp': t.timestamp,
                'cost': t.cost,
                'sellers_wallet_uuid': t.sellers_wallet_uuid,
                'customer_wallet_uuid': t.customer_wallet_uuid,
                'product_uuid': t.product_uuid,
                'delivery_option': t.delivery_option,
                'longitude': t.longitude,
                'latitude': t.latitude
            })

        return transactions_list

    def create_transaction(self):
        return None

    def get_transaction_by_id(self, trans_id):
        transaction = Transactions.get_by_id(trans_id)
        return {
            'id': transaction.id,
            'timestamp': transaction.timestamp,
            'cost': transaction.cost,
            'sellers_wallet_uuid': transaction.sellers_wallet_uuid,
            'customer_wallet_uuid': transaction.customer_wallet_uuid,
            'product_uuid': transaction.product_uuid,
            'delivery_option': transaction.delivery_option,
            'longitude': transaction.longitude,
            'latitude': transaction.latitude
        }
