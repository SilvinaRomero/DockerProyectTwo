from flask import Flask,render_template,request,redirect
# from bson import ObjectId
from pymongo import MongoClient
from scraping import consulta,get_bd

app = Flask(__name__)

# títulos y cabeceras de las plantillas
titulo = "Prueba Flanks"
cabecera = "Registro completo de SICAVS"


@app.route("/")
def lista_imcompletas():
    basedatos=get_bd()
    if request.values.get("volver"):
        # si volvemos de la ruta info solo enviamos los datos leidos de la bd
        colec = basedatos.flanks.find({})
        mensaje = "Información extraida desde la base de datos"
        return render_template('index.html',lista=colec,t=titulo,h=cabecera,mensaje=mensaje)
    else:
        lista = basedatos.list_collection_names()
        # si existe la colección llamamos a la función con el parámetro primera en False para que haga el match
        if "flanks" in lista:
            mensaje="La base de datos ya existia, comparamos los datos entre la base de datos y los datos de la web"
            datos=consulta(False)
        else:
            # si es la primera vez sacamos los datos de la web
            colec = basedatos.flanks
            datos=consulta(True)
            for sicav in datos:
                colec.insert_one(sicav)
            mensaje="La base de datos no existía, rellenamos base de datos desde la web"

        return render_template('index.html',lista=datos,t=titulo,h=cabecera,mensaje=mensaje)


@app.route("/info",methods=["GET"])
def buscar():
    basedatos=get_bd()
    isin = request.values.get("isin")
    encontradas = basedatos.flanks.find_one({"isin":{"$eq":isin}})
    return render_template("buscar.html",lista=encontradas,t=titulo,h=cabecera)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=5000)
