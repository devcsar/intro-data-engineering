# Datasets del curso

## Hilo conductor: NYC TLC Yellow Taxi

Se usa el mismo dataset en las 10 sesiones. Así los alumnos no reaprenden el dominio en cada clase, solo la herramienta nueva.

| Archivo | Contenido | Tamaño aproximado |
|---|---|---|
| `yellow_tripdata_2024-01.parquet` | 2,964,624 filas y 19 columnas, un viaje por fila | 50 MB |
| `taxi_zone_lookup.csv` | 265 zonas: `LocationID`, `Borough`, `Zone`, `service_zone` | 12 KB |

URLs oficiales:

- Viajes: `https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-01.parquet`
- Zonas: `https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv`

Los notebooks descargan los archivos por URL y los guardan en `datos/` dentro del proyecto de Deepnote. Se hace así porque la subida web de Deepnote Free tiene tope de 100 MB y porque enseña ingesta desde una fuente real. La carpeta de trabajo (`/work`) se conserva cuando la máquina se apaga, `/tmp` no.

## Por qué este dataset

- Ya viene en Parquet, así que el formato se justifica sin trabajo previo.
- Tiene tabla de hechos (viajes) y dimensión (zonas), lo que da joins naturales.
- Es lo bastante grande para justificar evaluación lazy y lo bastante chico para la máquina Basic de Deepnote (alrededor de 390 MB en memoria).

## Puntos de enseñanza que regala

- `LocationID` 264 y 265 son "Unknown", ilustra por qué un `INNER JOIN` puede perder filas.
- Hay viajes con distancia cero, importes negativos y fechas fuera del mes. Material directo para la sesión de calidad de datos.
- Schema drift entre meses: `passenger_count`, `RatecodeID` y `congestion_surcharge` cambian entre `DOUBLE` e `INT64` según el archivo, y `airport_fee` a veces va capitalizado. Los archivos de 2025 en adelante agregan `cbd_congestion_fee` (20 columnas contra 19). Por eso se fija un solo mes para clase y el schema drift se muestra como demostración.

## Columnas principales (enero 2024)

Verificar el esquema real con `viajes.schema` en la sesión 1, estas son las que más se usan:

- `tpep_pickup_datetime`, `tpep_dropoff_datetime`: inicio y fin del viaje
- `passenger_count`, `trip_distance`: pasajeros y distancia en millas
- `PULocationID`, `DOLocationID`: zona de origen y destino (llave hacia `taxi_zone_lookup.csv`)
- `payment_type`: método de pago (código numérico)
- `fare_amount`, `tip_amount`, `total_amount`: importes en dólares

## Alternativa local: Ecobici CDMX

- Portal: `datos.cdmx.gob.mx`
- Uso: gancho de motivación y opción de proyecto final.
- Verificar disponibilidad antes de cada cohorte, los históricos han tenido fechas de actualización irregulares. El feed en tiempo real (GBFS) no entrega histórico.

## Otras fuentes para el proyecto final

- `inegi.org.mx/datosabiertos`
- `datos.gob.mx`
- Un dataset libre del alumno, aprobado por el instructor

## Respaldo si CloudFront falla en clase

- Descargar los dos archivos antes de la sesión y subir el parquet a una carpeta compartida (Google Drive o GitHub Release) con enlace público.
- Dejar en el notebook una variable `URL_VIAJES` fácil de cambiar por la URL de respaldo.
