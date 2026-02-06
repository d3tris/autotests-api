import pytest
from pydantic import BaseModel, EmailStr
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from clients.users.public_users_client import get_public_users_client, PublicUsersClient
from clients.users.private_users_client import PrivateUsersClient, get_private_users_client


# cоздаем дополнительный слой UserFixture, который объединяет запрос и ответ
class UserFixture(BaseModel):
    request: CreateUserRequestSchema  # запрос на создание пользователя (там есть email и пароль)
    response: CreateUserResponseSchema  # ответ с данными пользователя (но без пароля)

    @property
    def email(self) -> EmailStr:  # user pwd
        return self.request.email

    @property
    def password(self) -> str:  # user pwd
        return self.request.password

    @property
    def authentication_user(self) -> AuthenticationUserSchema:
        return AuthenticationUserSchema(email=self.email, password=self.password)


@pytest.fixture
def public_users_client() -> PublicUsersClient:
    # Создаем новый API клиент для работы с публичным API пользователей
    return get_public_users_client()


@pytest.fixture  # создаёт пользователя перед каждым тестом
# {scope фикстуры}_{название создаваемой сущности}
# Используем фикстуру public_users_client, которая создает нужный API клиент
def function_user(public_users_client: PublicUsersClient) -> UserFixture:
    request = CreateUserRequestSchema()
    response = public_users_client.create_user(request)
    return UserFixture(request=request, response=response)


@pytest.fixture
def private_users_client(function_user: UserFixture) -> PrivateUsersClient:
    return get_private_users_client(function_user.authentication_user)
