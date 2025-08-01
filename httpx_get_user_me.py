import httpx

login_payload = {
    "email": "dar@gmail.com",
    "password": "password12345"
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

get_header = {"Authorization": f"Bearer {login_response_data["token"]["accessToken"]}"}
get_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=get_header)
get_response_data = get_response.json()
print("Get response:", get_response_data)
print("Status Code:", get_response.status_code)
