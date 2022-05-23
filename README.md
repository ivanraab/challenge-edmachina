# challenge-edmachina

En la siguiente APIrest se encuentran tres modelos:

    -Lead:
        Contiene toda la info personal de los leads y las materias y carreras a las que está inscripto.

    -Carrera:
        Contiene un campo nombre y las materias que contiene.

    -Materia:
        Contiene un campo nombre para ser identificada.

SWAGGER:
    -La APIrest cuenta con un swagger configurado. "/swagger"


Inicio:

    Requisitos:

        -docker, docker-compose

    Build:

        -Se debe ir la raiz de repositorio y usar el comando "docker-compose up --build"

    Instanciación:
        
        -Se debe ejecutar bash en el contenedor "docker-compose exec django_app bash"

        -Luego ejecutar las migraciones "python manage.py makemigrations" >> "python manage.py migrate"

    Utilización:

        - Los endpoints de carga se utilizan para cargar información, son los siguientes:

            - POST /api/leads:
                Permite cargar un lead, se debe enviar un objeto con la info personal requerida \
                además de una lista de las carreras que cursa y una lista de las materias que cursa.

            - POST /api/carreras:
                Permite cargar una carrera, se debe enviar un objeto con el nombre de la carrera a crear \
                y una lista de las materias que esta carrera incluye.
            
            - POST /api/materias:
                Permite cargar una materia, se debe enviar un objeto con el nombre de la materia.

        - Los endpoints para obtener información, son los siguientes:

            - GET /api/leads/  -  /api/carreras/  -  /api/materias/
                Get de cada uno de estos endpoints permite obtener el listado de leads, carreras o materias.

            - GET /api/leads/{id}/  -  /api/carreras/{id}/  -  /api/materias/{id}/
                Get de cada uno de estos endpoints permite obtener el detalle de un lead, carrera o materia \
                en particular.