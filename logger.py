import logging
from config import LOGS_DIR

# Crear la carpeta de logs si no existe
LOGS_DIR.mkdir(exist_ok=True)

# Configuración del archivo de log
logging.basicConfig(
    filename=LOGS_DIR / "log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def info(mensaje):
    print(f"[INFO] {mensaje}")
    logging.info(mensaje)

def error(mensaje):
    print(f"[ERROR] {mensaje}")
    logging.error(mensaje)