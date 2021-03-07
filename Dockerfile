FROM python:3.7.3-stretch

# Working Directory
WORKDIR /app

# Copy source code to working directory
COPY . app.py app_utils.py main.py /app/
COPY templates/ /app/
COPY img_files/ xml_files/ txt_files/ /app/

# Install packages from requirements.txt
# hadolint ignore=DL3013
RUN pip install --no-cache-dir --upgrade pip &&\
    pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt
    
# Expose port 8080
EXPOSE 8080

# Run app.py at container launch
CMD ["python", "main.py"]