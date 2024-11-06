# Back-end server for Liveness Detection Capstone Bangkit team!

## How to run

### Create python3 virtual env

```bash
python3 -m venv myenv
```

### Activate Python 3 virtual env

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
