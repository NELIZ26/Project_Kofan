<script setup>
import { ref, computed } from "vue";
import Swal from "sweetalert2";

// 1. Datos simulados de reservas
const reservas = ref([
  {
    id: "RES-001",
    cliente: "Andrés Mendoza",
    habitacion: "Suite del Tucán",
    checkIn: "2024-03-10",
    checkOut: "2024-03-12",
    total: 500000,
    estado: "Confirmada",
  },
  {
    id: "RES-002",
    cliente: "Lucía Fernández",
    habitacion: "Cabaña del Río",
    checkIn: "2024-03-15",
    checkOut: "2024-03-20",
    total: 900000,
    estado: "Pendiente",
  },
  {
    id: "RES-003",
    cliente: "Mark Sullivan",
    habitacion: "Habitación Estándar",
    checkIn: "2024-03-05",
    checkOut: "2024-03-07",
    total: 300000,
    estado: "Cancelada",
  },
]);

// 2. Filtro de búsqueda
const filtro = ref("");

const reservasFiltradas = computed(() => {
  return reservas.value.filter(
    (res) =>
      res.cliente.toLowerCase().includes(filtro.value.toLowerCase()) ||
      res.id.toLowerCase().includes(filtro.value.toLowerCase()),
  );
});

// 3. Acciones
const actualizarEstado = (id, nuevoEstado) => {
  const res = reservas.value.find((r) => r.id === id);
  if (res) {
    res.estado = nuevoEstado;
    Swal.fire({
      title: "Estado Actualizado",
      text: `La reserva ahora está ${nuevoEstado}`,
      icon: "success",
      confirmButtonColor: "#0f3b2a",
    });
  }
};

const eliminarReserva = (id) => {
  Swal.fire({
    title: "¿Eliminar registro?",
    text: "Esta acción borrará la reserva del historial.",
    icon: "warning",
    showCancelButton: true,
    confirmButtonColor: "#d33",
    confirmButtonText: "Sí, borrar",
  }).then((result) => {
    if (result.isConfirmed) {
      reservas.value = reservas.value.filter((r) => r.id !== id);
    }
  });
};

// Helpers para colores
const getBadgeClass = (estado) => {
  switch (estado) {
    case "Confirmada":
      return "bg-success";
    case "Pendiente":
      return "bg-warning text-dark";
    case "Cancelada":
      return "bg-danger";
    default:
      return "bg-secondary";
  }
};
</script>

<template>
  <div class="bookings-manager">
    <div class="row g-3 mb-4">
      <div class="col-md-4">
        <div
          class="card border-0 shadow-sm p-3 border-start border-4 border-success rounded-4"
        >
          <div class="d-flex align-items-center">
            <div
              class="icon-box bg-success-subtle p-3 rounded-3 me-3 text-success"
            >
              <font-awesome-icon icon="fa-solid fa-calendar-check" size="lg" />
            </div>
            <div>
              <h6 class="text-muted mb-0">Confirmadas</h6>
              <h4 class="fw-bold mb-0">
                {{ reservas.filter((r) => r.estado === "Confirmada").length }}
              </h4>
            </div>
          </div>
        </div>
      </div>
      <div class="col-md-4">
        <div
          class="card border-0 shadow-sm p-3 border-start border-4 border-warning rounded-4"
        >
          <div class="d-flex align-items-center">
            <div
              class="icon-box bg-warning-subtle p-3 rounded-3 me-3 text-warning"
            >
              <font-awesome-icon icon="fa-solid fa-clock" size="lg" />
            </div>
            <div>
              <h6 class="text-muted mb-0">Pendientes</h6>
              <h4 class="fw-bold mb-0">
                {{ reservas.filter((r) => r.estado === "Pendiente").length }}
              </h4>
            </div>
          </div>
        </div>
      </div>
      <div class="col-md-4">
        <div
          class="card border-0 shadow-sm p-3 border-start border-4 border-primary rounded-4"
        >
          <div class="d-flex align-items-center">
            <div
              class="icon-box bg-primary-subtle p-3 rounded-3 me-3 text-primary"
            >
              <font-awesome-icon
                icon="fa-solid fa-hand-holding-dollar"
                size="lg"
              />
            </div>
            <div>
              <h6 class="text-muted mb-0">Ingresos Proyectados</h6>
              <h4 class="fw-bold mb-0">
                ${{
                  reservas.reduce((acc, r) => acc + r.total, 0).toLocaleString()
                }}
              </h4>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="card border-0 shadow-sm rounded-4 overflow-hidden">
      <div class="card-header bg-white p-3 border-0">
        <div class="input-group">
          <span class="input-group-text bg-light border-0"
            ><font-awesome-icon icon="fa-solid fa-magnifying-glass"
          /></span>
          <input
            v-model="filtro"
            type="text"
            class="form-control bg-light border-0"
            placeholder="Buscar por cliente o ID de reserva..."
          />
        </div>
      </div>

      <div class="table-responsive">
        <table class="table table-hover align-middle mb-0">
          <thead class="table-light">
            <tr>
              <th class="ps-4">ID / Cliente</th>
              <th>Habitación</th>
              <th>Fechas (In - Out)</th>
              <th>Total</th>
              <th>Estado</th>
              <th class="text-end pe-4">Acciones</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="res in reservasFiltradas" :key="res.id">
              <td class="ps-4">
                <div class="fw-bold">{{ res.id }}</div>
                <div class="small text-muted">{{ res.cliente }}</div>
              </td>
              <td>{{ res.habitacion }}</td>
              <td>
                <div class="small">
                  <span class="fw-bold">Entra:</span> {{ res.checkIn }}
                </div>
                <div class="small">
                  <span class="fw-bold">Sale:</span> {{ res.checkOut }}
                </div>
              </td>
              <td class="fw-bold text-success">
                ${{ res.total.toLocaleString() }}
              </td>
              <td>
                <span
                  :class="[
                    'badge rounded-pill px-3',
                    getBadgeClass(res.estado),
                  ]"
                >
                  {{ res.estado }}
                </span>
              </td>
              <td class="text-end pe-4">
                <div class="btn-group">
                  <button
                    class="btn btn-sm btn-light border"
                    @click="actualizarEstado(res.id, 'Confirmada')"
                    title="Confirmar"
                  >
                    <font-awesome-icon
                      icon="fa-solid fa-check"
                      class="text-success"
                    />
                  </button>
                  <button
                    class="btn btn-sm btn-light border"
                    @click="actualizarEstado(res.id, 'Cancelada')"
                    title="Cancelar"
                  >
                    <font-awesome-icon
                      icon="fa-solid fa-xmark"
                      class="text-danger"
                    />
                  </button>
                  <button
                    class="btn btn-sm btn-light border text-secondary"
                    @click="eliminarReserva(res.id)"
                  >
                    <font-awesome-icon icon="fa-solid fa-trash" />
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<style scoped>
.bg-success-subtle {
  background-color: #d1e7dd;
}
.bg-warning-subtle {
  background-color: #fff3cd;
}
.bg-primary-subtle {
  background-color: #cfe2ff;
}

.icon-box {
  width: 50px;
  height: 50px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.table thead th {
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.btn-group .btn:hover {
  background-color: #f8f9fa;
}
</style>
