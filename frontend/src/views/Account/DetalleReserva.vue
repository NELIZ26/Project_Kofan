<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();

// Datos de ejemplo de la reserva seleccionada
const detalleReserva = ref({
  id: "RES-2026-001",
  alojamiento: "Cabaña del Bosque #2",
  tipo: "Cabaña Superior - 2 Personas",
  checkIn: "20/03/2026",
  checkOut: "25/03/2026",
  estado: "ACEPTADA",
  totalPagado: "$850.000 COP",
  huespedes: [
    { nombre: "Nelson Contreras", documento: "1098XXXXXX", rol: "Titular" },
    { nombre: "Mishel Otaiza", documento: "1065XXXXXX", rol: "Acompañante" },
  ],
  serviciosIncluidos: [
    "Desayuno Amazónico",
    "Acceso a Senderos",
    "Wifi en áreas comunes",
  ],
});

const volver = () => router.back();
</script>

<template>
  <div class="detalle-wrapper">
    <button @click="volver" class="btn btn-link text-success mb-3 p-0 fw-bold">
      <font-awesome-icon icon="arrow-left" class="me-2" /> Volver a mis reservas
    </button>

    <div class="card shadow-sm border-0 rounded-4 overflow-hidden">
      <div
        class="header-detalle p-4 text-white d-flex justify-content-between align-items-center"
      >
        <div>
          <span class="badge bg-white text-success mb-2"
            >Reserva {{ detalleReserva.id }}</span
          >
          <h2 class="fw-bold mb-0">{{ detalleReserva.alojamiento }}</h2>
        </div>
        <div class="text-end">
          <div class="status-pill-detalle">{{ detalleReserva.estado }}</div>
        </div>
      </div>

      <div class="card-body p-4">
        <div class="row g-4">
          <div class="col-md-6 border-end">
            <h5 class="fw-bold verde-kofan mb-4">
              Información del Alojamiento
            </h5>

            <div class="info-item mb-3">
              <label class="text-muted small d-block">Tipo de Habitación</label>
              <span class="fw-semibold">{{ detalleReserva.tipo }}</span>
            </div>

            <div class="row mb-3">
              <div class="col-6">
                <label class="text-muted small d-block">Fecha de Entrada</label>
                <span class="fw-semibold text-success">{{
                  detalleReserva.checkIn
                }}</span>
              </div>
              <div class="col-6">
                <label class="text-muted small d-block">Fecha de Salida</label>
                <span class="fw-semibold text-danger">{{
                  detalleReserva.checkOut
                }}</span>
              </div>
            </div>

            <div class="mb-3">
              <label class="text-muted small d-block"
                >Servicios Incluidos</label
              >
              <div class="d-flex flex-wrap gap-2 mt-2">
                <span
                  v-for="serv in detalleReserva.serviciosIncluidos"
                  :key="serv"
                  class="badge-servicio"
                >
                  {{ serv }}
                </span>
              </div>
            </div>
          </div>

          <div class="col-md-6">
            <h5 class="fw-bold verde-kofan mb-4">Huéspedes Registrados</h5>

            <div
              v-for="huesped in detalleReserva.huespedes"
              :key="huesped.documento"
              class="huesped-card p-3 mb-2 rounded-3 border"
            >
              <div class="d-flex align-items-center">
                <div class="huesped-icon me-3">
                  <font-awesome-icon icon="user" />
                </div>
                <div>
                  <div class="fw-bold mb-0">{{ huesped.nombre }}</div>
                  <small class="text-muted"
                    >{{ huesped.rol }} • {{ huesped.documento }}</small
                  >
                </div>
              </div>
            </div>

            <div class="mt-4 p-3 bg-light rounded-3">
              <div class="d-flex justify-content-between align-items-center">
                <span class="fw-bold">Total de la estancia:</span>
                <span class="fs-5 fw-bold verde-kofan">{{
                  detalleReserva.totalPagado
                }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div
        class="card-footer bg-white p-3 d-flex justify-content-end gap-2 border-top-0"
      >
        <button class="btn btn-outline-secondary btn-sm">
          Descargar Comprobante
        </button>
        <button class="btn btn-kofan-primary btn-sm">
          Contactar con recepción
        </button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.verde-kofan {
  color: #0f3b2a;
}

.header-detalle {
  background: linear-gradient(135deg, #0f3b2a 0%, #1a5c43 100%);
}

.status-pill-detalle {
  background: rgba(255, 255, 255, 0.2);
  backdrop-filter: blur(5px);
  padding: 8px 20px;
  border-radius: 30px;
  font-weight: bold;
  font-size: 0.8rem;
  border: 1px solid rgba(255, 255, 255, 0.3);
}

.badge-servicio {
  background: #f0fdf4;
  color: #157347;
  padding: 5px 12px;
  border-radius: 8px;
  font-size: 0.75rem;
  border: 1px solid #dcfce7;
}

.huesped-card {
  transition: all 0.2s;
}
.huesped-card:hover {
  border-color: #2ecc71 !important;
  background-color: #f9fdfb;
}

.huesped-icon {
  width: 35px;
  height: 35px;
  background: #e9ecef;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  color: #0f3b2a;
}

.btn-kofan-primary {
  background-color: #0f3b2a;
  color: white;
  border: none;
  border-radius: 8px;
  font-weight: 600;
}
</style>
