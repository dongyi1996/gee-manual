### Manual para la instalación y uso de Google Earth Engine (GEE)
GEE es un catálogo multi-petabyte de imágenes satelitales y data geoespacial que permite a investigadores, científicos y desarrolladores detectar cambios, mapear tendencias y cuantificar diferencias de la Tierra. Para mayor información se puede consultar a [Google Earth Engine](https://earthengine.google.com/).

#### Conexión a Google Earth Engine (GEE)
Inicialmente, es necesario crear una cuenta en [Google Earth Engine API](https://signup.earthengine.google.com/#!/), para posteriormente realizar la conexión entre Python y la API. Con este fin se usará la terminal y la siguientes lineas de comandos:

> pip install earthengine-api

> pip install earthengine-api --upgrade

Vale resaltar que en Python se importará el módulo de la manera siguiente:

> import ee

Finalizada la instalación se procede a autenticar con los servidores de Earth Engine;

> ee.Authenticate()

Donde se hará la verificación de la cuenta via Web browser y se asignará un *verification code* que debe ser copiado en la terminal (ver *authenticate.py*) y seguidamente, al presionar *Enter*, se guardará el token de autorización (*authorization token*).

Es importante destacar que para iniciar la API se debe utilizar;

> ee.Initialize()

Con el propósito de validar las instalaciones es recomendable realizar el ejemplo *catalogue/initialize.py* el cual permitirá iniciar la API y consultar la imagen *srtm90_v4*. 

Para mayor información consultar la documentación oficial [Developers guides](https://developers.google.com/earth-engine/guides/python_install).

#### Obtener Imágenes
Con GEE es posible aceder a una colección de imagenes (o a una imagen) según el catálogo de productos disponibles en [Earth Engine Data Catalog](https://developers.google.com/earth-engine/datasets/).

Para los siguientes ejemplos se ha seleccionado al Parque Nacional Guatopo. En *catalogue/map_guatopo.py* se consulta la colección de imágenes *WCMC/WDPA/current/polygons*, seleccionando la imágen *Guatopo*;

> import ee
import folium
import geehydro

> ee.Initialize()

> polygonCollection = 'WCMC/WDPA/current/polygons'
polygonName = 'Guatopo'
polygon = ee.FeatureCollection(polygonCollection) \
            .filter(ee.Filter.eq('NAME', polygonName))


 Una vez tomada la imagén se procede a crear un mapa con la ayuda de *folium*. Para esto se ha seleccionado la localización $10°30'59.7"N 66°51'36.3"W$ para el inicio del mapa con un zoom de 9. Igualmente, se incorpora el control de escala y el control de layers. 
 
 > point = [10.5165848,-66.8600685]
Map = folium.Map(location=point, zoom_start=9, control_scale = True)
Map.addLayer(polygon, name=polygonName)
Map.setControlVisibility(layerControl=True, fullscreenControl=True, latLngPopup=True)

 Finalmente, se guarda el mapa creado en formato *.HTML* en la dirección 
 *catalogue/map_html/Layer_Guatopo.html*.

 > Map.save('catalogue/map_html/Layer_Guatopo.html')

