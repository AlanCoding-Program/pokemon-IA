La API que desarrollamos es de pokemon, expecificamente una que simula ser una pokedex. por lo que posee un total de 4 tablas las cuales son: 

| Tabla         | Descripción                                                   | Parámetros                              |
| ------------- | ------------------------------------------------------------- | --------------------------------------- |
| **pokemon**   | Contiene los Pokémon registrados                              | `nombre`                                |
| **tipo**      | Define los tipos de los Pokémon                               | `tipo`                                  |
| **habilidad** | Define las habilidades disponibles                            | `habilidad`                             |
| **pokedex**   | Relaciona las tres tablas anteriores mediante claves foráneas | `pokemon_id`, `tipo_id`, `habilidad_id` |


**estructura**

hicimos la API dividiendo la parte logica y las ruta, por lo que metimos los conjuntos de archivos en dos carpetas diferentes para que sea mas organizado e intuititvo para aquel que ojee el proyecto.

📦 proyecto-pokemon/
├── api/
│   └── main.py               # Punto de entrada principal
├── modelos.py                # Modelos Pydantic
├── Rutas/
│   ├── pokemon.py            # Endpoints relacionados a Pokémon
│   ├── tipos.py              # Endpoints relacionados a Tipos
│   ├── habilidad.py          # Endpoints relacionados a Habilidades
│   └── pokedex.py            # Endpoints para la tabla relacional Pokedex
├── Managers/
│   ├── conexion.py           # Manejo de la conexión a la base de datos
│   ├── Managerpokemon.py     # Lógica para Pokémon
│   ├── Managertipos.py       # Lógica para Tipos
│   ├── Managerhabilidad.py   # Lógica para Habilidades
│   └── Managerpokedex.py     # Lógica para Pokedex
├── requirements.txt
└── vercel.json               # Configuración de despliegue en Vercel


Los endpoints principales son los siguientes:

**tipos**
| Método   | Ruta                         | Descripción                 |
| -------- | ---------------------------- | --------------------------- |
| `POST`   | `/tipo/crear_tipo`           | Crea un nuevo tipo          |
| `GET`    | `/tipo/ver_tipos`            | Lista todos los tipos       |
| `PUT`    | `/tipo/actualizar_tipo/{id}` | Actualiza un tipo existente |
| `DELETE` | `/tipo/borrar_tipo/{id}`     | Elimina un tipo por ID      |


**pokemon**
| Método   | Ruta                               | Descripción             |
| -------- | ---------------------------------- | ----------------------- |
| `POST`   | `/pokemon/crear_pokemon`           | Crea un nuevo Pokémon   |
| `GET`    | `/pokemon/ver_pokemon`             | Lista todos los Pokémon |
| `PUT`    | `/pokemon/actualizar_pokemon/{id}` | Actualiza un Pokémon    |
| `DELETE` | `/pokemon/borrar_pokemon/{id}`     | Elimina un Pokémon      |


**habilidad**
| Método   | Ruta                                   | Descripción                 |
| -------- | -------------------------------------- | --------------------------- |
| `POST`   | `/habilidad/crear_habilidad`           | Crea una nueva habilidad    |
| `GET`    | `/habilidad/ver_habilidades`           | Lista todas las habilidades |
| `PUT`    | `/habilidad/actualizar_habilidad/{id}` | Actualiza una habilidad     |
| `DELETE` | `/habilidad/borrar_habilidad/{id}`     | Elimina una habilidad       |


**pokedex**
| Método | Ruta                       | Descripción                                             |
| ------ | -------------------------- | ------------------------------------------------------- |
| `POST` | `/pokedex/agregar_pokedex` | Agrega un registro combinando Pokémon, tipo y habilidad |
| `GET`  | `/pokedex/ver_pokedex`     | Devuelve la vista completa de la Pokédex con joins      |

