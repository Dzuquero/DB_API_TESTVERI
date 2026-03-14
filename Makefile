
run:
	docker compose up --build

test:
	pytest

migrate:
	alembic upgrade head
