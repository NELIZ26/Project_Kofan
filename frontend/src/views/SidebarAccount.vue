<script setup>
import { useRouter } from "vue-router";
import { useAuthStore } from "../stores/auth";

const router = useRouter();
const auth = useAuthStore();

const handleLogout = () => {
  auth.logout();
  router.push("/home");
};
</script>

<template>
  <aside class="sidebar-kofan shadow-sm">
    <div class="user-info text-center p-3 mb-3">
      <div class="avatar-placeholder mx-auto mb-2">
        <img src="../img/login.png" alt="">
        <!--<font-awesome-icon :icon="['fas', 'users']" class="me-2 text-success" />-->
        {{ auth.user?.nombre?.charAt(0) }}
      </div>
      <h6 class="mb-0 fw-bold">{{ auth.user?.nombre }}</h6>
      <small class="text-muted">Cliente Kofán</small>
    </div>

    <nav class="nav flex-column gap-2">
      <router-link :to="{ name: 'account-datos' }" class="nav-link-kofan">
        <font-awesome-icon :icon="['fas', 'user-gear']" class="me-2 text-success" /> Datos Personales
      </router-link>
      
      <router-link :to="{ name: 'account-reservas' }" class="nav-link-kofan">
        <font-awesome-icon :icon="['fas', 'calendar-check']" class="me-2 text-success" /> Mis Reservas
      </router-link>
      
      <router-link :to="{ name: 'account-avisos' }" class="nav-link-kofan">
        <font-awesome-icon :icon="['fas', 'bell']" class="me-2 text-success" /> Avisos
      </router-link>

      <hr class="my-2 opacity-10">

      <a href="#" @click.prevent="handleLogout" class="nav-link-kofan logout-link">
        <font-awesome-icon :icon="['fas', 'right-from-bracket']" class="me-2 text-danger" /> Salir
      </a>
    </nav>
  </aside>
</template>

<style scoped>
img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.sidebar-kofan {
  background-color: #ffffff;
  border-radius: 20px;
  padding: 20px;
  border: 1px solid #eee;
}

.avatar-placeholder {
  width: 60px;
  height: 60px;
  background-color: #0f3b2a;
  color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
  font-weight: bold;
}

.nav-link-kofan {
  display: flex;
  align-items: center;
  padding: 12px 15px;
  text-decoration: none;
  color: #444;
  border-radius: 12px;
  transition: all 0.3s ease;
  font-weight: 500;
}

.nav-link-kofan:hover {
  background-color: #f0fdf4;
  color: #0f3b2a;
}

/* Estilo para la ruta activa */
.router-link-active {
  background-color: #0f3b2a !important;
  color: white !important;
}

.router-link-active .text-success {
  color: #2ecc71 !important;
}

.logout-link:hover {
  background-color: #fff1f1;
  color: #dc3545;
}
</style>