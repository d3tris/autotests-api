import pytest
from pydantic import BaseModel
from fixtures.files import FileFixture
from fixtures.users import UserFixture
from clients.courses.courses_client import CoursesClient, get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema, CreateCourseResponseSchema


# вспомогательный класс представляет объект с данными созданного курса
class CourseFixture(BaseModel):
    request: CreateCourseRequestSchema  # содержит данные запроса на создание курса
    response: CreateCourseResponseSchema  # содержит ответ API после создания курса


@pytest.fixture
# Фикстура создает клиент CoursesClient, который используется для взаимодействия с API курсов.
# В аргумент передается function_user — фикстура, предоставляющая тестового пользователя.
# Используется get_courses_client, который создает и возвращает объект CoursesClient, уже аутентифицированный от имени данного пользователя.
# Теперь в тестах можно использовать courses_client для отправки запросов в API курсов
def courses_client(function_user: UserFixture) -> CoursesClient:
    return get_courses_client(function_user.authentication_user)


@pytest.fixture
# Фикстура создает тестовый курс перед выполнением теста и возвращает объект с данными созданного курса
def function_course(
        courses_client: CoursesClient,
        function_user: UserFixture,
        function_file: FileFixture
) -> CourseFixture:
    request = CreateCourseRequestSchema(
        preview_file_id=function_file.response.file.id,
        created_by_user_id=function_user.response.user.id
    )
    response = courses_client.create_course(request)
    return CourseFixture(request=request, response=response)
