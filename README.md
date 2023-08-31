# RapidFort Assignment Documentation

## Project Overview

The main goal of this project is to create a web server that enables users to upload files and access details about the uploaded files. The project includes the following tasks:

1. **Set Up a REST API Server:** Construct a REST API server that can handle file uploads and provide comprehensive file information.

2. **Define the API:** Clearly outline the REST API endpoints and methods (GET, POST) to facilitate both file uploads and retrieval of information.

3. **Integrate User-Friendly UI:** Enhance user experience by implementing a basic web-based interface that makes it easy for users to upload files and retrieve information.

4. **Automate Docker Build with GitHub Action:** Streamline the process of building Docker containers by utilizing GitHub Actions or a similar CI/CD pipeline.

5. **Initiate Container Launch Using Bash Script:** Develop a Bash script to launch the Docker container effortlessly.

6. **Create Kubernetes Manifest Files:** Generate Kubernetes manifest files that effectively deploy and manage the web server application within a Kubernetes cluster.

## API Documentation

| Endpoint       | GET `/`                |
|----------------|------------------------|
| **Description**| Endpoint to check the server status. |
| **Response**   | - HTTP Status Code: 200 OK<br>- Response Body: `{"message": "API is running"}` |

| Endpoint       | POST `/upload/`                    |
|----------------|------------------------------------|
| **Description**| Endpoint to upload files and retrieve their information. |
| **Request**    | - Method: POST<br>- Headers: `Content-Type: multipart/form-data`<br>- Body: Form data with the uploaded file(s) |
| **Response**   | - HTTP Status Code: 200 OK<br>- Response Body: JSON containing information about uploaded file(s), e.g.:<br>json<br>{<br>  "files": [<br>    {<br>      "filename": "file.txt",<br>      "size": 1234,<br>      "path": "/app/uploads/"<br>    }<br>  ]<br>} |

## GitHub Repository

The entire project is stored within a GitHub repository: [https://github.com/AbhinandanGautam/Rapidfort-Task](https://github.com/AbhinandanGautam/Rapidfort-Task)

This repository incorporates the following components:

- Source code for index.html
- app.py serving as the backend for this flask application
- Dockerfile for orchestrating the Docker container construction
- GitHub Actions configuration file for automating Docker builds (.github/workflows/docker-image.yml)
- Bash script for effortlessly running the Docker container
- Kubernetes manifest files aimed at deploying the application within a Kubernetes cluster