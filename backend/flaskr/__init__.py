import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def paginate_questions(request, selection):
  page=request.args.get('page',1,type=int)
  
  start=(page-1)*QUESTIONS_PER_PAGE
  end=start + QUESTIONS_PER_PAGE

  current_questions=[question.format() for question in selection[start:end]]

  return current_questions





def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  
  '''
  @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
  '''
  cors=CORS(app)  

  '''
  @TODO: Use the after_request decorator to set Access-Control-Allow
  '''
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Origin','*')
    response.headers.add('Access-Control-Allow-Methods','GET,POST,DELETE,OPTIONS')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    return response

  '''
  @TODO: 
  Create an endpoint to handle GET requests 
  for all available categories.
  '''
  
  #route handler to get categories
  @app.route('/categories')
  def get_categories():
    categories=Category.query.all()
    formatted_categories=[category.format() for category in categories]
    categories_dict={}
    for category in formatted_categories:
      categories_dict[category['id']]=category['type']
    return jsonify({'success':True, 'categories':categories_dict}), 200


  '''
  @TODO: 
  Create an endpoint to handle GET requests for questions, 
  including pagination (every 10 questions). 
  This endpoint should return a list of questions, 
  number of total questions, current category, categories. 

  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions. 
  '''
  @app.route('/questions')
  def display_questions():
    categories=Category.query.all()
    formatted_categories=[category.format() for category in categories]
    categories_dict={}
    for category in formatted_categories:
      categories_dict[category['id']]=category['type']
    selection=Question.query.all()
    current_questions=paginate_questions(request,selection)

    total_questions=len(selection)

    current_category=Category.query.first().format()  ##############################################change this line later##################################################################################



    


    return jsonify({'success':True, 'categories':categories_dict, 'questions':current_questions, 'total_questions':total_questions, 'current_category':current_category}), 200

    
  '''
  @TODO: 
  Create an endpoint to DELETE question using a question ID. 

  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page. 
  '''
  @app.route('/questions/<int:question_id>', methods=['DELETE'])
  def delete_question(question_id):
    Question.query.filter_by(id=question_id).one_or_none().delete()

    return jsonify({'success':True, 'deleted_question_id':question_id}), 200

  '''
  @TODO: 
  Create an endpoint to POST a new question, 
  which will require the question and answer text, 
  category, and difficulty score.

  TEST: When you submit a question on the "Add" tab, 
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.  
  '''

  @app.route('/questions', methods=['POST'])
  def add_question():
    question=request.json['question']
    answer=request.json['answer']
    category=request.json['category']
    difficulty=request.json['difficulty']
    new_question=Question(question,answer,category,difficulty)
    new_question.insert()
    return jsonify({'success':True}),200
    

  '''
  @TODO: 
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question. 

  TEST: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 
  '''

  '''
  @TODO: 
  Create a GET endpoint to get questions based on category. 

  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''


  '''
  @TODO: 
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''

  '''
  @TODO: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''
  
  return app

    