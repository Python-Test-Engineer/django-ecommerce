pip install gunicorn uvicorn

python -m gunicorn core.asgi:application -k uvicorn.workers.UvicornWorker

git rm -r --cached .