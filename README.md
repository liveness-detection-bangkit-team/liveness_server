# Back-end server for Liveness Detection Capstone Bangkit team!

Repository for Back-end server for Liveness Detection company capstone team (Braincore)

## API Documentation

### Register Account

Endpoint: POST /auth/register

Request Body:

```bash
{
  "name": "fullname",
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
export FLASK_APP=src/app.py
flask --debug run -h 0.0.0.0
```
