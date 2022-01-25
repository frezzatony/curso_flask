from flask import request
from flask_restful import Resource

listaHabilidades = [
  {
    'id'  :  1,
    'descricao' : 'Python'
  }

]

class Habilidades(Resource):
  def get(self):
    return listaHabilidades
  
  def put(self):
    listaHabilidades.append({
      'id'  :   len(listaHabilidades)+1,
      'descricao'  :  request.form['descricao']
    })
    return listaHabilidades
  
  def post(self):
    try:
      key = int(request.form['id'])-1
      listaHabilidades[key]['descricao']= request.form['descricao']
      response = listaHabilidades
    except Exception:
      response = {
        'error'  :  True,
        'message'  :  'Id informada não encontrada',
      }
    
    return response
      
  
  def delete(self):
    
    try:
      listaHabilidades.pop(int(request.form['id'])-1)
      response = listaHabilidades
    except Exception:
      response = {
        'error'  :  True,
        'message'  :  'Id informada não encontrada'
      }
      
    return response
    