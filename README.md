# Migración en América Latina (Una visión preliminar)

## Descripción
La presente app consiste en un dashboard o tablero de control que nos permite interactuar con datos migratorios y macroecónomicos para América Latina, disponibles en la revista Expansión y en el repositorio de datos del Banco Mundial.

![Vista general del dashboard](https://github.com/calvarad/p-g1/blob/master/General.gif)
## Objetivos
Identificar con base en las nacionalidades y los indicadores macroeconómicos y sociales de los países de origen la posibilidad de que un individuo representativo decida migrar

Describir y caracterizar a la **población inmigrante de Chile** basados en datos demográficos y sociales. 

Conocer cómo los inmigrantes en Chile se desenvuelven en el aspecto económico, social y cultural.

## Replica
Esta aplicación es de uso libre y gratuito basado en la [licencia MIT](https://github.com/calvarad/p-g1/blob/master/LICENSE.txt).
Si desea replicar este proyecto, favor en su cmd o Anaconda prompt escriba `git clone https://github.com/calvarad/p-g1.git`. 
Después, instale los paquetes necesarios presentes en requierements.txt escribiendo en el cmd o Anaconda prompt `pip install > requirements.txt`
Luego, utilice las bases de datos contenidas [aquí](https://www.dropbox.com/sh/6y8ec7p3cz0uxme/AACoT7PymDcHXj6iHtiTf6fPa?dl=0), le recomendamos que a la hora de descargarlas las extraiga dentro de la carpeta donde tenga clonado el repositorio.

## ¿Cómo se hizo este dashboard?
### Busqueda de datos 

Los datos utilizados para la creación del mapa salieron de un *web scrapping* dentro de la página de cada perfil de país de la revista [Expansión](https://datosmacro.expansion.com/demografia/migracion/inmigracion/chile). El [código](https://github.com/calvarad/p-g1/blob/master/Web_data.py) ingresa a la página web y toma los datos disponibles de cada país disponibles a la fecha. Después los consolida dentro de un archivo csv. 
Debemos aclarar que para efectos de simular un mapa cloropetico, en excel agregamos los códigos iso 3166 (Disponibles en este [enlace](https://github.com/lukes/ISO-3166-Countries-with-Regional-Codes/blob/master/all/all.csv) y disponibles en la carpeta [db](https://www.dropbox.com/sh/6y8ec7p3cz0uxme/AACoT7PymDcHXj6iHtiTf6fPa?dl=0) como "paises.csv") de cada país por medio de la función *vlookup*.

Después los datos utilizados en la creación de las tablas con perfiles de comparación, fueron extraidos del repositorio de indicadores de desarrollo del [Banco mundial](http://databank.worldbank.org/data/source/world-development-indicators#). Se selecionaron la mayoría de países de América Latina.

### Representación de los datos

Luego utilizamos los paquetes plotly y dash (basados en el microframework Flask y en javascript) que nos permitieron:
* Crear gráficos y mapas
* Organizar los perfiles de país
* Crear un entorno interactivo y amigable para el usuario




