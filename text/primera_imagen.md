#### Primera imágen con GEE
**Autor:** Javier Martínez


En el presente ejemplo se cargará la imagen *srtm90_v4* para validar la inatalación y funcionamiento 
de *Google Earth Engine*. Por lo que;

1. Se importa el módulo gee.
2. Se da inicio de la API.
3. Se descarga la imagen.
4. Print de los resultados alcanzados.


```python
# Módulo
import ee

# Iniciando API
ee.Initialize()

# Cargando Imagen
image = ee.Image('srtm90_v4')

# Print resultados
print(image.getInfo())
```

    {'type': 'Image', 'bands': [{'id': 'elevation', 'data_type': {'type': 'PixelType', 'precision': 'int', 'min': -32768, 'max': 32767}, 'dimensions': [432000, 144000], 'crs': 'EPSG:4326', 'crs_transform': [0.000833333333333, 0, -180, 0, -0.000833333333333, 60]}], 'version': 1494271934303000.0, 'id': 'srtm90_v4', 'properties': {'system:time_start': 950227200000, 'system:time_end': 951177600000, 'system:asset_size': 18827626666}}

