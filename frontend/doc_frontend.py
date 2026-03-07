import os
import json
import re

def generar_doc_frontend():
    print("🎨 Documentando el Frontend (Vue.js)...")
    
    # 1. Leer package.json
    dependencias = {}
    if os.path.exists('package.json'):
        with open('package.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            dependencias = data.get('dependencies', {})

    # 2. Escanear iconos de FontAwesome en /src
    iconos = set()
    patron = r'icon="fa-solid fa-([^"]+)"'
    for root, dirs, files in os.walk('src'):
        for file in files:
            if file.endswith('.vue'):
                with open(os.path.join(root, file), 'r', encoding='utf-8', errors='ignore') as f:
                    encontrados = re.findall(patron, f.read())
                    iconos.update(encontrados)

    # 3. Listar vistas de Admin
    vistas = []
    path_admin = os.path.join('src', 'views', 'admin')
    if os.path.exists(path_admin):
        vistas = [f for f in os.listdir(path_admin) if f.endswith('.vue')]

    # 4. Crear archivo
    with open('DOC_FRONTEND.md', 'w', encoding='utf-8') as doc:
        doc.write("# 🖥️ Documentación Frontend - Ecohotel Kofán\n\n")
        doc.write("## 📦 Librerías de Node.js\n")
        for lib, ver in dependencias.items():
            doc.write(f"- {lib} ({ver})\n")
        
        doc.write("\n## 🚩 Iconos FontAwesome Detectados\n")
        for ico in sorted(list(iconos)):
            doc.write(f"- `fa-{ico}`\n")
            
        doc.write("\n## 📂 Módulos Administrativos\n")
        for v in vistas:
            doc.write(f"- `{v}`\n")

    print("✅ Archivo 'DOC_FRONTEND.md' generado.")

if __name__ == "__main__":
    generar_doc_frontend()