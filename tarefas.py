from flask import Flask, jsonify, request
import json

app = Flask(__name__)

tarefas = [
  {
    'id'  : 1,
    'responsavel' : 'John Smith',
    'tarefa'  : 'criar tela de login',
    'status' : 'pendente'
  },
  {
    'id'  : 2,
    'responsavel' : 'Marc Doe',
    'tarefa'  : 'Desenvolver método GET',
    'status' : 'concluido'
  },
]

@app.route('/')
def main():
  return 'tarefas'

@app.route('/list',methods=['POST','GET'])
def listTasks():
  
  if request.method == 'POST':
    
    try:
      response = {
        'status'  : 'success',
        'tarefa'  : tarefas[int(request.form['id'])-1]
      }
    except Exception:
      response = {
        'status'  : 'error',
        'message' : 'Tarefa não encontrada'
      }
  else:
    response = tarefas
  
  return jsonify(response)


if __name__ == '__main__':
  app.run(debug=True)