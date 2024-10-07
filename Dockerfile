# 1. Use a minimal and non-root base image
# Use an official Python runtime as a parent image, choosing a slim or minimal base image
FROM python:3.12-slim

# 2. Set environment variables (avoid sensitive information)
# This improves security by avoiding sensitive information in the code itself
ENV PYTHONUNBUFFERED=1

# 3. Create a non-root user
# It's a good practice to create a user to run your application instead of using the root user
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser

# 4. Set the working directory in the container
WORKDIR /app

# 5. Copy only the necessary files
# Avoiding copying unnecessary files from the local system (e.g., tests, docs) into the container
COPY mywebsite-arguments.py /app/

# 6. Install dependencies securely (if needed)
# Update the package lists and install any necessary system dependencies securely with no-cache
RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*  # Clean up cache to reduce image size and prevent attacks

# 7. Use non-root user for execution
USER appuser

# 8. Expose only the necessary port
EXPOSE 8000

# 9. Define the entrypoint and default command
# Allow for passing in runtime arguments and ensure the script runs as non-root
ENTRYPOINT ["python", "mywebsite-arguments.py"]
CMD ["--host", "0.0.0.0", "--port", "8000"]