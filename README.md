# Django

---

## Configuración del Entorno

Asegúrate de realizar los siguientes pasos:

1. Clona este repositorio en tu máquina local:

```plaintext
git clone https://github.com/jm-suarez/django.git
```

2. Crea un entorno virtual en la carpeta del proyecto:

```
python -m venv venv
```

3. Activa el entorno virtual:

- En Windows:
  ```
  venv\Scripts\activate
  ```
- En macOS y Linux:
  ```
  source venv/bin/activate
  ```

4. Instala las dependencias del proyecto:

```
pip install -r requirements.txt
```

5. Levanta Django Framework:

```
python manage.py runserver
```

6. Estará disponible en http://localhost:8000. Puedes acceder a los diferentes endpoints descritos en la documentación para realizar pruebas.

¡Listo! Ahora puedes comenzar a utilizar.
 * Usuario: User1 
 * Contraseña: Pass.123
---

## Endpoints

### Productos

- **POST /kardexapp/api/productos/all:** Obtiene todos los productos en formato json.
- **GET /kardexapp/productos:** CRUD de productos.

### Saldos Iniciales

- **POST /kardexapp/api/saldos/all:** Obtiene todos los saldos en formato json.
- **GET /kardexapp/saldos:** CRUD de saldos.

### Entregas

- **POST /kardexapp/api/entregas/all:** Obtiene todos las entregas en formato json.
- **GET /kardexapp/entregas:** CRUD de entregas.

### Ingresos

- **POST /kardexapp/api/ingresos/all:** Obtiene todos los ingresos en formato json.
- **GET /kardexapp/ingresos:** CRUD de ingresos.
