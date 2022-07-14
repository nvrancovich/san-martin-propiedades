# san_martin_propiedades_geodatos

Este repositorio esta destinado a al extracción, análisis exploratorio y predicción de los valores de las propiedades en venta ubicadas en el partido de General San Martín, Provincia de Buenos Aires, Argentina.

## Roadmap

### I - Preparación y adquisición de los datos
- Preparacion y definicion de etapas del proyecto.
- Armado del script para extraer los links de cada propiedad individual.
- Armado del script para extraer los features de cada propiedad individual (precio, m2, baños, dormitorios, antigûedad, coordenadas geográficas).
- Armado del archivo .geojson con los poligonos de cada uno de los segmentos en los que se divide el partido de San Martín. Utilizando google mymaps para generar un archivo .kml y mygeodata para convertirlo en un .geojson.
- Armado del script para cruzar la tabla con las features y la tabla con los poligonos de las segmentaciones y tener en una sola tabla el segmento (categoría) según las coordenadas de cada propiedad.

### II - Análisis exploratorio de los datos y relato

- Análsis exploratorio de las features obtenidas con una muestra del 10% de las propiedades.
- Graficos de las metricas más interesantes.

### III - Modelo de machine learning y deploy

- Definición y armado de un modelo de Machine Learning.
