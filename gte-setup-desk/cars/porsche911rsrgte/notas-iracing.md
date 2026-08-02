# Notas oficiales de iRacing — Porsche 911 RSR GTE

Este archivo recoge, resumidas y organizadas por tema, las notas que iRacing
aporta para este coche. Se amplía sesión a sesión: cada vez que haya notas
nuevas, se añade un bloque `## Sesión — <fecha>` al final con lo que aporte
de nuevo, sin borrar lo anterior.

---

## Nomenclatura de los setups de iRacing (carpeta del coche)

| Setup | Combustible | Uso |
|---|---|---|
| `baseline` | — | Alta downforce, estable, punto de partida/introducción al coche |
| `baseline_wet` | — | Neumáticos de lluvia + TC ajustado para mojado |
| `*_sprint` | 50% | Carreras con límite de combustible, o de ~25-30 min |
| `*_endurance` | 100% | Carreras sin límite de combustible, o de ~1h o más |
| `*_nurburgring_combined` / `*_ringmeister` | 50% | Solo Nürburgring Nordschleife; altura mínima 70 mm |

## Inspección técnica

Si el setup falla la inspección técnica, lo más probable es que haya que
ajustar las **alturas de suelo (ride heights)**, delante y/o detrás.

## Trim aerodinámico según velocidad punta del circuito

El ángulo del alerón trasero (**RWA**, rango total 0°–12°) determina el nivel
de downforce. `high_downforce` de iRacing usa 9°, `low_downforce` usa 1°.

| Velocidad punta del circuito | Nivel de downforce | RWA sugerido |
|---|---|---|
| < 250 km/h | Alta | 9° a 12° |
| 250–270 km/h | Media | 2° a 8° |
| > 270 km/h | Baja / mínima | 0° o 1° |

Más altitud o más calor ambiente → conviene más downforce que la tabla.
El diseño del circuito (nº de curvas rápidas, etc.) también influye — la
tabla es una guía, no una regla fija.

### Efecto del ángulo de alerón trasero (RWA)

- **Menos ángulo** → más sobreviraje, menos downforce, menos drag (arrastre),
  menos velocidad en curva, **más velocidad punta**.
- **Más ángulo** → más subviraje, más downforce, más drag,
  **más velocidad en curva**, menos velocidad punta.

## Alturas dinámicas (ride heights) y plataforma aerodinámica

- El GTE es muy sensible a pequeñas variaciones de altura, delante y detrás.
- **Máxima downforce total** = alerón al máximo + rango de alturas dinámicas
  objetivo (se calcula en la calculadora Aero Balance, pestaña Tires/Aero).
- Salirse del rango objetivo (por arriba o por abajo) = pérdida de downforce.
- Si la altura trasera sube más de la cuenta en frenada → el balance se
  desplaza hacia delante Y se pierde downforce a la vez → efecto
  desestabilizador. Esto es lo que en la práctica limita cuánto puedes
  acercarte al máximo teórico.
- **Mínimo drag** = alerón al mínimo + mismo rango de alturas objetivo —
  raramente alcanzable sin tocar el suelo, y esta puesta a punto no es
  óptima ni para downforce total ni para el balance.
- Cambiar solo el ángulo del alerón cambia el balance aerodinámico → usar
  la Aero Balance Calculator (Tires/Aero) para ver los ajustes y alturas
  objetivo recomendados para compensar (funciona en ambos sentidos).
- Se pueden combinar ajustes de altura delantera + trasera para retener
  más downforce al bajar el alerón, a costa de algo más de drag.
- Los valores de la pestaña Tires/Aero son **objetivos orientativos**, no
  dogma: si no se puede alcanzar un buen balance exactamente en esos
  números, prioriza el balance general por encima del número exacto.

## Barras estabilizadoras (ARB)

- ARB delantera más dura → **más subviraje**
- ARB delantera más blanda → **más sobreviraje**
- ARB trasera más dura → **más sobreviraje**
- ARB trasera más blanda → **más subviraje**
- Ambas más blandas → menos rendimiento aerodinámico, más agarre mecánico
  (bueno en pistas rugosas), respuesta más lenta a los inputs.
- Ambas más duras → más rendimiento aerodinámico (bueno en curvas rápidas
  de barrido), menos agarre mecánico, respuesta más rápida a los inputs.

## Diferencial

Cuatro ajustes disponibles:

**Diff coast / drive ramp angle** — ángulo menor = más bloqueo.
- *Coast* = fase de deceleración (soltar gas / frenar).
- *Drive* = fase de aceleración.

**Clutch plates / Friction faces** — dominan con par de entrada alto
(full throttle, frenada sostenida, coastdown puro):
- Más discos → más subviraje en retención, más sobreviraje en aceleración,
  menos giro de la rueda interior en superficies rugosas o al pisar pianos.
- Menos discos → lo contrario de lo anterior; normalmente mejor en pistas
  suaves y con pianos planos (ej. Spa).

**Preload** — se suma al par total de bloqueo como un offset siempre
presente, incluso con par cero. Domina sobre todo en transición (al soltar
gas, o al inicio del trail braking):
- Más preload → menos sobreviraje al soltar gas, más estabilidad en
  entrada de curva, más subviraje en retención, más sobreviraje en
  aceleración.
- Menos preload → lo contrario: más sobreviraje al soltar gas, menos
  estabilidad en entrada, menos subviraje en retención, menos sobreviraje
  en aceleración.

## Marchas

Las relaciones por defecto están pensadas para ajustarse a la curva de par
del motor. Recomendación de iRacing: ajustar primero el **Final Drive**
según la velocidad punta del circuito, y luego mover marchas individuales
±1 paso para mantenerte en la zona óptima de la banda de potencia.

---

## Cómo se usa esto en la práctica

- Antes de tocar el alerón trasero en la app, mira la tabla de velocidad
  punta de arriba para elegir un RWA de partida razonable.
- Si cambias el alerón, usa el razonamiento del Aero Balance Calculator
  (alturas objetivo) para no descompensar el balance sin darte cuenta.
- Si notas sobreviraje/subviraje en un tramo concreto, contrasta primero
  con las tablas de ARB y diferencial de aquí antes de tocar varios
  parámetros a la vez.
