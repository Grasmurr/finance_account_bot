from sqlalchemy.orm import Session

from repository.users import UserRepository


class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def get_or_create_user(self, user_id, username, full_name):
        user = self.user_repo.get_user(user_id)
        if not user:
            return self.user_repo.create_user(user_id, username, full_name)



