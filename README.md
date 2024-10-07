# challenge1

# all the below commands must be run from cli

1. Use Docker Content Trust:
    - Enable Docker Content Trust (DCT) to ensure that you only pull signed images from trusted sources.

export DOCKER_CONTENT_TRUST=1

2. Build the Docker Image Securely

docker build -t python-webserver-secure .

3. Run the Secure Container
    - When you run the container, ensure that it operates with non-root privileges:

docker run -p 8000:8000 python-webserver-secure

OR

1. 	Limit Container Capabilities:
	- Use Docker’s capability drop to remove unnecessary Linux kernel capabilities when running the container. This command removes all capabilities except the ability to bind to network services.

docker run --cap-drop=ALL --cap-add=NET_BIND_SERVICE -p 8000:8000 python-webserver-secure

OR

1. Will use Read-Only Filesystem:
    - Run the container with a read-only filesystem for additional security:

docker run --read-only -p 8000:8000 python-webserver-secure
