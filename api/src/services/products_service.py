from models import Products


class ProductService:

    def get_users(self):
        users = Users.select()

        user_list = []

        for user in users:
            user_list.append({
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'wallet_uuid': user.wallet_uuid,
                'deleted': user.deleted
            })

        return user_list

    def create_user(self):
        return None

    def get_user_by_id(self, user_id):
        user = Users.get_by_id(user_id)
        return {
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'wallet_uuid': user.wallet_uuid,
            'deleted': user.deleted
        }
