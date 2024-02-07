# Hospital Management System

Hospital Management System is a web application built using Django, a high-level Python web framework, designed to manage hospital information efficiently.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)


## Introduction

The Hospital Management System allows hospitals to store and manage essential information such as hospital name, address, contact details, website, and capacity. It provides a user-friendly interface for viewing and managing hospital data.

## Features

- Add, view, edit, and delete hospitals.
- Display a landing page with basic information about the project.
- GraphQL endpoint to query hospitals.

## Project Structure

The project consists of the following main components:

- **hospitalProject**: Contains project-level settings and configuration.
- **hospital**: Contains the main application with models, views, and templates.

## Installation

To run the Hospital Management System locally, follow these steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/nonzoo/HosptalManagementSystem.git

2. **Navigate to the project directory**:
   
   ```bash
   cd HospitalManagementSystem

3. **Install dependencies**:
   
   ```bash
   pip install -r requirements.txt
   
4. **Apply database migrations**:
   
   ```bash
   python manage.py migrate

5. **Create a superuser account**:

   ```bash
   python manage.py createsuperuser

6. **Run the development server**:

   ```bash
   python manage.py runserver


## Usage
Once the application is running, you can perform the following actions:

- Visit the landing page at http://127.0.0.1:8000/ to view basic information about the Hospital Management System.
- Access the admin panel at http://127.0.0.1:8000/admin/ to manage hospitals.
- Use the GraphQL endpoint at http://127.0.0.1:8000/graphql/ to query hospitals.


## Contributing
Contributions are welcome! If you'd like to contribute to the project, please follow these steps:

- Fork the repository.
- Create a new branch for your feature or bug fix:
  ```bash
   git checkout -b feature-name
  
- Commit your changes:
   ```bash
   git commit -am 'Add new feature'.
   
- Push to the branch:
   ```bash
   git push origin feature-name.
- Submit a pull request.
