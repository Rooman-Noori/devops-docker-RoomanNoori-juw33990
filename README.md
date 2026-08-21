# DevOps Docker Project

A containerized web application developed as part of a DevOps and Docker project. The application is packaged using Docker to provide a consistent and portable development and deployment environment.

## 📌 Project Overview

This project demonstrates the use of **Docker** to containerize a Python-based web application. It includes the application source code, dependencies, Docker configuration, and frontend templates.

The main goal is to understand how an application can be:

* Containerized using Docker
* Configured with a Dockerfile
* Installed with required Python dependencies
* Run consistently across different environments
* Accessed through a web browser

## 🛠️ Technologies Used

* **Python**
* **Flask**
* **Docker**
* **HTML**
* **CSS**
* **JavaScript**
* **Git & GitHub**

## 📂 Project Structure

```text
devops-docker-RoomanNoori-juw33990/
│
├── Dockerfile
├── app.py
├── requirements.txt
├── templates/
│   └── ...
├── static/
│   └── ...
└── README.md
```

## 🐳 Docker Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Rooman-Noori/devops-docker-RoomanNoori-juw33990.git
```

### 2. Navigate to the Project

```bash
cd devops-docker-RoomanNoori-juw33990
```

### 3. Build the Docker Image

```bash
docker build -t devops-docker-app .
```

### 4. Run the Docker Container

```bash
docker run -d -p 5000:5000 --name devops-docker-app devops-docker-app
```

### 5. Open the Application

Open your browser and visit:

```text
http://localhost:5000
```

## 🔧 Useful Docker Commands

Check running containers:

```bash
docker ps
```

View application logs:

```bash
docker logs devops-docker-app
```

Stop the container:

```bash
docker stop devops-docker-app
```

Start the container again:

```bash
docker start devops-docker-app
```

Remove the container:

```bash
docker rm devops-docker-app
```

## 🎯 Project Objectives

* Learn Docker containerization
* Understand Dockerfile configuration
* Manage Python application dependencies
* Run a web application inside a Docker container
* Practice DevOps concepts and deployment workflows
* Use GitHub for source-code management

## 🚀 Future Improvements

* Add Docker Compose support
* Implement environment variables for configuration
* Add automated testing
* Set up CI/CD using GitHub Actions
* Deploy the containerized application to a cloud platform

## 👩‍💻 Author

**Rooman Noori**

BS Software Engineering
Jinnah University for Women

### GitHub

https://github.com/Rooman-Noori
