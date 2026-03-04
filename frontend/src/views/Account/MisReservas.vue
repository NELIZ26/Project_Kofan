<script setup>
import { ref, computed, onMounted } from "vue";
import { useAuthStore } from "@/stores/auth";
import { useReservaStore } from "@/stores/reserva";
import Swal from "sweetalert2";

const auth = useAuthStore();
const resStore = useReservaStore();

// --- ESTADO (Variables Reactivas) ---
const checkInDate = ref("");
const checkOutDate = ref("");
const filtroEstado = ref("TODAS");

// Datos base (Simulando lo que vendría de una base de datos)
const reservas = ref([
  {
    id: 1,
    detalle: "Cabaña 2 personas",
    fechaReserva: "08/01/2025",
    checkIn: "2026-02-18",
    checkOut: "2026-02-20",
    estado: "ACEPTADA",
  },
  {
    id: 2,
    detalle: "Cabaña 2 personas",
    fechaReserva: "08/01/2025",
    checkIn: "2025-08-20",
    checkOut: "2025-08-25",
    estado: "PENDIENTE",
  },
  {
    id: 3,
    detalle: "Cabaña 2 personas",
    fechaReserva: "08/01/2025",
    checkIn: "2024-11-08",
    checkOut: "2024-11-10",
    estado: "CANCELADA",
  },
  {
    id: 4,
    detalle: "Cabaña 2 personas",
    fechaReserva: "08/01/2025",
    checkIn: "2025-08-20",
    checkOut: "2025-08-25",
    estado: "PENDIENTE",
  },
  {
    id: 5,
    detalle: "Cabaña 2 personas",
    fechaReserva: "08/01/2025",
    checkIn: "2025-08-20",
    checkOut: "2025-08-25",
    estado: "ACEPTADA",
  },
]);

// Copia reactiva para los filtros de fecha
const reservasFiltradas = ref([]);

// --- LÓGICA DE FILTRADO (Computed) ---
const listaVisual = computed(() => {
  if (filtroEstado.value === "TODAS") {
    return reservasFiltradas.value;
  }
  return reservasFiltradas.value.filter((r) => r.estado === filtroEstado.value);
});

const countAceptadas = computed(() => {
  return reservasFiltradas.value.filter((r) => r.estado === "ACEPTADA").length;
});

// --- MÉTODOS ---
onMounted(() => {
  // Inicializamos la lista con todos los datos al cargar
  reservasFiltradas.value = [...reservas.value];
});

const filtrarLista = () => {
  if (!checkInDate.value || !checkOutDate.value) {
    Swal.fire({
      icon: "warning",
      title: "Fechas incompletas",
      text: "Por favor selecciona un rango de inicio y fin.",
      confirmButtonColor: "#0f3b2a",
    });
    return;
  }

  const inicio = new Date(checkInDate.value);
  const fin = new Date(checkOutDate.value);

  reservasFiltradas.value = reservas.value.filter((reserva) => {
    const fechaIn = new Date(reserva.checkIn);
    return fechaIn >= inicio && fechaIn <= fin;
  });
};

const limpiarFiltros = () => {
  // Si no hay nada filtrado, no hacemos nada
  if (
    !checkInDate.value &&
    !checkOutDate.value &&
    filtroEstado.value === "TODAS"
  )
    return;

  checkInDate.value = "";
  checkOutDate.value = "";
  filtroEstado.value = "TODAS";
  reservasFiltradas.value = [...reservas.value];

  // Notificación tipo Toast (Elegante y rápida)
  const Toast = Swal.mixin({
    toast: true,
    position: "top-end",
    showConfirmButton: false,
    timer: 2000,
    timerProgressBar: true,
  });

  Toast.fire({
    icon: "success",
    title: "Filtros eliminados",
  });
};

const formatFecha = (fechaISO) => {
  if (!fechaISO) return "";
  const [year, month, day] = fechaISO.split("-");
  return `${day}/${month}/${year}`;
};

const getStatusClass = (estado) => {
  switch (estado) {
    case "ACEPTADA":
      return "status-aceptada";
    case "PENDIENTE":
      return "status-pendiente";
    case "CANCELADA":
      return "status-cancelada";
    default:
      return "";
  }
};
</script>

