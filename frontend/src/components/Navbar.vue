<script setup>
import { useRouter, useRoute } from "vue-router";
import { computed, ref, onMounted, onUnmounted, watch } from "vue";
import { useAuthStore } from "../stores/auth";
// IMPORTANTE: Asegúrate de tener instalado bootstrap vía npm
import { Collapse } from "bootstrap";

const router = useRouter();
const route = useRoute();
const auth = useAuthStore();

// --- LÓGICA PARA EL SCROLL DINÁMICO ---
const isScrolled = ref(false);

const handleScroll = () => {
  isScrolled.value = window.scrollY > 50;
};

// --- LÓGICA PARA EL AUTO-CIERRE DEL MENÚ ---
let bsCollapse = null;

onMounted(() => {
  window.addEventListener("scroll", handleScroll);

  // Inicializamos el objeto Collapse de Bootstrap referenciando el ID del HTML
  const menuElement = document.getElementById("navbarKofan");
  if (menuElement) {
    bsCollapse = new Collapse(menuElement, { toggle: false });
  }
});

// ESCUCHADOR: Cuando la ruta cambie, cerramos el menú
watch(
  () => route.path,
  () => {
    const menuElement = document.getElementById("navbarKofan");
    // Si el menú está abierto (clase 'show' de Bootstrap), lo ocultamos
    if (menuElement && menuElement.classList.contains("show")) {
      bsCollapse.hide();
    }
  },
);

onUnmounted(() => {
  window.removeEventListener("scroll", handleScroll);
});

// --- LÓGICA DE USUARIO ---
const isLogged = computed(() => auth.isLogged);
const MyProfile = computed(() => "Mi Perfil");

function logout() {
  auth.logout();
  router.push("/home");
}

// Modificamos la lógica de isScrolled para que sea un computed
const navbarSolid = computed(() => {
  // 1. Si el usuario ya hizo scroll, siempre es sólido
  if (isScrolled.value) return true;

  // 2. Lista de NOMBRES de rutas que deben tener navbar sólido
  const nombresSolid = [
    "login", 
    "register", 
    "account-datos", 
    "account-reservas", 
    "account-avisos", 
    "account-reserva-detalle" // Este es el nombre que definimos en el router
  ];

  // 3. Verificamos si el nombre de la ruta actual está en la lista O si empieza por /Account
  return nombresSolid.includes(route.name) || route.path.startsWith("/Account");
});
</script>

<template>
  <header
    class="navbar navbar-expand-lg fixed-top"
    id="barra"
    :class="{ 'navbar-scrolled': navbarSolid }"
  >
    <div class="container-fluid">
      <router-link to="/home" class="navbar-brand logo-section">
        <img src="../img/Kofan.png" width="70" alt="Logo Kofán" />
      </router-link>

      <button
        class="navbar-toggler custom-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarKofan"
        aria-controls="navbarKofan"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarKofan">
        <ul class="navbar-nav mx-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <router-link to="/home" class="nav-link">Inicio</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/about" class="nav-link">Nosotros</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/services" class="nav-link">Servicios</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/galeria" class="nav-link">Galería</router-link>
          </li>
        </ul>

        <div class="d-lg-flex align-items-center gap-3 contact-section">
          <button
            class="btn btn-success btn-contate"
            @click="router.push('/contacto')"
          >
            Contáctanos
          </button>

          <ul class="navbar-nav login-nav align-items-center">
            <li v-if="!auth.isLogged" class="nav-item d-flex gap-2">
              <router-link
                to="/login"
                class="btn btn-outline-light btn-sm px-3"
              >
                Ingresar
              </router-link>
              <router-link to="/register" class="btn btn-success btn-sm px-3">
                Registrarse
              </router-link>
            </li>

            <li v-else class="nav-item dropdown">
              <button
                class="btn btn-success dropdown-toggle d-flex align-items-center gap-2"
                data-bs-toggle="dropdown"
                aria-expanded="false"
              >
                <font-awesome-icon :icon="['fas', 'user-circle']" />
                <span>Hola, {{ auth.user?.nombre }}</span>
              </button>
              <ul class="dropdown-menu dropdown-menu-end shadow">
                <li>
                  <router-link class="dropdown-item" to="/Account/datos">
                    <font-awesome-icon
                      :icon="['fas', 'id-card']"
                      class="me-2"
                    />
                    Mi Perfil
                  </router-link>
                </li>
                <li><hr class="dropdown-divider" /></li>
                <li>
                  <a
                    class="dropdown-item text-danger"
                    href="#"
                    @click.prevent="logout"
                  >
                    <font-awesome-icon
                      :icon="['fas', 'sign-out-alt']"
                      class="me-2"
                    />
                    Cerrar Sesión
                  </a>
                </li>
              </ul>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </header>
</template>

<style scoped>
#barra {
  background: transparent;
  transition: all 0.4s ease-in-out;
  padding: 1rem 1.5rem;
}

.navbar-scrolled {
  background: #0f3b2a !important;
  padding: 0.5rem 1.5rem !important;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
}

.nav-link {
  color: white !important;
  font-weight: 500;
  margin: 0 10px;
  transition: color 0.3s;
}

.nav-link:hover,
.router-link-active {
  color: #2ecc71 !important;
}

/* Personalización del botón hamburguesa */
.custom-toggler.navbar-toggler {
  border-color: rgba(255, 255, 255, 0.5);
  padding: 4px 8px;
}

.custom-toggler .navbar-toggler-icon {
  background-image: url("data:image/svg+xml;charset=utf8,%3Csvg viewBox='0 0 32 32' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath stroke='white' stroke-width='2' stroke-linecap='round' stroke-miterlimit='10' d='M4 8h24M4 16h24M4 24h24'/%3E%3C/svg%3E");
}

.user-link {
  cursor: pointer;
}

.btn-contate {
  border-radius: 25px;
  padding: 8px 20px;
  font-weight: 600;
}

.auth-section {
  min-height: 100vh;
  background: #f4f7f6;
  padding-top: 100px; /* Esto deja espacio para el Navbar sólido */
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Ajustes para Móviles */
@media (max-width: 991px) {
  .navbar-collapse {
    background: #0f3b2a;
    margin-top: 1rem;
    padding: 1.5rem;
    border-radius: 15px;
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
  }

  .nav-item {
    padding: 10px 0;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  }

  .contact-section {
    margin-top: 15px;
    text-align: center;
  }
}
</style>
