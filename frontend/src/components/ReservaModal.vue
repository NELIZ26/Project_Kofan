<script setup>
import { useReservaStore } from "../stores/reserva.js";
// Asegúrate de tener 'leaf' y 'plus' en tu configuración de FontAwesome
const store = useReservaStore();
</script>

<template>
  <div
    class="modal-overlay"
    :class="{ active: store.isModalOpen }"
    @click.self="store.closeModal"
  >
    <div class="modal-card">
      <button class="btn-close-custom" @click="store.closeModal">
        <font-awesome-icon icon="plus" style="transform: rotate(45deg)" />
      </button>

      <div class="modal-body">
        <div class="text-center mb-4">
          <font-awesome-icon icon="leaf" class="verde-kofan mb-2 fs-4" />
          <h2 class="fw-bold verde-kofan">Reserva tu Experiencia</h2>
          <p class="text-muted small">
            Completa tus datos para vivir la magia del Putumayo
          </p>
        </div>

        <div class="tabs-kofan mb-4">
          <button
            type="button"
            class="tab-item"
            :class="{ active: store.personType === 'natural' }"
            @click="store.setPersonType('natural')"
          >
            Persona Natural
          </button>
          <button
            type="button"
            class="tab-item"
            :class="{ active: store.personType === 'juridica' }"
            @click="store.setPersonType('juridica')"
          >
            Empresa (Jurídica)
          </button>
        </div>

        <form @submit.prevent="store.handleSubmit" novalidate>
          <div class="row g-3">
            <div class="col-md-8">
              <label class="form-label-kofan">{{ store.labelNombres }}</label>
              <input
                type="text"
                class="input-kofan"
                v-model="store.form.nombres"
                :placeholder="store.placeholderNombres"
                :class="{ 'is-invalid': store.errors.nombres }"
              />
            </div>

            <div class="col-md-4" v-if="store.personType === 'natural'">
              <label class="form-label-kofan">Tipo Documento</label>
              <select
                class="input-kofan"
                v-model="store.form.tipoDocumento"
                :class="{ 'is-invalid': store.errors.tipoDocumento }"
              >
                <option value="" disabled>Seleccione...</option>
                <option value="CC">C.C.</option>
                <option value="CE">C.E.</option>
                <option value="PA">Pasaporte</option>
              </select>
            </div>

            <div class="col-md-6" v-if="store.personType === 'natural'">
              <label class="form-label-kofan">Fecha de Nacimiento</label>
              <input
                type="date"
                class="input-kofan"
                v-model="store.form.fechaNacimiento"
                :class="{ 'is-invalid': store.errors.fechaNacimiento }"
              />
            </div>

            <div class="col-md-6">
              <label class="form-label-kofan">Correo Electrónico</label>
              <input
                type="email"
                class="input-kofan"
                v-model="store.form.correo"
                placeholder="ejemplo@correo.com"
                :class="{ 'is-invalid': store.errors.correo }"
              />
            </div>

            <div class="col-md-6">
              <label class="form-label-kofan">{{ store.labelNumDoc }}</label>
              <input
                type="number"
                class="input-kofan"
                v-model="store.form.numDocumento"
                :class="{ 'is-invalid': store.errors.numDocumento }"
              />
            </div>

            <div class="col-md-4">
              <label class="form-label-kofan">Teléfono</label>
              <input
                type="tel"
                class="input-kofan"
                v-model="store.form.telefono"
                placeholder="300..."
                :class="{ 'is-invalid': store.errors.telefono }"
              />
            </div>

            <div class="col-md-4">
              <label class="form-label-kofan">Huéspedes</label>
              <select class="input-kofan" v-model="store.form.cantidadPersonas">
                <option value="1">1 Persona</option>
                <option value="2">2 Personas</option>
                <option value="3">3 Personas</option>
                <option value="4">4 Personas</option>
                <option value="5+">5+ Personas</option>
              </select>
            </div>

            <div class="col-md-4">
              <label class="form-label-kofan">Alojamiento</label>
              <select class="input-kofan" v-model="store.form.habitacion">
                <option value="Cabana2">Cabaña Individual</option>
                <option value="CabanaFamilia">Cabaña Familiar</option>
                <option value="Camping">Zona Camping</option>
              </select>
            </div>

            <div class="col-md-12">
              <label class="form-label-kofan"
                >Fecha de Ingreso (Check-In)</label
              >
              <input
                type="date"
                class="input-kofan"
                v-model="store.form.fechaReserva"
                :min="store.minDate"
                :class="{ 'is-invalid': store.errors.fechaReserva }"
              />
            </div>
          </div>

          <div class="text-center mt-5">
            <button type="submit" class="btn-kofan-confirm">
              Confirmar Reserva
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* Contenedor principal del modal */
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(15, 59, 42, 0.7);
  backdrop-filter: blur(8px);
  display: grid;
  place-items: center;
  z-index: 1050;
  opacity: 0;
  visibility: hidden;
  transition: all 0.3s ease;
}

