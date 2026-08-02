#!/usr/bin/env python3
"""
Genera gte-setup-desk.html a partir de:
  - gte-setup-desk.template.html   (la app, sin datos de coches)
  - cars/<carpeta-coche>/config.json   (un archivo por coche)

Para añadir un coche nuevo:
  1. Crea una carpeta nueva dentro de cars/, por ejemplo cars/bmw-m8-gte/
  2. Pon dentro un config.json con esta forma (mira cars/ferrari488gte/config.json
     como ejemplo completo):
       {
         "key": "bmw",
         "name": "BMW M8 GTE",
         "exact": false,
         "motorGroups": [ { "title": "...", "color": "var(--motor)", "fields": [...] } ],
         "aeroGroups": [ ... ]
       }
     Cada field es: {"id","label","unit","type":"number","min","max","step","def"}
     o bien: {"id","label","type":"select","options":[...],"def":...}
  3. Ejecuta: python3 build.py
  4. Se regenera gte-setup-desk.html con el coche nuevo ya disponible en el desplegable.
"""
import json
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
CARS_DIR = os.path.join(ROOT, 'cars')
TEMPLATE = os.path.join(ROOT, 'gte-setup-desk.template.html')
OUTPUT = os.path.join(ROOT, 'gte-setup-desk.html')


def load_cars():
    cars = {}
    order = []
    for folder in sorted(os.listdir(CARS_DIR)):
        config_path = os.path.join(CARS_DIR, folder, 'config.json')
        if not os.path.isfile(config_path):
            continue
        with open(config_path, encoding='utf-8') as f:
            data = json.load(f)
        key = data.get('key', folder)
        car = {k: v for k, v in data.items() if k != 'key'}

        notes_path = os.path.join(CARS_DIR, folder, 'notas-iracing.md')
        if os.path.isfile(notes_path):
            with open(notes_path, encoding='utf-8') as f:
                car['referenceNotes'] = f.read()

        cars[key] = car
        order.append(key)
    return cars, order


def main():
    cars, order = load_cars()
    if not cars:
        raise SystemExit('No se encontró ningún cars/<carpeta>/config.json')

    cars_json = json.dumps(cars, indent=2, ensure_ascii=False)

    options_html = '\n'.join(
        f'        <option value="{key}">{cars[key]["name"]}</option>' for key in order
    )

    with open(TEMPLATE, encoding='utf-8') as f:
        html = f.read()

    if '/*__CARS_JSON__*/{}' not in html:
        raise SystemExit('No se encontró el marcador /*__CARS_JSON__*/{} en la plantilla')
    if '<!--__CAR_OPTIONS__-->' not in html:
        raise SystemExit('No se encontró el marcador <!--__CAR_OPTIONS__--> en la plantilla')

    html = html.replace('/*__CARS_JSON__*/{}', cars_json)
    html = html.replace('<!--__CAR_OPTIONS__-->', options_html)

    with open(OUTPUT, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f'OK: generado {OUTPUT} con {len(cars)} coche(s): {", ".join(order)}')


if __name__ == '__main__':
    main()
