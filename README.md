# Proyecto: CRUD con Python3 + Flask + MySQL + Autenticación


### Instalación
<br>
Sigue estos pasos para instalar y ejecutar la app en tu entorno local

<br><br>
1. **Clona el repositorio**
```bash
git clone https://github.com/Angel-Garay/angel-fazt-python.git
cd angel-fazt-python
```

<br><br>
2. **Crea y activa un entorno virtual:**
```bash
python3 -m venv venv
source venv/bin/activate
```

<br><br>
3. **Instala las dependencias:**
```bash
pip install -r requirements.txt
```

<br><br>
4. **Configura la base de datos MySQL:**
- Aseguráte de tener MySQL instalado y ejecutándose.
- Crea unaa base de datos para el proyecto:
```sql
<!-- Aca va la DB contactos creada manualmente, no hace falta que tenga alguno insertado -->
<!-- Aca va la DB usuarios creada manualmente, hay que crear 1 usuario si o si -->
```

<br><br>
5. **Inicializa el servicio LAMPP**
```bash
cd /opt/lampp
ls				<!-- tiene que existir el manager-linux-x64.run -->
sudo ./manager-linux-x64.run
```

<br><br>
6. **Ejecuta la app**
```bash
python3 App.py
```


<br><br><br>
### Descripción del Proyecto
> Este proyecto es una app web hecha con Flask que permite a los usuarios registrarse, iniciar sesión y gestionar
> sus contactos. Utiliza MySQL como base de datos para almacenar la información. La autenticación se maneja a
> través de Flask-Login, proporcionando una experiencia segura y personalizada para cada usuario. Además, se integra
> con un servidor LAMP para la ejecución y gestión de las solicitudes.


<br><br><br>
### Funcionalidades:
- Registro e inicio de sesión de usuarios.
- Gestión de contactos.
- Integración con MySQL para almacenamiento persistente de datos.
- Uso de LAMP para el despliegue de la aplicación.


<br><br><br>
### Tecnologías Usadas
- **Python 3**: Lenguaje.
- **Flask**: Framework web.
- **MySQL**: Sistema de gestión de bases de datos relacional.
- **Flask-Login**: Extensión de Flask para gestionar la autenticación de usuarios.
- **LAMP**: Conjunto de software libre que incluye Linux, Apache, MySQL y PHP/Perl/Python.
- **HTML/CSS**: Para la estructura y el estilo de la interfaz de usuario.
- **Bootstrap**: Framework de CSS para un diseño.


<br><br><br>
---
### Links de vidos de los cuales surge la idea:
[Fazt](https://www.youtube.com/watch?v=IgCfZkR8wME&t=1763s)
[UskoKruM2010](https://www.youtube.com/watch?v=FX0lMm_Qj10&t=2067s)
[JonMircha](https://www.youtube.com/watch?v=FlsoBiteuPM&t=1313s)


<br><br><br>
---
#### Hecho por Angel Garay



