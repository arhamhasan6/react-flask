
from flask import Flask, jsonify , request , json
import sqlite3
import json

app=Flask(__name__,template_folder='templates')

def get_db_connectiong():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    print(conn)
    return conn

def get_db_conectionp(content):
    connection = sqlite3.connect('database.db')
    cur = connection.cursor()
    cur.execute(f"INSERT INTO todo ( content) VALUES  ('{str(content)}')" )
    connection.commit()
    connection.close()


# def todo_serializer():
#     conn = get_db_connectiong()
#     posts = conn.execute('SELECT  FROM todo').fetchall()
#     conn.close()

#     print(posts)
    
#     return{
#         columns
#     }


@app.route('/api',methods=['GET'])
def index():
    # conn = get_db_connectiong()
    # posts = conn.execute('SELECT * FROM todo').fetchall()
    # conn.close()
    # for i in posts:
    #     print(i)
   connection_obj = sqlite3.connect('database.db')
  
# cursor object
   cursor_obj = connection_obj.cursor()
  
# to select all column we will use
   statement = '''SELECT * FROM todo'''
  
   cursor_obj.execute(statement)
  
   print("All the data")
   output = cursor_obj.fetchall()
   # for row in output:
   #   print(row)
   columns=['id','created','content']
   results=[]
   for row in output:
      results.append(dict(zip(columns, row)))
   print(results)
  
   connection_obj.commit()
  
# Close the connection
   connection_obj.close()
   
   return jsonify(results)

@app.route('/api/create',methods=['POST'])
def create():
   request_data= json.loads(request.data)
   content = request_data['content']
   get_db_conectionp(content)

   print(request_data)
   return{'201': 'todo created successfully'}


@app.route('/api/<int:id>')
def show(id):
   connection_obj = sqlite3.connect('database.db')
  
# cursor object
   cursor_obj = connection_obj.cursor()
  
# to select all column we will us
   statement = f'SELECT * FROM todo WHERE id={id}'
  
   cursor_obj.execute(statement)
  
   print("All the data")
   output = cursor_obj.fetchall()
   # for row in output:
   #   print(row)
   columns=['id','created','content']
   results=[]
   for row in output:
      results.append(dict(zip(columns, row)))
   print(results)
  
   connection_obj.commit()
  
# Close the connection
   connection_obj.close()
   
   return jsonify(results)





@app.route('/api/<int:id>',methods=['POST'])
def delete(id):
      request_data= json.loads(request.data)
      Id= request_data['id']

      connection_obj = sqlite3.connect('database.db')

      # cursor object
      cursor_obj = connection_obj.cursor()

      # to select all column we will us
      statement = f'DELETE * FROM todo WHERE id={id}'

      cursor_obj.execute(statement)

      print("All the data")
      output = cursor_obj.fetchall()
      # for row in output:
      #   print(row)
      columns=['id','created','content']
      results=[]
      for row in output:
         results.append(dict(zip(columns, row)))
      print(results)

      connection_obj.commit()

      # Close the connection
      connection_obj.close()

      return{'204': 'todo deleted successfully'}





if __name__=='__main__':
    app.run(debug=True)