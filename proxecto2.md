
# Proxecto 2: Integración de inventarios de servidores (TXT + JSON + SQLite)

## Obxectivo

Deseñar un programa en Python que permita combinar e xestionar varios inventarios de servidores, almacenados en diferentes formatos, e almacenar os datos nunha base de datos SQLite.

---

## Ficheiros de entrada

1. **Inventario en texto plano** (`inventario.txt`), co formato do proxecto 1:

```
nombre ; ip ; sistema ; ubicacion ; responsable
```

- O código do proxecto 1 xa procesa este ficheiro e devolve:
  - `lista_servers` → servidores válidos.
  - `lista_errores` → servidores con erros.

2. **Inventario en JSON** (`inventario_json.json`), con diccionarios de servidores pre-validado.  

- Os servidores do JSON poden **coincidir no nome** cos do ficheiro de texto.  
- Non hai erros de formato ou validación nos datos do JSON.

---

## Requisitos do programa

1. **Non modificar o proxecto 1**: utilizar as funcións existentes para procesar `inventario.txt`.  
2. **Procesar o ficheiro JSON**:  
   - Ler os servidores desde JSON.  
   - Engadir os novos servidores ao inventario global.  
3. **Xestionar erros**:  
   - Crear unha lista de erros para os servidores do ficheiro de texto (`lista_errores` do proxecto 1).  
4. **Exportación**:  
   - Gardar todos os servidores válidos nun **novo ficheiro JSON** (`inventario_completo.json`) ordenando as claves e indentando o ficheiro.  
5. **Persistencia en SQLite**:  
   - Crear unha táboa `servidores` nunha base de datos SQLite (`inventario.db`).  
   - Gardar todos os servidores válidos na base de datos.  
   - Evitar duplicados na base de datos usando a clave primaria `nombre`.  
6. **Consulta interactiva**:  
   - Pedir ao usuario un `nombre` de servidor.  
   - Mostrar os datos correspondentes desde a base de datos.

---

## Obxectivos pedagóxicos

- Aprender a integrar distintos formatos de datos (TXT e JSON) sen modificar código preexistente.  
- Practicar lectura e escritura de JSON e SQLite desde Python.  
- Implementar operacións básicas de persistencia e consulta interactiva.
