from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route('/<int:id>')
def pessoa(id):  
  return jsonify({
    'id'    : id, 
    'nome'  : 'Tony Frezza',
    'profissao' : 'Analista de sistemas'
  })

@app.route('/soma/<int:valorA>/<int:valorB>/')
def soma(valorA, valorB):
  return jsonify({'soma':(valorA+valorB)})

@app.route('/somapost',methods=['POST','PUT','GET'])
def somaPost():
  if request.method == 'POST':
    dados = json.loads(request.data)
    total = sum(dados['valores'])   
    
  elif request.method == 'GET':
    total = 10+10
  
  return jsonify({'soma':total})
  


if __name__ == '__main__':
  app.run(debug = True)