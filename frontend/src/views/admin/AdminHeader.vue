<script setup>
import { useAuthStore } from "@/stores/auth";
import { useRouter } from "vue-router";
import Swal from 'sweetalert2';

const auth = useAuthStore();
const router = useRouter();

const handleLogout = () => {
  Swal.fire({
    title: '¿Cerrar sesión?',
    text: "Volverás a la página de inicio.",
    icon: 'question',
    showCancelButton: true,
    confirmButtonColor: '#0f3b2a',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Sí, salir',
    cancelButtonText: 'Cancelar'
  }).then((result) => {
    if (result.isConfirmed) {
      auth.logout();
      router.push("/home");
    }
  });
};
</script>

<template>
  <header class="admin-header bg-white shadow-sm d-flex align-items-center justify-content-between px-4">
    <div class="header-left d-flex align-items-center">
      <button class="btn btn-light d-md-none me-2">
        <i class="fa fa-bars"></i>
      </button>
      <h5 class="mb-0 text-secondary fw-bold">
        <i class="fa fa-tachometer-alt me-2 text-success"></i>
        Panel de Control
      </h5>
    </div>

    <div class="header-right d-flex align-items-center gap-3">
      <div class="user-profile d-none d-sm-flex align-items-center">
        <div class="user-info text-end me-2">
          <p class="mb-0 fw-bold lh-1">{{ auth.user?.nombre }}</p>
          <small class="text-muted">Administrador</small>
        </div>
        <div class="avatar-circle">
          {{ auth.user?.nombre?.charAt(0) }}
        </div>
      </div>
      
      <div class="vertical-divider"></div>

      <button @click="handleLogout" class="btn btn-outline-danger btn-sm rounded-pill px-3">
        <i class="fa fa-sign-out-alt me-1"></i> Salir
      </button>
    </div>
  </header>
</template>

<style scoped>
.admin-header {
  height: 70px;
  width: 100%;
  border-bottom: 1px solid #eee;
}

.avatar-circle {
  width: 40px;
  height: 40px;
  background-color: #0f3b2a;
  color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
}

.vertical-divider {
  width: 1px;
  height: 30px;
  background-color: #ddd;
  margin: 0 10px;
}

.lh-1 { line-height: 1; }
</style>