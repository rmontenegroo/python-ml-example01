IMAGE?=app
TAG?=latest

base: Dockerfile-base
		docker build -f Dockerfile-base . -t $(IMAGE)-base:latest

build: base Dockerfile
		docker build . -t $(IMAGE):$(TAG) --build-arg IMAGEBASE=$(IMAGE)-base:latest

run: build
		docker run -ti -p 8080:8080 $(IMAGE):$(TAG)