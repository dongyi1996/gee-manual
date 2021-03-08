### Manual para la instalación y uso de Google Earth Engine (GEE)
GEE es un catalogo multi-petabyte de imágenes satelitales y data geoespacial que permite a investigadores, científicos y desarrolladores detectar cambios, mapear tendencias y cuantificar diferencias de la Tierra. Para mayor información se puede consultar a [Google Earth Engine](https://earthengine.google.com/).

#### Conexión a Google Earth Engine (GEE)
Inicialmente, es necesario crear una cuenta en [Google Earth Engine API](https://signup.earthengine.google.com/#!/), para posteriormente realizar la conexión entre Python y la API. Con este fin usaremos la terminal y la siguientes lineas de comandos:

> pip install earthengine-api

> pip install earthengine-api --upgrade

Vale resaltar que en Python se importará el módulo de la manera siguiente:

> import ee

Finalizada la instalación se procede a autenticar con los servidores de Earth Engine;

> ee.Authenticate()

Donde se hará la verificación de la cuenta via Web browser y se asignará un *verification code* que debe ser copiado en la terminal (ver *authenticate.py*) y seguidamente, al presionar *Enter*, se guardará el token de autorización (*authorization token*).

Es importante destacar que para inicial la API se debe utilizar;

> ee.Initialize()

Con el propósito de validar las instalaciones es recomendable realizar el ejemplo *initialize.py* el cual permitirá iniciar la API y consultar la imagen *srtm90_v4*. 

Para mayor información consultar la documentación oficial [Developers guides](https://developers.google.com/earth-engine/guides/python_install).

### Obtener Imágenes
Con GEE es posible aceder a una colección de imagenes (o a una imagen) según el catalogo de productos disponibles en [Earth Engine Data Catalog](https://developers.google.com/earth-engine/datasets/).

