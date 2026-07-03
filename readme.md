Documentación: Extractor de clave de producto de Windows
Descripción general
Este script en Python lee la clave de producto de Windows almacenada en el registro del sistema (la que Windows guarda como respaldo al activarse) y la guarda en un archivo de texto local.
Requisitos

Sistema operativo: Windows (usa el módulo winreg, exclusivo de Windows).
Permisos: Debe ejecutarse con privilegios de administrador, ya que la ruta del registro consultada normalmente requiere acceso elevado.
Python: No requiere librerías externas; winreg viene incluido en la instalación estándar de Python en Windows.

Funcionamiento paso a paso

Apertura de la clave del registro

python ruta_registro = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\SoftwareProtectionPlatform"
llave = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, ruta_registro)
Se abre la ruta donde Windows almacena información relacionada con la activación del sistema.

Lectura del valor

python clave_producto, tipo = winreg.QueryValueEx(llave, "BackupProductKeyDefault")
Se obtiene el valor BackupProductKeyDefault, que contiene la clave de producto original grabada en el firmware/BIOS (en equipos OEM) o la usada durante la activación.

Cierre de la clave del registro

python winreg.CloseKey(llave)
Buena práctica para liberar el recurso del sistema una vez leído el valor.

Guardado en archivo

python with open(nombre_archivo, "w", encoding="utf-8") as archivo:
archivo.write(f"Tu clave de Windows 11 es: {clave_producto}\n")
La clave se escribe en un archivo clave_windows.txt en el directorio donde se ejecuta el script.

Manejo de errores
Todo el proceso está envuelto en un bloque try/except, por lo que si la ruta no existe, el valor no está presente, o faltan permisos, se captura la excepción y se informa el motivo por consola.

Salida esperada

Éxito: Se crea (o sobrescribe) el archivo clave_windows.txt con el mensaje:

Tu clave de Windows 11 es: XXXXX-XXXXX-XXXXX-XXXXX-XXXXX

Error: Se imprime un mensaje indicando que no se pudo leer o guardar la clave, junto con el detalle de la excepción (por ejemplo, FileNotFoundError si la ruta del registro no existe en ese equipo).

Consideraciones importantes

⚠️ Seguridad: La clave de producto es información sensible. El archivo .txt generado queda en texto plano y sin cifrar; conviene eliminarlo o protegerlo tras su uso.
⚠️ No todos los equipos tienen este valor: BackupProductKeyDefault suele existir en equipos con licencia OEM grabada en el firmware (tabla ACPI/MSDM). En equipos activados por otros medios (cuenta digital, clave retail, KMS) puede no estar presente, y el script arrojará error.
⚠️ Privilegios: Si el script no se ejecuta como administrador, es probable que OpenKey falle por falta de permisos.
