import os

def generar_doc_backend():
    print("🐍 Documentando el Backend (Python)...")
    
    # 1. Buscar librerías importadas
    librerias = set()
    archivos_py = []
    
    for root, dirs, files in os.walk('.'):
        if 'venv' in root or '__pycache__' in root: continue
        for file in files:
            if file.endswith('.py') and file != 'doc_backend.py':
                archivos_py.append(os.path.join(root, file))
                with open(os.path.join(root, file), 'r', encoding='utf-8', errors='ignore') as f:
                    for line in f:
                        if line.startswith('import ') or line.startswith('from '):
                            parts = line.split()
                            if len(parts) > 1:
                                lib = parts[1].split('.')[0]
                                if lib not in ['os', 'sys', 'json', 're', 'datetime']:
                                    librerias.add(lib)

    # 2. Crear requirements.txt
    with open('requirements.txt', 'w', encoding='utf-8') as req:
        for lib in sorted(list(librerias)):
            req.write(f"{lib}\n")
    
    # 3. Crear DOC_BACKEND.md
    with open('DOC_BACKEND.md', 'w', encoding='utf-8') as doc:
        doc.write("# ⚙️ Documentación Backend - Ecohotel Kofán\n\n")
        doc.write("## 🐍 Dependencias de Python\n")
        for lib in sorted(list(librerias)):
            doc.write(f"- `{lib}`\n")
        
        doc.write("\n## 📂 Estructura de Archivos\n")
        for arc in archivos_py:
            doc.write(f"- `{arc}`\n")

    print("✅ 'requirements.txt' y 'DOC_BACKEND.md' generados.")

if __name__ == "__main__":
    generar_doc_backend()