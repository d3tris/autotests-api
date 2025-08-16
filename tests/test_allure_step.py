import allure


# def test_feature():
#     with allure.step("Building API client"):
#         ...
#
#     with allure.step("Create course"):
#         ...
#
#     with allure.step("Deleting course"):
#         assert False


@allure.step("Building API client")
def build_api_client():
    with allure.step("Get user authentication tokens"):
        ...

    with allure.step("Create new API client"):
        ...


@allure.step("Creating course with title '{title}'")
def create_course(title: str):
    ...


@allure.step("Deleting course")
def delete_course():
    ...


def test_feature():
    build_api_client()
    create_course(title="A")
    create_course(title="B")
    create_course(title="C")
    create_course(title="D")
    delete_course()
