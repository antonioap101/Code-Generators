import importlib
import logging

from fastapi import FastAPI, APIRouter

# Configuración del logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Crear un nuevo router con el prefijo /api
api_router = APIRouter(prefix="/api")

# Lista de módulos a importar como routers
modules = [
    "api.graphml.graphml_router",
    "api.crud.crud_router",
    # Añade aquí otros módulos conforme avances en los trabajos
]

for module_name in modules:
    try:
        # Importa dinámicamente el módulo
        module = importlib.import_module(module_name)
        # Registra el router si existe
        if hasattr(module, "router"):
            api_router.include_router(module.router)
            logger.info(f"Router cargado exitosamente desde {module_name}.")
    except ModuleNotFoundError:
        logger.warning(f"El módulo {module_name} no se encontró. Ignorándolo.")
    except Exception as e:
        logger.error(f"Error al cargar el módulo {module_name}: {e}")


# Incluir el nuevo router en la aplicación principal


@api_router.get("/")
def home():
    return {"message": "¡Bienvenido al API de Generación Automática de Código de Antonio Aparicio González!"}


app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
