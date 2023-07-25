init:
	alembic init alembic
migrate:
	alembic revision --autogenerate -m "$(m)"
upgrade:
	alembic upgrade head
downgrade:
	alembic downgrade -1
