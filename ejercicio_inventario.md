# Ejercicio: Procesamiento de un fichero de inventario de servidores

Tu empresa mantiene un fichero plano llamado `inventario.txt` que se
genera automáticamente cada noche por un script antiguo.\
El fichero contiene información de servidores, pero presenta varios
problemas:

-   Formato irregular: espacios de más, mayúsculas/minúsculas
    inconsistentes.\
-   Algunas líneas están incompletas.\
-   Hay campos opcionales.\
-   Los separadores son inconsistentes (`;` o `,`).

El objetivo es procesar este fichero para generar una estructura válida
en Python que puedas usar después para auditorías o informes.

Se adjunta el fichero de ejemplo ```inventario.txt```

## Objetivos del ejercicio

Implementa un script en Python que:

### 1 - Lea el fichero línea a línea

-   Ignora líneas vacías.\
-   Ignora líneas que empiezan con `#`.

### 2 - Normalice cada línea

-   Acepta tanto `;` como `,` como separadores.\
-   Elimina espacios de más.\
-   Pasa **sistema operativo** a minúsculas.\
-   Convierte **responsable** para que empiece en mayúscula (solo
    primera letra).
    -   Ejemplo: `ana` → `Ana`.

### 3 - Valide los datos

Para cada línea procesada, verifica:

-   **nombre** → obligatorio, string no vacío\
-   **ip** → válida en formato IPv4 (puedes usar `split` o el módulo
    `ipaddress`)\
-   **sistema operativo** → uno de: `linux`, `windows`, `macos`\
-   **ubicacion** → puede estar vacía, pero se normaliza a `None`\
-   **responsable** → puede ser `"-"` → se pasa a `None`

Si algo falla → descarta la línea y registra el error en una lista.

### 4 - Construya una lista de diccionarios

Ejemplo de diccionario final:

```python
{ "nombre": "srv-web01", "ip": "192.168.1.10", "sistema":
"linux", "ubicacion": "sala 1", "responsable": "Ana" }
```

### 5 - Escribir en un fichero informe_servidores.txt un informe resumen
Escribir en el fichero de salida los siguientes datos, uno por línea
-   Número de servidores válidos cargados
-   Número de líneas descartadas (con errores)
-   Lista de IPs únicas
-   Cuántos responsables distintos ("dueños" de máquinas)

Salida esperada en el fichero:
```
Número de servidores válidos cargados: 6
Número de líneas descartadas (con errores): 5
Lista de IPs únicas: 192.168.1.10, 192.168.1.20, 192.168.1.30, 10.0.0.5
Responsables distintos: 3
```

## Requisito obligatorio. Descomposición en funciones

 - leer_fichero()
 - normalizar_linea() 
 - validar_datos()
 - procesar_inventario()

# Flujo general de funciones

## leer_fichero()

**Entrada:**  
- Ruta del fichero (`inventario.txt`)

**Acción:**  
- Abre el fichero  
- Lee línea a línea  
- Devuelve una lista de líneas (strings)

**Salida:**  
```
lineas = ["srv-web01 ; 192.168.1.10 ; linux ; sala 1 ; Ana", ...]
```

---

## normalizar_linea(linea)

**Entrada:**  
- Una línea de texto

**Acción:**  
- Reemplaza separadores `;` o `,` por un separador uniforme  
- Elimina espacios de más  
- Convierte `sistema` a minúsculas  
- Capitaliza `responsable` (Ana, Carlos…)  
- Devuelve la línea como diccionario preliminar

**Salida (ejemplo):**
```
{
    "nombre": "...",
    "ip": "...",
    "sistema": "...",
    "ubicacion": "...",
    "responsable": "..."
}
```

---

## validar_datos(diccionario_linea)

**Entrada:**  
- Diccionario de campos normalizados

**Acción:**  
- Verifica que `nombre` no esté vacío  
- Valida que `ip` sea correcta  
- Comprueba que `sistema` ∈ {linux, windows, macos}  
- Normaliza `ubicacion` y `responsable` a `None` si están vacíos o `"-"`  

**Salida:**  
- Si válido → `(True, diccionario)`  
- Si falla → `(False, mensaje_error)`

---

## procesar_inventario()
Esta función es la que orquesta todas las demás y realiza las operaciones finales.

**Entrada:**  
- Ruta del fichero

**Acción:**  
1. Llama a `leer_fichero()` para obtener las líneas  
2. Itera por cada línea  
   - Si está vacía o empieza con `#`, la ignora  
   - Llama a `normalizar_linea()`  
   - Llama a `validar_datos()`  
   - Si es válida → la agrega al inventario final  
   - Si falla → registra el error en la lista de errores  
3. Genera el informe final:  
   - Número de servidores válidos  
   - Líneas descartadas  
   - IPs únicas  
   - Contador por sistema operativo  
   - Responsables distintos  

**Salida:**  
- Devuelve la lista de diccionario con el Inventario válido  
- Lista de errores  
- Informe resumen


