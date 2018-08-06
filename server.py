from flask import Flask, render_template ,request, redirect
from mysqlconnection import connectToMySQL

app=Flask(__name__)

mysql = connectToMySQL('LeadsAndClients')

@app.route('/')
def index():
    languages = mysql.query_db("SELECT * FROM languages;")
    return render_template('index.html', languages = languages)

# @app.route('/change', methods=['POST'])
# def create():
#     query = "INSERT INTO languages (first_name, last_name, occupation, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(occupation)s, NOW(), NOW());"
#     data = {
#              'first_name': request.form['first'],
#              'last_name':  request.form['last'],
#              'occupation': request.form['occupation']
#            }
  
#     new_friend_id = mysql.query_db(query, data)

#     return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
