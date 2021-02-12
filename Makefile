all: build run

build:
	viash build -p docker -m -s config.vsh.yaml

run:
	viash run -p docker config.vsh.yaml -- --input ipsum.md --output ipsum.html
