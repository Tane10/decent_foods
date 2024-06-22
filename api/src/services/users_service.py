from models import Users, UserRequestModel


def format_user(data: Users) -> dict[str, any]:
    return {
        'id': data.id,
        'name': data.name,
        'email': data.email,
        'wallet_uuid': data.wallet_uuid,
        'deleted': data.deleted
    }


class UserService:

    def get_users(self) -> list[dict[str, any]]:
        users = Users.select()

        user_list = []

        for user in users:
            user_list.append(format_user(user))

        return user_list

    def create_user(self, new_user: UserRequestModel) -> dict[str, any]:
        try:
            created_user = (
                Users.insert(
                    name=new_user.name,
                    email=new_user.email,
                    wallet_uuid=new_user.wallet_uuid).execute())
            response = format_user(created_user)
            return response
        except Exception as error:
            print("An exception occurred:", error)  # An exception occurred: division by zero

    def get_user_by_id(self, user_id) -> dict[str, any]:
        user = Users.get_by_id(user_id)
        return format_user(user)
