# GTE Setup Desk

Herramienta interactiva de puesta a punto para competir en GTE en iRacing.

## Estructura del proyecto

```
gte-setup-desk/
  gte-setup-desk.html            ← Archivo final, listo para usar/abrir (generado)
  gte-setup-desk.template.html   ← Plantilla de la app (sin datos de coches)
  build.py                       ← Regenera gte-setup-desk.html a partir de cars/
  cars/
    ferrari488gte/
      config.json                ← Parámetros exactos del Ferrari 488 GTE
    porsche911rsrgte/
      config.json                ← Parámetros aproximados del Porsche 911 RSR GTE
  scripts/
    guardar_setup_ferrari488gte.bat
```

## Cómo añadir un coche nuevo

1. Crea una carpeta nueva dentro de `cars/`, con el nombre del coche
   (por ejemplo `cars/bmw-m8-gte/`).
2. Dentro, crea un `config.json` con la misma forma que
   `cars/ferrari488gte/config.json` (grupos de parámetros para el
   Ingeniero de Motor y el Ingeniero de Aero, con id, etiqueta, unidad,
   rango, paso y valor de partida — o un desplegable de opciones).
3. Ejecuta `python3 build.py` desde esta carpeta.
4. Se regenera `gte-setup-desk.html` con el coche nuevo ya disponible
   en el desplegable de la app.

No hace falta tocar `gte-setup-desk.template.html` ni el resto del
código para añadir un coche — solo su carpeta y su `config.json`.

## Coches actuales

- **Ferrari 488 GTE** — parámetros exactos, tomados de capturas de iRacing.
- **Porsche 911 RSR GTE** — parámetros aproximados, pendientes de capturas
  exactas del juego.

## Cómo usar la app

Abre `gte-setup-desk.html` dentro de una conversación de Claude (como
artefacto), para que funcionen correctamente:

- El guardado interno del histórico de setups.
- El diálogo con los ingenieros (llama a la API de Claude desde dentro
  del artefacto).

Usa los botones **Exportar** / **Importar** del panel de histórico para
tener siempre una copia de seguridad de tus setups en un `.json` local,
independiente de dónde abras la herramienta.

## Scripts

- `scripts/guardar_setup_ferrari488gte.bat` — crea (si no existe) la
  carpeta `setupClaude` dentro de la carpeta de setups del Ferrari 488 GTE
  en iRacing, y copia ahí los archivos `.sto` que arrastres sobre él.
