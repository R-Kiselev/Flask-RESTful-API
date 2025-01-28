.PHONY: init build run db-init db-migrate db-upgrade

init:  build run
	docker-compose exec backend flask db init
	docker-compose exec backend flask db migrate
	docker-compose exec backend flask db upgrade
	docker-compose exec backend flask init
	@echo "Init done, containers running"

build:
	docker-compose build

run:
	docker-compose up -d

down:
	docker-compose down

db-init:
	docker-compose exec backend flask db init

db-migrate:
	docker-compose exec backend flask db migrate

db-upgrade:
	docker-compose exec backend flask db upgrade
