from flask import Flask

app = Flask(__name__)

@app.route("/<numero>",methods=['POST','GET'])

def ola(numero):
    return 'Olá mundão: {}'.format(numero)
  
if __name__ == "__main__":
  app.run(debug=True)