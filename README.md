# REST_API_Mongo
Simple REST API build with Flask and MongoDB

## Table of Contents

- [Introduction](#introduction)
- [Technologies Used](#technologies-used)
- [Setup](#setup)
- [Usage](#usage)
- [Endpoints](#endpoints)

## Introduction

Welcome to the Simple REST API Project! This project aims to provide a straightforward and efficient solution for managing and querying data related to parts and categories through a RESTful API.

## Purpose

The primary purposes of this project are:

1. **Parts Management:** Enable users to perform CRUD (Create, Read, Update, Delete) operations on parts, where each part has essential attributes such as serial number, name, description, category, quantity, and price.

2. **Categories Management:** Allow users to manage categories, providing a hierarchical structure for organizing parts.

3. **Search Functionality:** Implement a search feature that enables users to find parts based on various criteria.

## Key Features

- **Parts Management:** Users can add, update, delete, and retrieve details of individual parts.

- **Categories Management:** Users can create, update, delete, and view details of categories.

- **Search Functionality:** Users can perform searches for parts based on specified criteria, enhancing the discoverability of relevant items.

## Technologies Used

Flask
Flask is a lightweight and flexible Python web framework. It's easy to use and allows for rapid development of web applications, used with Flask-MongoEngine extension it simplifies integration with MongoDB using the MongoEngine ODM (Object-Document Mapper). It provides easy-to-use tools for working with MongoDB databases in Flask applications.

MongoEngine
Description: MongoEngine is a Python Object-Document Mapper (ODM) that provides a high-level abstraction for interacting with MongoDB databases. It simplifies the integration of MongoDB with Python applications.

These technologies and frameworks collectively form the backbone of your application, enabling the development of a robust and efficient REST API with Flask and MongoDB integration.

## Setup
Install requirements from a .txt file:

```bash
# setup command
pip3 install -r requirements.txt
```
After installation run:
```bash
python3 main.py
```
Now, you are connected to local MongoDB database. Let's populate it with some exaple data:
```bash
python3 populate.py
```

## Usage

To play with API You can use curl. If You want to get things more visualised i recommend Postman or some online free API testing tool for more readable data:

```bash
#The part module
{
serial_number: "123456"
name: "Resistor 1"
description: "A resistor for testing"
category: "Resistors"
quantity: 10
price: 1.99
location:  {
    room: "A"
    bookcase: "B"
    shelf: "1"
    cuvette: "C"
    column: "2"
    row: "3"}
}
```

```bash
#The category module
{
name: "Electronics"
parent_name: ""
}
```
## Endpoints

### Parts

- **Endpoint_1:**
  - Method: GET
  - Path: `/api/products`

  - **Description:** Retrieve information about all parts.

  - **Example:**
    ```bash
    curl -X GET http://localhost:5000/api/products
    ```

- **Endpoint_2:**
  - Method: GET
  - Path: `/api/products/{serial_number}`

  - **Description:** Retrieve information about a specific part by its serial number.

  - **Example:**
    ```bash
    curl -X GET http://localhost:5000/api/products/ABC123
    ```

- **Endpoint_3:**
  - Method: POST
  - Path: `/api/products`

  - **Description:** Create a new part.

  - **Example_4:**
    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"serial_number": "ABC123", "name": "Sample Part", "category": "Electronics", "quantity": 10, "price": 25.99}' http://localhost:5000/api/products
    ```

- **Endpoint_5:**
  - Method: PUT
  - Path: `/api/products/{serial_number}`

  - **Description:** Update information about a specific part.

  - **Example:**
    ```bash
    curl -X PUT -H "Content-Type: application/json" -d '{"name": "Updated Part Name", "price": 29.99}' http://localhost:5000/api/products/ABC123
    ```

- **Endpoint_6:**
  - Method: DELETE
  - Path: `/api/products/{serial_number}`

  - **Description:** Delete a specific part by its serial number.

  - **Example:**
    ```bash
    curl -X DELETE http://localhost:5000/api/products/ABC123
    ```

### Categories

- **Endpoint_1:**
  - Method: GET
  - Path: `/api/categories`

  - **Description:** Retrieve information about all categories.

  - **Example:**
    ```bash
    curl -X GET http://localhost:5000/api/categories
    ```

- **Endpoint_2:**
  - Method: GET
  - Path: `/api/categories/{name}`

  - **Description:** Retrieve information about a specific category by its name.

  - **Example:**
    ```bash
    curl -X GET http://localhost:5000/api/categories/Electronics
    ```

- **Endpoint_3:**
  - Method: POST
  - Path: `/api/categories`

  - **Description:** Create a new category.

  - **Example:**
    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"name": "Electronics", "parent_name": "Components"}' http://localhost:5000/api/categories
    ```

- **Endpoint_4:**
  - Method: PUT
  - Path: `/api/categories/{name}`

  - **Description:** Update information about a specific category.

  - **Example:**
    ```bash
    curl -X PUT -H "Content-Type: application/json" -d '{"description": "Updated category description"}' http://localhost:5000/api/categories/Electronics
    ```

- **Endpoint_5:**
  - Method: DELETE
  - Path: `/api/categories/{name}`

  - **Description:** Delete a specific category by its name.

  - **Example:**
    ```bash
    curl -X DELETE http://localhost:5000/api/categories/Electronics
    ```

### Searching Parts

- **Endpoint_1:**
  - Method: POST
  - Path: `/api/products/search`

  - **Description:** Search for parts based on a provided search phrase.

  - **Example:**
    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"search_phrase": "ABC"}' http://localhost:5000/api/products/search
    ```
