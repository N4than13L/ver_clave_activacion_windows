import winreg

def obtener_y_guardar_clave():
    try:
        # Abrir la ruta del registro donde se guarda la clave original
        ruta_registro = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\SoftwareProtectionPlatform"
        llave = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, ruta_registro)
        
        # Leer el valor de BackupProductKeyDefault
        clave_producto, tipo = winreg.QueryValueEx(llave, "BackupProductKeyDefault")
        winreg.CloseKey(llave)
        
        # Guardar la clave en un archivo .txt
        nombre_archivo = "clave_windows.txt"
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            archivo.write(f"Tu clave de Windows 11 es: {clave_producto}\n")
            
        print(f"Éxito: Clave guardada correctamente en '{nombre_archivo}'.")
        
    except Exception as e:
        print(f"Error: No se pudo obtener o guardar la clave. Detalle: {e}")

if __name__ == "__main__":
    obtener_y_guardar_clave()