.modal-overlay.active {
  opacity: 1;
  visibility: visible;
}

/* Tarjeta del modal */
.modal-card {
  background: white;
  width: 95%;
  max-width: 750px;
  border-radius: 25px;
  position: relative;
  overflow: hidden;
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
  animation: slideUp 0.4s ease-out;
}

@keyframes slideUp {
  from {
    transform: translateY(30px);
    opacity: 0;
  }
  to {
    transform: translateY(0);
    opacity: 1;
  }
}

.modal-body {
  padding: 3rem;
  max-height: 90vh;
  overflow-y: auto;
}

/* Estilos de las Pestañas (Tabs) */
.tabs-kofan {
  background: #f1f5f2;
  padding: 5px;
  border-radius: 15px;
  display: flex;
}

.tab-item {
  flex: 1;
  border: none;
  background: transparent;
  padding: 12px;
  border-radius: 12px;
  font-weight: 700;
  color: #666;
  transition: 0.3s;
}

.tab-item.active {
  background: white;
  color: #0f3b2a;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
}

/* Etiquetas y Campos de entrada */
.form-label-kofan {
  font-size: 0.8rem;
  font-weight: 700;
  color: #0f3b2a;
  margin-bottom: 6px;
  display: block;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.input-kofan {
  width: 100%;
  padding: 12px 15px;
  border: 1px solid #e0e0e0;
  border-radius: 12px;
  background: #fcfcfc;
  transition: all 0.3s ease;
}

.input-kofan:focus {
  outline: none;
  border-color: #2ecc71;
  background: white;
  box-shadow: 0 0 0 4px rgba(46, 204, 113, 0.1);
}

/* Estado de error */
.is-invalid {
  border-color: #e74c3c !important;
  background-color: #fff8f8;
}

.verde-kofan {
  color: #0f3b2a;
}

/* Botón de cierre superior */
.btn-close-custom {
  position: absolute;
  top: 20px;
  right: 20px;
  background: #f1f5f2;
  border: none;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  color: #0f3b2a;
  z-index: 10;
  transition: 0.3s;
  display: flex;
  align-items: center;
  justify-content: center;
}

.btn-close-custom:hover {
  background: #e74c3c;
  color: white;
  transform: rotate(90deg);
}

/* Botón Confirmar */
.btn-kofan-confirm {
  background: #0f3b2a;
  color: white;
  border: none;
  padding: 16px 60px;
  border-radius: 15px;
  font-weight: 700;
  font-size: 1.1rem;
  transition: all 0.3s ease;
  box-shadow: 0 10px 15px -3px rgba(15, 59, 42, 0.3);
}

.btn-kofan-confirm:hover {
  background: #1a5c43;
  transform: translateY(-2px);
  box-shadow: 0 20px 25px -5px rgba(15, 59, 42, 0.4);
}

/* Responsive */
@media (max-width: 768px) {
  .modal-body {
    padding: 1.5rem;
  }
  .btn-kofan-confirm {
    width: 100%;
  }
}
</style>
