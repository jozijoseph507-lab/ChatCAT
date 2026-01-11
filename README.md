# ChatCAT 🐱

**ChatCAT** is an interactive cat-themed chat API built with **Python** and **FastAPI**.  
It allows users to send messages and receive fun, random cat-style responses. This project demonstrates backend development concepts, RESTful APIs, JSON handling, and interactive programming logic — perfect for learning or teaching API workflows.

---

## Features

- RESTful API built with **FastAPI** and served with **Uvicorn**
- Randomized cat responses for user messages
- Input validation using **Pydantic**
- Lightweight and easy to extend for new endpoints
- Ideal for learning backend development and API design

---

## Getting Started

### Prerequisites

- Python 3.11+
- pip (Python package manager)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/jozijoseph507-lab/ChatCAT.git
cd ChatCAT
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the server:

bash
Copy code
python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload
Open your browser and visit:

cpp
Copy code
http://127.0.0.1:8000/
API Endpoints
GET /
Returns a welcome message:

json
Copy code
{
  "message": "Welcome to ChatCAT! Use POST /chat to talk to the cat."
}
POST /chat
Send a JSON message and get a random cat response.

Request:

json
Copy code
{
  "message": "Hello ChatCAT"
}
Response:

json
Copy code
{
  "user_message": "Hello ChatCAT",
  "cat_response": "Meow! 🐱"
}
Technologies Used
Python 3.11

FastAPI

Uvicorn

Pydantic

Project Highlights
Designed and implemented an interactive API to demonstrate backend concepts and RESTful workflows

Useful for learning or teaching programming, APIs, and JSON-based data exchange

Fully extensible for additional chat logic, endpoints, or frontend integration

License
This project is open-source. Feel free to use, modify, and share!
