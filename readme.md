# Instructions

Create a venv (for me it is with python 3.9)

    python -m venv .venv
    pip install prefect==2.10.13

In the venv terminal:

    $env:PREFECT_API_URL='http://127.0.0.1:4200/api'
    prefect server start

In another venv terminal:

    python deployment.py

In another venv terminal:

    $env:PREFECT_API_URL='http://127.0.0.1:4200/api'
    prefect agent start -p default-agent-pool

Then run the deployement. As for me, I did it from the webview but it works from terminal and python script also.