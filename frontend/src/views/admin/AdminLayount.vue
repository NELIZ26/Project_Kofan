<script setup>
import { useAuthStore } from "@/stores/auth";
import AdminHeader from "./AdminHeader.vue"; // Asegúrate de que la ruta sea correcta
import { useRouter } from "vue-router";

const auth = useAuthStore();
const router = useRouter();

const handleLogout = () => {
  auth.logout();
  router.push("/login");
};
</script>

<template>
  <div class="admin-wrapper d-flex">
    <aside class="admin-sidebar bg-dark text-white p-3 shadow">
      <div class="text-center mb-4">
        <img src="@/img/Kofan.png" width="100" alt="Logo" class="filter-white" />
        <h5 class="mt-2 fw-bold text-success">Kofán Admin</h5>
      </div>

      <nav class="nav flex-column gap-2">
        <router-link :to="{ name: 'admin-stats' }" class="nav-link-admin">
          <i class="fa fa-chart-line me-2"></i> <span>Estadísticas</span>
        </router-link>
        <router-link :to="{ name: 'admin-rooms' }" class="nav-link-admin">
          <i class="fa fa-bed me-2"></i> <span>Habitaciones</span>
        </router-link>
        <router-link :to="{ name: 'admin-users' }" class="nav-link-admin">
          <i class="fa fa-users me-2"></i> <span>Usuarios</span>
        </router-link>
        <router-link :to="{ name: 'admin-bookings' }" class="nav-link-admin">
          <i class="fa fa-calendar-check me-2"></i> <span>Reservas</span>
        </router-link>
        <router-link :to="{ name: 'admin-gallery' }" class="nav-link-admin">
          <i class="fa fa-images me-2"></i> <span>Galería</span>
        </router-link>
        
        <hr class="border-secondary opacity-25">
        
        <button @click="handleLogout" class="btn btn-outline-danger w-100 mt-2 border-0 shadow-sm">
          <i class="fa fa-sign-out-alt me-2"></i> <span>Salir</span>
        </button>
      </nav>
    </aside>

    <div class="main-container flex-grow-1 bg-light">
      <AdminHeader />
      
      <main class="p-4">
        <div class="d-flex justify-content-between align-items-center mb-4">
           <h3 class="text-dark fw-bold text-capitalize">
             {{ $route.name?.replace('admin-', '') }}
           </h3>
        </div>

        <router-view></router-view> 
      </main>
    </div>
  </div>
</template>

<style scoped>
.admin-wrapper {
  min-height: 100vh;
  background-color: #f8f9fa;
}

.admin-sidebar {
  width: 260px;
  min-height: 100vh;
  position: sticky;
  top: 0;
  z-index: 1000;
}

.main-container {
  display: flex;
  flex-direction: column;
}

.nav-link-admin {
  color: #adb5bd;
  text-decoration: none;
  padding: 12px 15px;
  border-radius: 10px;
  transition: all 0.3s ease;
  font-weight: 500;
}

.nav-link-admin:hover {
  background: rgba(46, 204, 113, 0.1);
  color: #2ecc71;
}

.router-link-active {
  background: #0f3b2a !important;
  color: white !important;
  box-shadow: 0 4px 12px rgba(15, 59, 42, 0.3);
}



@media (max-width: 768px) {
  .admin-sidebar {
    width: 85px;
  }
  .admin-sidebar span, .admin-sidebar h5 {
    display: none;
  }
  .nav-link-admin {
    text-align: center;
    padding: 15px;
  }
  .nav-link-admin i {
    margin: 0 !important;
    font-size: 1.2rem;
  }
}
</style>