<template>
  <div class="reservas-container">
    <div class="d-flex justify-content-between align-items-center mb-4">
      <div>
        <h4 class="fw-bold verde-kofan mb-1">Gestión de Reservas</h4>
        <p class="text-muted mb-0 small">
          Titular:
          <span class="fw-bold text-dark">{{
            auth.user?.nombre || "Huésped"
          }}</span>
        </p>
      </div>
    </div>

    <div class="actions-card p-3 mb-4 shadow-sm border">
      <div class="row g-3 align-items-end">
        <div class="col-md-3">
          <label class="form-label small fw-bold text-secondary">Desde</label>
          <input
            type="date"
            v-model="checkInDate"
            class="form-control kofan-input"
          />
        </div>
        <div class="col-md-3">
          <label class="form-label small fw-bold text-secondary">Hasta</label>
          <input
            type="date"
            v-model="checkOutDate"
            class="form-control kofan-input"
          />
        </div>
        <div class="col-md-6 d-flex gap-2 justify-content-md-end mt-3">
          <button @click="filtrarLista" class="btn btn-kofan-secondary">
            <font-awesome-icon icon="filter" /> Filtrar
          </button>
          <button @click="limpiarFiltros" class="btn btn-outline-danger-kofan">
            <font-awesome-icon icon="trash-can" /> Limpiar
          </button>
          <button
            @click="resStore.openModal"
            class="btn btn-kofan-primary px-4"
          >
            Reservar Ahora
          </button>
        </div>
      </div>
    </div>

    <ul class="nav nav-tabs kofan-tabs mb-4">
      <li class="nav-item">
        <button
          class="nav-link"
          :class="{ active: filtroEstado === 'TODAS' }"
          @click="filtroEstado = 'TODAS'"
        >
          Todas ({{ reservasFiltradas.length }})
        </button>
      </li>
      <li class="nav-item">
        <button
          class="nav-link"
          :class="{ active: filtroEstado === 'ACEPTADA' }"
          @click="filtroEstado = 'ACEPTADA'"
        >
          Aceptadas
          <span class="badge bg-success ms-1">{{ countAceptadas }}</span>
        </button>
      </li>
      <li class="nav-item">
        <button
          class="nav-link"
          :class="{ active: filtroEstado === 'PENDIENTE' }"
          @click="filtroEstado = 'PENDIENTE'"
        >
          Pendientes
        </button>
      </li>
      <li class="nav-item">
        <button
          class="nav-link"
          :class="{ active: filtroEstado === 'CANCELADA' }"
          @click="filtroEstado = 'CANCELADA'"
        >
          Canceladas
        </button>
      </li>
    </ul>

    <div class="table-responsive rounded-3 border bg-white">
      <table class="table table-hover align-middle mb-0">
        <thead class="bg-light">
          <tr class="text-muted small">
            <th class="py-3 px-4">DETALLE DEL HOSPEDAJE</th>
            <th>REGISTRO</th>
            <th class="text-center">ESTANCIA (IN/OUT)</th>
            <th class="text-center">ESTADO</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="reserva in listaVisual"
            :key="reserva.id"
            class="reserva-row"
          >
            <td class="px-4">
              <router-link
                :to="{
                  name: 'account-reserva-detalle',
                  params: { id: reserva.id },
                }"
                class="text-decoration-none d-block clickable-reserva"
              >
                <div class="d-flex align-items-center">
                  <div class="icon-circle me-3">
                    <font-awesome-icon icon="hotel" class="text-success" />
                  </div>
                  <div>
                    <div class="fw-bold text-dark">{{ reserva.detalle }}</div>
                    <small class="text-muted"
                      ><font-awesome-icon icon="users" /> Huéspedes
                      Adultos</small
                    >
                  </div>
                </div>
              </router-link>
            </td>
            <td class="text-muted small">{{ reserva.fechaReserva }}</td>
            <td class="text-center small fw-semibold">
              {{ formatFecha(reserva.checkIn) }} <br />
              <span class="text-muted font-monospace">↓</span> <br />
              {{ formatFecha(reserva.checkOut) }}
            </td>
            <td class="text-center">
              <span :class="['status-pill', getStatusClass(reserva.estado)]">
                {{ reserva.estado }}
              </span>
            </td>
          </tr>

          <tr v-if="listaVisual.length === 0">
            <td colspan="4" class="text-center py-5 text-muted">
              <font-awesome-icon
                icon="magnifying-glass"
                class="fs-1 mb-3 d-block mx-auto"
              />
              <p>No se encontraron resultados con los filtros aplicados.</p>
              <button
                @click="limpiarFiltros"
                class="btn btn-sm btn-link text-success"
              >
                Ver todas las reservas
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<style scoped>
.verde-kofan {
  color: #0f3b2a;
}

/* Tarjeta de Filtros */
.actions-card {
  background-color: #ffffff;
  border-radius: 15px;
}

.kofan-input {
  border-radius: 10px;
  border: 1px solid #dee2e6;
  padding: 0.6rem;
  transition: 0.3s;
}

.kofan-input:focus {
  border-color: #2ecc71;
  box-shadow: 0 0 0 0.25rem rgba(46, 204, 113, 0.1);
}

/* Botones Personalizados */
.btn-kofan-primary {
  background-color: #0f3b2a;
  color: white;
  border-radius: 10px;
  font-weight: 600;
  border: none;
}
.btn-kofan-primary:hover {
  background-color: #1a5c43;
}

.btn-kofan-secondary {
  background-color: #2ecc71;
  color: white;
  border-radius: 10px;
  font-weight: 600;
  border: none;
}

.btn-outline-danger-kofan {
  border: 1px solid #ee6c4f;
  color: #ee6c4f;
  background: transparent;
  border-radius: 10px;
  font-weight: 600;
}
.btn-outline-danger-kofan:hover {
  background-color: #fff5f2;
  color: #d85d41;
}

/* Pestañas (Tabs) */
.kofan-tabs .nav-link {
  color: #777;
  border: none;
  border-bottom: 3px solid transparent;
  padding: 10px 20px;
  font-weight: 600;
  transition: 0.3s;
}
.kofan-tabs .nav-link.active {
  color: #0f3b2a;
  background: transparent;
  border-bottom: 3px solid #2ecc71;
}

/* Semáforo de Estados */
.status-pill {
  padding: 6px 14px;
  border-radius: 20px;
  font-size: 0.7rem;
  font-weight: 800;
  letter-spacing: 0.5px;
  display: inline-block;
  min-width: 100px;
}
.status-aceptada {
  background: #e0fdf0;
  color: #157347;
  border: 1px solid #157347;
}
.status-pendiente {
  background: #fff9db;
  color: #947100;
  border: 1px solid #947100;
}
.status-cancelada {
  background: #fff5f5;
  color: #c92a2a;
  border: 1px solid #c92a2a;
}

/* Otros */
.user-avatar {
  width: 45px;
  height: 45px;
  background: #0f3b2a;
  color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
}

.icon-circle {
  width: 38px;
  height: 38px;
  background: #f0fdf4;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.reserva-row {
  transition: background 0.2s;
}
.reserva-row:hover {
  background-color: #f9fbf9 !important;
}
</style>
