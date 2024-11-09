import folium, json
m = folium.Map(location=[47.3, 7.61], zoom_start=10)

infoHtmlText = """<table style="width:100%">
  <tr>
    <th>Company</th>
    <th>Contact</th>
    <th>Country</th>
  </tr>
  <tr>
    <td>Alfreds Futterkiste</td>
    <td>Maria Anders</td>
    <td>Germany</td>
  </tr>
  <tr>
    <td>Centro comercial Moctezuma</td>
    <td>Francisco Chang</td>
    <td>Mexico</td>
  </tr>
</table>"""

folium.Marker(
    location=[47.40875, 8.50778],
    popup=infoHtmlText,
    icon=folium.Icon(color="red", icon="info-sign"),
).add_to(m)


rfile = open('Data/Gemeinden_SolothurnWGS84.json', 'r', encoding='utf-8').read() 
jsonData = json.loads(rfile)        
style_function = {
                 'fillColor': 'white',
                }
folium.GeoJson(jsonData, name='json_data',#,
               #style_function=lambda x: style_function

              ).add_to(m)

m