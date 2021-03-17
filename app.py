from flask import Flask, jsonify, request
import overpass
api = overpass.API()

app = Flask(__name__)
def settings():
    return 'settings'


@app.route("/api")
def api_root():
    return jsonify({"restos": "http://127.0.0.1:5000/api/restos/"})

magasins = []

@app.route('/api/restos/<ville>', methods=["GET"])
def magasin(ville):
    if request.method == 'GET':
        response = api.get (f"""area[name="{ville}"]; node["amenity"=restaurant](area);""")
        return response 