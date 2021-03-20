### Manual para la instalación y uso de Google Earth Engine (GEE)
**Autor:** Javier Martínez

**Tutor:** Isabel LLatas

GEE es un catálogo multi-petabyte de imágenes satelitales y data geo-espacial que permite a investigadores, científicos y desarrolladores detectar cambios, mapear tendencias y cuantificar diferencias de la Tierra. Para mayor información consultar a [Google Earth Engine](https://earthengine.google.com/).

#### Conexión a Google Earth Engine (GEE)

Inicialmente, es necesario crear una cuenta en [Google Earth Engine API](https://signup.earthengine.google.com/#!/). Para realizar la conexión entre Python y la API se debe installar el siguiente paquete;

> pip install earthengine-api

> pip install earthengine-api --upgrade

En Python se importará el módulo como;

> import ee

Finalizada la instalación se procede a autenticar con los servidores de Earth Engine;

> ee.Authenticate()

En este caso se hará la verificación de la cuenta via web browser y se asignará un *verification code* que debe ser copiado en la terminal y seguidamente, al presionar *Enter*, se guardará el token de autorización (*authorization token*). Es importante destacar que para iniciar la API se debe utilizar *Initialize* y no es necesario volver a autenticar con  *Authenticate*;

> ee.Initialize()

Para validar la instalación se recomienda seguir el ejemplo [Primera imágen con GEE](notebook/primera_imagen.ipynb). 

Para mayor información consultar la documentación oficial [Developers guides](https://developers.google.com/earth-engine/guides/python_install).

#### Ejemplos Prácticos

1. [Primera imágen con GEE](notebook/primera_imagen.ipynb).
2. [El Parque Nacional Guatopo](notebook/map_guatopo.ipynb). 
3. [Series de Tiempo (EVI y NDVI)](notebook/time_serie.ipynb). 
