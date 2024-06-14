from models import Users


class UserService:

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
