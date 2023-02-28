from flask import Flask,request
from scraping import consulta,get_bd
from bson.json_util import dumps

app = Flask(__name__)

@app.route("/")
def lista_imcompletas():
    basedatos=get_bd()
    lista = basedatos.list_collection_names()
    # si existe la colección llamamos a la función con el parámetro primera en False para que haga el match
    if "flanks" in lista:
        datos=consulta(False)
    else:
        # si es la primera vez sacamos los datos de la web
        colec = basedatos.flanks
        datos=consulta(True)
        for sicav in datos:
            colec.insert_one(sicav)
            
    data_json = dumps(datos, indent=3,ensure_ascii=False)
    return data_json


@app.route("/info",methods=["GET"])
def buscar():
    basedatos=get_bd()
    isin = request.values.get("isin")
    encontradas = basedatos.flanks.find_one({"isin":{"$eq":isin}})
    data_json = dumps(encontradas, indent=3,ensure_ascii=False)

    return data_json

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=5000)
