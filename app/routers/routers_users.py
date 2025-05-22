from typing import List

from fastapi import APIRouter

from app.models.models_users import User


router: APIRouter = APIRouter()
users: List[User] = []
user_counter: int = 1


@router.post('/users/', response_model=User)
def create_user(name: str) -> User:
    """
    Create a new user.
    Args:
        name: str = User's name for identification.
    Returns:
        User: User = The object created with an ID from DB.
    """
    print(f'{name=}')
    global user_counter
    new_user: User = User(id=user_counter, name=name)
    users.append(new_user)
    user_counter += 1

    return new_user


@router.get('/users/', response_model=List[User])
def list_users() -> List[User]:
    """
    List all users in db.
    Returns:
        List[User]: an list of objects registered in db.
    """

    return users
