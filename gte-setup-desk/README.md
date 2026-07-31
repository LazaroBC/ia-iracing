# iRacing GTE Setups

Proyecto personal de puesta a punto para competir en GTE en iRacing.

## Contenido

- `gte-setup-desk.html` — Herramienta interactiva (Setup Desk) con dos roles de ingeniería
  (Motor / Aerodinámica), parámetros exactos de iRacing por coche, histórico de setups
  guardados y un diálogo con los ingenieros que interpreta el feedback del piloto y
  sugiere cambios de setup.
- `guardar_setup_ferrari488gte.bat` — Script de Windows que crea (si no existe) la carpeta
  `setupClaude` dentro de la carpeta de setups del Ferrari 488 GTE en iRacing, y copia ahí
  los archivos `.sto` que arrastres sobre él.

## Coches soportados actualmente

- Ferrari 488 GTE (parámetros exactos, tomados de capturas de iRacing)
- Porsche 911 RSR GTE (parámetros aproximados, pendientes de capturas exactas)

## Cómo usar la app

1. Abre `gte-setup-desk.html` dentro de una conversación de Claude (como artefacto) para
   que el guardado interno y el diálogo con los ingenieros funcionen correctamente.
2. Usa los botones **Exportar** / **Importar** del panel de histórico para tener siempre
   una copia de seguridad de tus setups en un `.json` local.

## Historial

Este repo se usa como control de versiones del proyecto a medida que se van afinando
parámetros, añadiendo coches nuevos o mejorando la herramienta.
