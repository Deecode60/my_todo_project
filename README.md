# Django Todo API

This is a simple REST API built with Django and Django REST Framework that allows users to manage their to-do lists. The API supports creating, reading, updating, and deleting to-do items.

## Project Description

The API allows users to:
- Create a new to-do item
- View a list of all to-do items
- View a specific to-do item by ID
- Update a to-do item (partially or fully)
- Delete a to-do item

## Setup Instructions 

1. Clone the Repository
Clone the project to your local machine:

Copy code:
git clone https://github.com/Deecode60/my_todo_project.git.

cd my_todo_project

2. Set Up a Virtual Environment 
Create and activate a virtual environment:

bash
Copy code
python -m venv venv  # Create a virtual environment

3. Install Dependencies
Install the required dependencies:

pip install -r requirements.txt


4. Run Migrations
Apply the database migrations:
python manage.py migrate


6. Start the Development Server
Run the development server:

python manage.py runserver
The API will be available at http://127.0.0.1:8000.


##  API Endpoints

1. **GET /todos**
Retrieve all the to-do items. You can also search for to-do items by their title using the `search` query parameter.

**Request Example:**
GET /todos?search=homework

**Response Example:**
  {
    "id": "unique_ID",
    "title": "homework",
    "description": "Complete math and science homework",
    "completed": false,
    "created_at": "2025-01-08T10:00:00Z"
  }

 
**2. GET /todos/:id**
 
Retrieve a specific to-do item by its ID.

Request Example:

GET /todos/unique_ID

Response Example:

{
  "id": "unique_ID",
  "title": "homework",
  "description": "Complete math and science homework",
  "completed": false,
  "created_at": "2025-01-08T10:00:00Z"
}


**3. POST /todos**
Create a new to-do item.

Request Example:

POST /todos

{
  "title": "homework",
  "description": "Complete math and science homework",
  "completed": false  
}
 # completed will be False by default
Response Example:

{
  "id": "unique_ID",
  "title": "homework",
  "description": "Complete math and science homework",
  "completed": false,
  "created_at": "2025-01-08T12:00:00Z"
}


**4. PUT /todos/:id**

Update a specific to-do item. This will replace the entire to-do item.

Request Example:

PUT /todos/unique_ID
{
  "title": " homework",
  "description": "Complete math, science, and history homework",
  "completed": true
}

Response Example:

{
  "id": "unique_ID",
  "title": "homework",
  "description": "Complete math, science, and history homework",
  "completed": true,
  "created_at": "2025-01-08T10:00:00Z"
}


**5. PATCH /todos/:id**

Partially update a to-do item (e.g., update only the completed status).

Request Example:

PATCH /todos/unique_ID
{
  "completed": true
}

Response Example:
{
  "id": "unique_ID",
  "title": "homework",
  "description": "Complete math and science homework",
  "completed": true,
  "created_at": "2025-01-08T10:00:00Z"
}

**6. DELETE /todos/:id**
Delete a specific to-do item by its ID.

Request Example:

DELETE /todos/unique_ID
Response Example:

"message": "Todo has been deleted."
