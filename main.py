import csv
from flask import Flask, jsonify, request
all_movies= []
with open("movies.csv",encoding="UTF8") as f:
    reader= csv.reader(f)
    data= list(reader)
    all_movies= data[1:]

like_movies=[]
dislike_movies=[]
not_watched=[]

app= Flask(__name__)
@app.route("/get-movie")
def get_movie():
    return jsonify({
        "data": all_movies[0],
        "status": "success",
    })

@app.route("/like-movies",methods=["POST"])
def like_movies():
    movie= all_movies[0]
    like_movies.append(movie)
    all_movies.pop(0)
    return jsonify({
        "data": like_movies,
        "status": "success"
    }), 201

@app.route("/dislike-movies", methods=["POST"])
def dislike_movies():
    movie= all_movies[0]
    all_movies= all_movies[1:]
    dislike_movies.append(movie)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/not-watched", methods=["POST"])
def not_watched():
    movie= all_movies[0]
    all_movies= all_movies[1:]
    not_watched.append(movie)
    return jsonify({
        "status": "success"
    }), 201

@app.rount("/populat-movies")
def populat_movies():
    movie_data=[]
    for movie in output:
        _d= {
            "title": movie[0],
            "poster_link": movie[1],
            "release_date":movie[2] or "N/A",
            "duration": movie[3],
            "rating": movie[4], 
            "overview": movie[5]
        }
        movie_date.append(_d)
    return jsonify({
        "data": movie_data,
        
        "status": "success"
    }), 201

if __name__=="__main__":
    app.run()
