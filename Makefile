.PHONY: run
run:
	python3 ipv4.py

.PHONY: unittest
unittest:
	python3 -m unittest

.PHONY: docker-image
docker-image:
	docker build -t ip-subnet-calculator:latest .

.PHONY: run-container
run-container:
	docker run -it ip-subnet-calculator:latest

