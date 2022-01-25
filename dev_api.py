from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
  {
      'id'  : 0,
      'nome' : 'Tony Frezza',
      'habilidades' : ['Python','Flask','PHP']
  },
  {
    'id'  : 1,
    'nome'  : 'Aldrin Fernandes',
    'habilidades' : ['Python','Django']
  }
  
]

@app.route('/dev/<int:id>',methods=['GET','PUT','DELETE'])
def desenvolvimento(id):
  
  if request.method == 'GET':
    
    try:
      response = desenvolvedores[id]
    except IndexError:
      response = {
        'status'  : 'erro',
        'message'  : 'Dev de ID:{} não encontrado.'.format(id)
      }
    except Exception:
      response = {
          'status' : 'erro',
          'message'  : 'Erro desconhecido. Contate o admin da API'
      }

      
  elif request.method == 'PUT':
    
    dados = json.loads(request.data)
    desenvolvedores[id] = dados
    response =  jsonify(dados)
    
  elif request.method == 'DELETE':
    desenvolvedores.pop(id)
    response =  {
      'status'  : 'sucesso',
      'message'  : 'Dev removido'
    }
  
      
  return jsonify(response)


@app.route('/dev',methods=['POST','GET'])
def listaDevs():
  if request.method == 'POST':
    dados = json.loads(request.data)
    desenvolvedores.append(dados)
    response = {
      'status'  : 'success',
      'message' : 'Dev inserido',
      'id'  :  len(desenvolvedores),
    }
  elif request.method == 'GET':
    response = desenvolvedores
    
  return jsonify(response)
  
  
if __name__ == '__main__':
  app.run(debug=True)
