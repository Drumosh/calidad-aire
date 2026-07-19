from pathlib import Path

# ==========================================
# CONFIGURACIÓN GENERAL
# ==========================================

# URL del sitio
URL = "https://airerm.mma.gob.cl/calidad-del-aire/"

# Carpeta donde se guardarán las imágenes
ONEDRIVE_DIR = Path(r"C:\Users\jocar\OneDrive\Calidad de Aire")

# Carpeta base del proyecto
BASE_DIR = Path(__file__).parent

# Carpetas internas
CAPTURAS_DIR = BASE_DIR / "capturas"
LOGS_DIR = BASE_DIR / "logs"
HISTORIAL_DIR = BASE_DIR / "historial"

# Archivo Excel
EXCEL_HISTORIAL = HISTORIAL_DIR / "Historial_Calidad_Aire.xlsx"

# Hora de ejecución
HORA_EJECUCION = "11:00"

# Tiempo máximo de espera (segundos)
TIMEOUT = 60

# Reintentos
REINTENTOS = 3