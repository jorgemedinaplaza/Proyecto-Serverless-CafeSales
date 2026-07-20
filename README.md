# Proyecto Serverless AWS - Cafe Sales

## Maestría en Arquitectura de Software

### Politécnico Grancolombiano

**Asignatura:** Contenerización de Aplicaciones

---

## Descripción

Aplicación desarrollada bajo una arquitectura Serverless en AWS para la gestión y consulta de ventas de una cafetería.

La solución utiliza servicios administrados de AWS para el almacenamiento, procesamiento y consulta de datos.

---

<h2 align="center">
Arquitectura de la Solución
</h2>

<p align="center">
    Arquitectura/Designer.jpg width="900">
</p>

---

## Tecnologías Utilizadas

- AWS S3
- AWS Lambda
- Amazon DynamoDB
- AWS Amplify
- HTML5
- CSS3
- JavaScript
- GitHub

---

## Funcionalidades

### Carga de Datos

- Lectura automática de archivos CSV desde Amazon S3.
- Inserción de registros en DynamoDB mediante AWS Lambda.

### Consulta de Información

- Consulta por Transaction ID.
- Visualización de ventas registradas.
- Consulta de las primeras 50 ventas almacenadas.

### Publicación

- Despliegue Web mediante AWS Amplify.
- Consumo de servicios Serverless mediante Function URL.

---

## Estructura del Proyecto

```text
Proyecto-Serverless-CafeSales
│
├── CafeSalesApp
│   ├── index.html
│   ├── styles.css
│   └── app.js
│
├── lambda-import
│   └── lambda_import.py
│
├── lambda-query
│   └── lambda_query.py
│
├── dataset
│   └── clean_cafe_saless.csv
│
└── README.md
```

---

## URL de la Aplicación

https://staging.dka722iag56xl.amplifyapp.com/

```

---

## Autor

JORGE ISMAEL MEDINA PLAZA

Maestría en Arquitectura de Software

Politécnico Grancolombiano
