from datetime import datetime
import shutil
from playwright.sync_api import sync_playwright
from config import URL, CAPTURAS_DIR, ONEDRIVE_DIR
from logger import info


CAPTURAS_DIR.mkdir(exist_ok=True)


def capturar_pagina():

    fecha = datetime.now().strftime("%d-%m-%Y")
    archivo = CAPTURAS_DIR / f"Calidad_Aire_{fecha}.png"

    info("Abriendo navegador...")

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=True
        )

        page = browser.new_page(
            viewport={
                "width": 1600,
                "height": 1200
            }
        )

        info("Cargando página...")

        page.goto(
            URL,
            wait_until="networkidle",
            timeout=60000
        )

        info("Buscando panel del pronóstico...")

        panel = page.locator("a.container-pronos")

        panel.wait_for(timeout=10000)

        panel.screenshot(
            path=str(archivo),
            animations="disabled"
        )

        browser.close()

    # Copiar la imagen al OneDrive
    ONEDRIVE_DIR.mkdir(parents=True, exist_ok=True)

    destino = ONEDRIVE_DIR / archivo.name

    shutil.copy2(archivo, destino)

    info(f"Captura guardada en {archivo}")
    info(f"Imagen copiada a {destino}")