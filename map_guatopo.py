import ee
import folium
import geehydro

# Inicio
ee.Initialize()

# Variables iniciales
polygonCollection = 'WCMC/WDPA/current/polygons' # Coleccion
polygonName = 'Guatopo' # Imagen

# Consultando la coleccion y seleccionando la  imagen
polygon = ee.FeatureCollection(polygonCollection) \
            .filter(ee.Filter.eq('NAME', polygonName))

# Mapa
point = [10.5165848,-66.8600685] # Centro del mapa.
Map = folium.Map(location=point, zoom_start=9, control_scale = True)
Map.addLayer(polygon, name=polygonName) # Agregando poligono
Map.setControlVisibility(layerControl=True, fullscreenControl=True, latLngPopup=True) # Layer control

# Guardando html
Map.save('Layer_Guatopo.html')