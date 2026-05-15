# CI/CD Python Flask Pipeline

This repository contains a full-cycle CI/CD automation pipeline for a Python Flask Web Application using **Jenkins** and **GitHub**.

## 🚀 Project Overview
The main goal of this task is to implement a continuous integration and continuous deployment (CI/CD) workflow. The pipeline automates the checkout, build environment, testing phase, and application deployment dynamically.

---

## 🛠️ Pipeline Architecture
The `Jenkinsfile` defines a declarative pipeline with the following stages:

1. **Checkout**: Automatically pulls the latest source code from this GitHub repository.
2. **Build**: Simulates/Validates the installation of application dependencies from `requirements.txt`.
3. **Test**: Simulates running automated unit tests (`pytest`) to ensure code quality before deployment.
4. **Deploy**: Deploys and initiates the Flask application environment on the local server.

---

## 📂 Project Structure
```text
├── app.py                # Main Flask Application
├── test_app.py           # Pytest script for testing endpoints
├── requirements.txt      # Python dependencies (Flask, Pytest)
├── Jenkinsfile           # Jenkins Automation Pipeline Script
└── README.md             # Project Documentation (This file)
