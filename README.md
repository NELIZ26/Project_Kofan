# 🌿 Kofán - Experiencia Amazónica 🍃

> **"Donde la selva y el espíritu se encuentran."**
> Una plataforma web moderna diseñada para conectar a los viajeros con la esencia ancestral de la comunidad Kofán en el Putumayo, Colombia.

---

## ✨ El Proyecto

Kofán no es solo un sitio web, es una ventana a la biodiversidad y cultura del Putumayo. El proyecto incluye:

- **Home Dinámico:** Bienvenida con animaciones fluidas y diseño orgánico.
- **Experiencias Auténticas:** Catálogo de senderismo, cultura viva y descanso pleno.
- **Hospedaje Ancestral:** Sistema de tarjetas interactivas con detalles de tarifas y servicios.
- **Información de Viaje:** Sección legal, políticas de reserva y consejos útiles.
- **Ubicación Real:** Integración con mapas y guías de acceso desde Puerto Asís.

---

## 🛠️ Tecnologías Utilizadas (Tech Stack)

- **Framework:** [Vue 3](https://vuejs.org/) (Composition API)
- **Build Tool:** [Vite](https://vitejs.dev/)
- **Estilos:** [Bootstrap 5](https://getbootstrap.com/) + CSS3 Custom Shapes (Dividers orgánicos)
- **Iconografía:** [FontAwesome](https://fontawesome.com/) (Solid & Brands)
- **Fuentes:** Google Fonts (_Handlee_ para títulos y _Poppins_ para cuerpo de texto)

---

## 🚀 Configuración del Proyecto (Setup)

### Recomendaciones de IDE

- **VS Code** + Extensión **Vue - Official** (anteriormente Volar).
- Desactivar la extensión **Vetur** para evitar conflictos.

### Instalación

```sh
# 1. Instalar dependencias base
npm install

# 2. Instalar paquetes de iconos necesarios (FontAwesome)
npm install @fortawesome/fontawesome-svg-core @fortawesome/free-solid-svg-icons @fortawesome/free-brands-svg-icons @fortawesome/vue-fontawesome@latest
```
# Iniciar servidor de desarrollo (Hot-Reload)
npm run dev

# Compilar y minificar para producción
npm run build

src/
 ├── components/      # Componentes independientes (Navbar, Footer, etc.)
 ├── styles/          # CSS global y variables de color (#1a5c43, #0f3b2a)
 ├── App.vue          # Componente raíz con el layout principal
 └── main.js          # Configuración de FontAwesome y registro de componentes