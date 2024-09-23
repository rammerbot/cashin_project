from models import session, Movie, Actor, MovieActor, Director
from datetime import datetime
from sqlalchemy import func, extract
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from ml import book_recommendations, course_recommendations, data
from sklearn.metrics.pairwise import cosine_similarity




# Sistema de Recomendacion de libros
def recommender(movie: str):
    title = movie
    recommendations = book_recommendations(title, data)
    return recommendations
   
# Sistema de Recomendacion de cursos
def recommender(movie: str):
    title = movie
    recommendations = book_recommendations(title, data)
    return recommendations
   
