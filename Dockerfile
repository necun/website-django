# Step 1: Use a Python base image
FROM python:3.9-slim

# Step 2: Set the working directory
WORKDIR /app

# Step 3: Copy the requirements file into the container
COPY requirements.txt /app/

# Step 4: Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the entire project into the container
COPY . /app/

# Step 6: Collect static files for production
RUN python manage.py collectstatic --noinput

# Step 7: Expose the port Django runs on
EXPOSE 8000

# Step 8: Command to run the Django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
