import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
# from bson import ObjectId


from datetime import datetime

datos = []

def get_bd():
    client = MongoClient(
        host='host_mongo',
        port=27017,
        username='root',
        password='pass',
        authSource='admin'
    )
    basedatos = client.data_flanks
    return basedatos

def consulta(primera):
    # son 42 paginas
    paginador = [1,2]
    url = 'https://www.cnmv.es/Portal/Consultas/MostrarListados.aspx?id=18&page='
    # para cada pagina
    # for i in range(paginador):
    for i in paginador:
        try:
            # hacemos la primera  petición a la url de las CMNV
            print("url pet -> " + url+str(i))
            response = requests.get(url+str(i))

            # creamos la sopa y parseamos el contenido
            html = BeautifulSoup(response.content, "html.parser")
            # comprobamos que existen sicavs
            if(html.find("li", class_='blocks-single')):
                nodes = html.find_all("li", class_='blocks-single')
                # analizamos cada nodo y extraemos la info
                for node in nodes:
                    url_sicav = node.find("a")['href']
                    reg = extraccion(url_sicav, node)
                    datos.append(reg)

                print("\n FIN DE LOS DATOS\n")
            else:
                break
        except requests.exceptions.HTTPError as e:
            print("\nERROR EN PETICION => " + url)
    # FIN RECORRER NODOS

    if(primera == True):
        # cuando la bd no existia
        return datos
    else:
        # cuando la bd ya existia
        basedatos=get_bd()
        collec = basedatos.flanks

        for dato in datos:
            # hacemos la comprobación de los registros en la bd
            if collec.find_one({"numero de registro": {"$eq": dato['numero de registro']}}):
                registro = collec.find_one({"numero de registro": {"$eq": dato['numero de registro']}})

                """Dejo comnentada esta parte, porque no logre comprobar si funcionaba,
                la idea es comparar si los datos de array datos es diferente al mismo documento que proviene de la bd,
                en tal caso se comprueba si el campo que queeremos añadir ya existe, si es asi, se debe hacer un
                replace_one, si no un update_one al documento"""

                # hoy =  datetime.now()
                # # CAMBIOS EN FECHA DE FOLLETO
                # if registro['fecha ultimo folleto'] != dato['fecha ultimo folleto']:
                #     registro.update({"historial": {"$set": {"fecha anterior folleto": {
                #                     "$set": registro['fecha ultimo folleto']}}}})
                #     # guardamos la fecha del cambio
                #     registro.update(
                #         {"historial": {"$set": {"fecha de cambio de folleto": {"$set": hoy}}}})
                #     # una vez actualizado cambiamos el valor de la fecha antigua por la acual (del html)
                #     registro.update(
                #         {"fecha ultimo folleto": {"$set": dato['fecha ultimo folleto']}})

                # # CAMBIOS EN DOMICILIO
                # if registro['domicilio'] != dato['domicilio']:
                #     registro.update(
                #         {"historial": {"$set": {"domicilio anterior": {"$set": registro['domicilio']}}}})
                #     registro.update(
                #         {"historial": {"$set": {"fecha de cambio de domicilio": {"$set": hoy}}}})
                #     registro.update({"domicilio": {"$set": dato['domicilio']}})

                # # CAMBIOS EN CAPITALES INICIALES
                # if registro['capital inicial'] != dato['capital inicial']:
                #     registro.update({"historial": {"$set": {"capital inicial anterior": {
                #                     "$set": registro['capital inicial']}}}})
                #     registro.update({"historial": {
                #                     "$set": {"fecha de cambio de capital inicial": {"$set": hoy}}}})
                #     registro.update(
                #         {"capital inicial": {"$set": dato['capital inicial']}})

                # # CAMBIOS EN CAPITALES MAXIMO
                # if registro['capital maximo estatuario'] != dato['capital maximo estatuario']:
                #     registro.update({"historial": {"$set": {"capital maximo estatuario anterior": {
                #                     "$set": registro['capital maximo estatuario']}}}})
                #     registro.update({"historial": {"$set": {
                #                     "fecha de cambio de capital maximo estatuario": {"$set": hoy}}}})
                #     registro.update({"capital maximo estatuario": {
                #                     "$set": dato['capital maximo estatuario']}})
            else:
                # si no encuentra el documento lo añade a la bd
                collec.insert_one(dato)
        
        # Al finalizar el bucle volvemos a leer la bd para devolver los datos actualizados
        basedatos=get_bd()
        collec = basedatos.flanks
        return collec.find({})

def extraccion(url, node):
    url = 'https://www.cnmv.es/Portal/Consultas/'+url
    print("     url sicav -> " + url)
    nif_sicav = url.split('=')[1]
    nombre = node.find("span", class_="tit-small").text.strip()
    fecha = node.find("li", class_="resumen").text.split("-")[1].strip()
    n_registro = node.find("li", class_="resumen").text.split("-")[0].strip().split(":")[1].strip()
    domicilio = node.find_all("li", class_="resumen")[-1].text.strip()

    try:
        # extraemos los datos de la web
        response = requests.get(url)
        if response.content:
            # creamos la sopa y parseamos el contenido
            html = BeautifulSoup(response.content, "html.parser")

            table = html.find("table", id='ctl00_ContentPrincipal_gridDatos')
            cap_inicial = table.find_all("td", class_="Derecha")[0].text.strip()

            cap_max = table.find_all("td", class_="Derecha")[-1].text.strip()

            isin = table.find("a").text.strip()

            f_folleto = table.find(
                attrs={'data-th': 'Fecha último folleto'}).text.strip()

            # elemeto sicav
            sicav_elem = {
                "nif": nif_sicav,
                "nombre": nombre,
                "fecha registro oficial": fecha,
                "numero de registro": n_registro,
                "domicilio": domicilio,
                "capital inicial": cap_inicial,
                "capital maximo estatuario": cap_max,
                "isin": isin,
                "fecha ultimo folleto": f_folleto,
                "url": url,
                "historial": {}
            }
            return sicav_elem

    except requests.exceptions.HTTPError as e:
        print("\nLa url no existe => " + url)
    except requests.exceptions.ConnectionError:
        print("\nEl servidor no funciona o el dominio es incorrecto => " + url)
    except requests.exceptions.RequestException as e:
        print("\nHa ocurrido un error => " + e)
    else:
        print("\nError no localizado, consulte con su administrador")