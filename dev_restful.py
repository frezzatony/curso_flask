from flask import Flask, request
from flask_restful import Resource, Api
import json
from habilidades import Habilidades

app = Flask(__name__)
api = Api(app)


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

class Desenvolvedor(Resource):
  
  def get(self,id):
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
    return response
  
  def put(self,id):
    dados = json.loads(request.data)
    desenvolvedores[id] = dados
    return dados

  def delete(self,id):
    desenvolvedores.pop(id)
    return {
      'status'  : 'sucesso',
      'message'  : 'Dev removido'
    }
  
class ListaDevs(Resource):
   
  def get(self):
    return desenvolvedores

api.add_resource(ListaDevs,'/')
api.add_resource(Desenvolvedor,'/dev/<int:id>')
api.add_resource(Habilidades,'/habilidades')


if __name__ == '__main__':
  app.run(debug=True,port=3000)
