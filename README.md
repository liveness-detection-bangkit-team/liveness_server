# Back-end server for Liveness Detection Capstone Bangkit team

Repository for Back-end server for Liveness Detection company capstone team (Braincore)

## API Documentation

url: https://liveness-server-653064696167.asia-southeast2.run.app/

### Response API

Endpoint: GET /

Response Success:

```bash
{
  "status_code": 200,
  "message": "You found me!"
}
```

### Response API with Token required

Endpoint: GET /home

Request Cookies:

- X-LIVENESS-TOKEN

Response Success:

```bash
{
  "status_code": 200,
  "message": "Hello {fullname}"
}
```

Response Failed:

```bash
{
  "status_code": 401,
  "message": "Unauthorized users"
}
```

### Register Account

Endpoint: POST /auth/register

Request Body:

```bash
{
  "fullname": "fullname",
  "username": "username",
  "password": "password"
}
```

> [!IMPORTANT]
>
> - The request body is mandatory.
> - The request body must be at least 5 characters long.

Response Body Success:

```bash
{
  "status_code": 201,
  "message": "Successfully created account!"
}
```

Response Body Failed:

```bash
{
  "status_code": 400,
  "message": "Name, Username, and Password is required"
}
```

### Login Account

Endpoint: POST /auth/login

Request Body:

```bash
{
  "username": "username",
  "password": "password"
}
```

> [!IMPORTANT]
>
> - The request body is mandatory.

Response Body Success:

```bash
{
  "status_code": 200,
  "message": "Login successfully!"
}
```

Response Body Failed:

```bash
{
  "status_code": 400,
  "message": "Username and Password is required"
}
```

Response wrong username:

```bash
{
  "status_code": 400,
  "message": "Username not found!"
}
```

Response wrong password:

```bash
{
  "status_code": 400,
  "message": "Password is incorrect!"
}
```

### Logout Account

Endpoint: DELETE /auth/logout

Request Cookies:

- X-LIVENESS-TOKEN

Response Success:

```bash
{
  "status_code": 200,
  "message": "Logged out"
}
```

### Delete Account

Endpoint: DELETE /user/delete

Request Cookies:

- X-LIVENESS-TOKEN

Response Success:

```bash
{
  "status_code": 200,
  "message": "Successfully deleted user!"
}
```

Response Body Failed:

```bash
{
  "status_code": 400,
  "message": "Unauthorized users"
}
```

Response Delete Failed:

```bash
{
  "status_code": 400,
  "message": "Failed to delete user!"
}
```

## How to run

### Create Python 3 virtual environment

```bash
python3 -m venv myenv
```

### Activate Python 3 virtual environment

```bash
source myenv/bin/activate
```

### Install packages

```bash
pip install -r requirements.txt
```

### Run Flask

Run in development mode to listen every change

```bash
export FLASK_APP=main.py
flask --debug run -h 0.0.0.0
```
