from pydantic import BaseModel, Field


class Address(BaseModel):
    city: str
    zipcode: str


class User(BaseModel):
    id: int
    name: str
    email: str
    # address: Address
    is_active: bool = Field(alias='isActive')


user_data = {
    'id': 1,
    'name': 'Alice',
    'email': 'alice@example.com',
    'isActive': True
}
user = User(**user_data)

# user = User(
#     id=1,
#     name='Alice',
#     email='alice@example.com'
#     # address=Address(city="Warsaw", zipcode="101011")
# )

print(user.model_dump())
print(user.model_dump_json())
