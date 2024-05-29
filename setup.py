import sys
from cx_Freeze import setup, Executable

# Reemplaza 'tu_script.py' con el nombre de tu script Python principal
script = 'proyecto.py'

base = None
if sys.platform == "win32":
    base = "Win32GUI"  # Para ocultar la ventana de la consola en Windows

setup(
    name="Ejecutable",
    version="1.0",
    description="Descripción de tu programa",
    executables=[Executable(script, base=base)],
    options={"build_exe": {"packages": ["os"], "include_files": []}},
)
