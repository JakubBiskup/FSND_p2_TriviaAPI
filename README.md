# Udacitrivia

This project is a full-stack application that allows users to play a trivia game, post new questions as well as delete the ones they don't like. 
This is the second project of Udacity's Full-Stack Developer Nanodegree Program. My job was to develop the API for this application.

## Getting Started

### Basic Requirements

In order to successfully set up the app, you need to have Python3, pip, Nodejs and Node Package Manager already installed on your local machine.

### Installing dependencies for backend

Install dependencies by navigating to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```
### Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```
change the database_path in models.py (line 7) to match your PostgreSQL user and password

### Running the server

To run the server, execute these three lines from within the `/backend` directory:
```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```
### Installing dependencies and running frontend

Open a terminal in `/frontend` directory and run:
```bash
npm install
```
and then run:
```bash
npm start
```
Open http://localhost:3000 to view the frontend in the browser.

#### Running tests

To set up tests, navigate to the `/backend` directory and run:
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
```
next, change the self.database_path in test_flaskr.py (line 18) to match your PostgreSQL user and password.  
Then you can run tests by running from the `/backend` directory:
```bash
python test_flaskr.py
```

## API Reference

### Getting Started
Base URL: At present, this app can only be run locally. The backend is hosted at http://127.0.0.1:5000/

### Error Handling
Errors are returned as JSON objects with "success" set to False, "error" set to the error's number and a "message" describing the error

The API will return four error types when requests fail:
- 400: Bad Request
- 404: Resource Not Found
- 422: Unprocessable 
- 500: Internal Server Error

### Endpoints
#### GET /questions
- General:
    - Returns a list of question objects, success value, total number of questions, categories as a dictionary and a current category
    - Results are paginated in groups of 10. Include a request argument to choose page number
-Sample: `curl http://127.0.0.1:5000/questions`
```
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "current_category": null,
  "questions": [
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    },
    {
      "answer": "Agra",
      "category": 3,
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    }
  ],
  "success": true,
  "total_questions": 24
}
```
#### GET /categories
Returns a success value and a dictionary of categories where id is the key and name is the value
Sample: `curl http://localhost:5000/categories`
```
{
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "success": true
}
```
#### DELETE /questions/<int:question_id>
Deletes a question of a given id from the database and returns success value and id of the deleted question

#### POST /questions
Searches the questions by a given search term or adds a new question.  
If the 'searchTerm' is included in the request body, the function will search the questions by a given term and not post a question.  
The search returns a success value, list of questions matching, number of questions matching and the search term.  
If there is no search term included in the request body, the function will post a new question with given question and answer texts, category and difficulty.  
Posting a question returns success value and added question's id.

#### GET /categories/<int:category_id>/questions
Returns a success value, list of questions in a given category and a current category object

#### POST /quizzes
This is an endpoint to play the trivia game. It returns success value, quiz category object, list of ids of previous questions and a randomly chosen question from that category which is not one of the previous questions.

