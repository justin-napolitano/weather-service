.PHONY: build run logs
export DOCKER_BUILDKIT=1
build:
	docker build -t weather-service:local .
run: build
	docker run --rm --env-file .env -p 8789:8789 weather-service:local
logs:
	docker logs -f $$(docker ps -q -f ancestor=weather-service:local)
