import pytest
from pydantic import BaseModel
from fixtures.users import UserFixture
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema
from clients.files.files_client import FilesClient, get_files_client


class FileFixture(BaseModel):
    request: CreateFileRequestSchema  # данные запроса на загрузку файла
    response: CreateFileResponseSchema  # ответ от API после успешного создания файла


@pytest.fixture
# Эта фикстура создает клиент FilesClient, который будет использоваться для работы с API загрузки файлов.
# В аргумент передается function_user — пользователь, полученный через фикстуру UserFixture.
# Используется метод get_files_client, который создает клиент, уже настроенный для работы от имени данного пользователя.
# Фикстура возвращает объект FilesClient, который можно использовать в тестах.
def files_client(function_user: UserFixture) -> FilesClient:
    return get_files_client(function_user.authentication_user)


@pytest.fixture
# Эта фикстура автоматически создает тестовый файл перед каждым тестом и возвращает информацию о нем
def function_file(files_client: FilesClient) -> FileFixture:
    request = CreateFileRequestSchema(upload_file="./testdata/files/image.png")
    response = files_client.create_file(request)
    return FileFixture(request=request, response=response)
