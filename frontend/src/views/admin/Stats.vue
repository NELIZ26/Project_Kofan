<script setup>
import { ref } from 'vue';

// Datos simulados para las estadísticas
const stats = ref({
  ingresosMes: 4500000,
  reservasActivas: 12,
  huespedesHoy: 8,
  ocupacionPorcentaje: 75
});

const habitacionesPopulares = ref([
  { nombre: 'Suite del Tucán', reservas: 45, ingresos: 1200000, color: 'success' },
  { nombre: 'Cabaña del Río', reservas: 32, ingresos: 850000, color: 'primary' },
  { nombre: 'Zona Camping', reservas: 15, ingresos: 300000, color: 'warning' },
]);

const ultimosMovimientos = ref([
  { id: 1, usuario: 'Carlos Ruiz', accion: 'Nueva Reserva', fecha: 'Hace 10 min', monto: '+ $250.000' },
  { id: 2, usuario: 'Marta Kofán', accion: 'Check-out', fecha: 'Hace 1 hora', monto: 'Finalizado' },
  { id: 3, usuario: 'Elena Gómez', accion: 'Cancelación', fecha: 'Hace 3 horas', monto: '- $150.000' },
]);
</script>

<template>
  <div class="admin-dashboard">
    <div class="row g-4 mb-4">
      <div class="col-md-3">
        <div class="card border-0 shadow-sm h-100 p-3 card-stat">
          <div class="d-flex justify-content-between">
            <div>
              <p class="text-muted small fw-bold mb-1 text-uppercase">Ingresos del Mes</p>
              <h3 class="fw-bold mb-0">${{ stats.ingresosMes.toLocaleString() }}</h3>
            </div>
            <div class="icon-circle bg-success-subtle text-success">
              <font-awesome-icon icon="fa-solid fa-hand-holding-dollar" />
            </div>
          </div>
          <div class="mt-3 small">
            <span class="text-success fw-bold"><font-awesome-icon icon="fa-solid fa-arrow-up" /> 12%</span>
            <span class="text-muted ms-2">vs mes anterior</span>
          </div>
        </div>
      </div>

      <div class="col-md-3">
        <div class="card border-0 shadow-sm h-100 p-3 card-stat">
          <div class="d-flex justify-content-between">
            <div>
              <p class="text-muted small fw-bold mb-1 text-uppercase">Reservas Activas</p>
              <h3 class="fw-bold mb-0">{{ stats.reservasActivas }}</h3>
            </div>
            <div class="icon-circle bg-primary-subtle text-primary">
              <font-awesome-icon icon="fa-solid fa-calendar-check" />
            </div>
          </div>
          <div class="mt-3 small text-muted">
            Proximas 7 días
          </div>
        </div>
      </div>

      <div class="col-md-3">
        <div class="card border-0 shadow-sm h-100 p-3 card-stat">
          <div class="d-flex justify-content-between">
            <div>
              <p class="text-muted small fw-bold mb-1 text-uppercase">Huéspedes Hoy</p>
              <h3 class="fw-bold mb-0">{{ stats.huespedesHoy }}</h3>
            </div>
            <div class="icon-circle bg-warning-subtle text-warning">
              <font-awesome-icon icon="fa-solid fa-users" />
            </div>
          </div>
          <div class="mt-3 small text-muted">
            En las instalaciones
          </div>
        </div>
      </div>

      <div class="col-md-3">
        <div class="card border-0 shadow-sm h-100 p-3 card-stat text-white bg-dark">
          <div class="d-flex justify-content-between">
            <div>
              <p class="text-light opacity-75 small fw-bold mb-1 text-uppercase">Ocupación</p>
              <h3 class="fw-bold mb-0">{{ stats.ocupacionPorcentaje }}%</h3>
            </div>
            <div class="icon-circle bg-white text-dark">
              <font-awesome-icon icon="fa-solid fa-bed" />
            </div>
          </div>
          <div class="progress mt-3" style="height: 6px;">
            <div class="progress-bar bg-success" :style="{ width: stats.ocupacionPorcentaje + '%' }"></div>
          </div>
        </div>
      </div>
    </div>

    <div class="row g-4">
      <div class="col-lg-8">
        <div class="card border-0 shadow-sm rounded-4 p-4">
          <h5 class="fw-bold mb-4">Habitaciones más solicitadas</h5>
          <div v-for="hab in habitacionesPopulares" :key="hab.nombre" class="mb-4">
            <div class="d-flex justify-content-between mb-1">
              <span class="fw-bold">{{ hab.nombre }}</span>
              <span class="text-muted small">{{ hab.reservas }} reservas</span>
            </div>
            <div class="progress" style="height: 10px;">
              <div 
                :class="['progress-bar', 'bg-' + hab.color]" 
                :style="{ width: (hab.reservas * 2) + '%' }"
              ></div>
            </div>
          </div>
        </div>
      </div>

      <div class="col-lg-4">
        <div class="card border-0 shadow-sm rounded-4 p-4">
          <h5 class="fw-bold mb-4">Actividad Reciente</h5>
          <div v-for="item in ultimosMovimientos" :key="item.id" class="d-flex mb-3 align-items-center">
            <div class="activity-dot me-3" :class="item.accion === 'Cancelación' ? 'bg-danger' : 'bg-success'"></div>
            <div class="flex-grow-1">
              <h6 class="mb-0 fw-bold small">{{ item.usuario }}</h6>
              <p class="mb-0 text-muted extra-small">{{ item.accion }} - {{ item.fecha }}</p>
            </div>
            <div class="fw-bold small">{{ item.monto }}</div>
          </div>
          <button class="btn btn-light btn-sm w-100 mt-2 fw-bold text-muted">Ver todo el historial</button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.card-stat {
  border-radius: 18px;
  transition: transform 0.3s ease;
}

.card-stat:hover {
  transform: translateY(-5px);
}

.icon-circle {
  width: 45px;
  height: 45px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.2rem;
}

.activity-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
}

.extra-small {
  font-size: 0.75rem;
}

.rounded-4 {
  border-radius: 1.25rem;
}

.bg-success-subtle { background-color: #d1e7dd; }
.bg-primary-subtle { background-color: #cfe2ff; }
.bg-warning-subtle { background-color: #fff3cd; }
</style>