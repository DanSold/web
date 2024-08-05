DEVELOPER -> danKo

Terminal:

pip install fastapi[all] pytest pytest-asyncio

uvicorn app.main:app --reload --port 8000

docker compose up

docker compose down

alembic init migration

alembic revision --autogenerate -m 'initial'