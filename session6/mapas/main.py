import os
from functools import wraps
from flask import Flask, jsonify, request, render_template
import folium #pip install folium



app = Flask(__name__)


@app.route('/')
def index():
    return render_template('output.html')

@app.route('/map')
def map():
    mapObj = folium.Map(location=[4.642351, -74.054290],zoom_start=15, width=800, height=500)
    # add a marker to the map object
    folium.Marker([4.642351,-74.054290],
                  popup="<i>Estamos en clase con el profe Andrey</i>").add_to(mapObj)
    # render the map object
    mapObj.get_root().render()
    # derive the script and style tags to be rendered in HTML head
    m_header = mapObj.get_root().header.render()
    # derive the div container to be rendered in the HTML body
    m_body_html = mapObj.get_root().html.render()
    # derive the JavaScript to be rendered in the HTML body
    m_script = mapObj.get_root().script.render()
    return render_template('map.html', header=m_header,body_html=m_body_html,script=m_script)



"""
MAIN ...........................................................................
"""
if __name__ == '__main__':
    #app.run()
    app.run(debug=True, port=os.getenv("PORT", default=5000 )) 
    #help coordinates: https://www.latlong.net/convert-address-to-lat-long.html