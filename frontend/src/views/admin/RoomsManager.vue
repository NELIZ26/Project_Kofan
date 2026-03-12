<script setup>
import { ref } from "vue";
import Swal from "sweetalert2";

// 1. Estado de la lista (Simulación de base de datos)
const habitaciones = ref([
  {
    id: 1,
    nombre: "Suite del Tucán",
    precio: 250000,
    capacidad: 2,
    estado: "Disponible",
  },
  {
    id: 2,
    nombre: "Cabaña del Río",
    precio: 180000,
    capacidad: 4,
    estado: "Mantenimiento",
  },
]);

// 2. Estado para el formulario del Modal
const nuevaHab = ref({
  nombre: "",
  precio: "",
  capacidad: 1,
  descripcion: "",
  imagen: null,
});

// 3. Funciones de Lógica
const guardarHabitacion = () => {
  if (!nuevaHab.value.nombre || !nuevaHab.value.precio) {
    Swal.fire({
      icon: "error",
      title: "Campos incompletos",
      text: "Por favor, asigne un nombre y un precio a la habitación.",
      confirmButtonColor: "#0f3b2a",
    });
    return;
  }

  // Agregamos a la lista localmente
  habitaciones.value.push({
    id: Date.now(),
    ...nuevaHab.value,
    estado: "Disponible",
  });

  Swal.fire({
    icon: "success",
    title: "¡Habitación Creada!",
    text: "Se ha registrado correctamente en el sistema.",
    timer: 2000,
    showConfirmButton: false,
  });

  // Limpiar y el modal se cierra por el data-bs-dismiss del botón o manualmente
  resetForm();
};

const resetForm = () => {
  nuevaHab.value = {
    nombre: "",
    precio: "",
    capacidad: 1,
    descripcion: "",
    imagen: null,
  };
};

const eliminarHabitacion = (id) => {
  Swal.fire({
    title: "¿Estás seguro?",
    text: "Esta acción no se puede deshacer.",
    icon: "warning",
    showCancelButton: true,
    confirmButtonColor: "#d33",
    cancelButtonColor: "#0f3b2a",
    confirmButtonText: "Sí, eliminar",
    cancelButtonText: "Cancelar",
  }).then((result) => {
    if (result.isConfirmed) {
      habitaciones.value = habitaciones.value.filter((h) => h.id !== id);
      Swal.fire("Eliminado", "La habitación ha sido borrada.", "success");
    }
  });
};
</script>

<template>
  <div class="rooms-manager">
    <div class="d-flex justify-content-between align-items-center mb-4">
      <div>
        <h4 class="fw-bold mb-1">Gestión de Habitaciones</h4>
        <p class="text-muted small">
          Crea y administra el inventario de hospedaje.
        </p>
      </div>
      <button
        class="btn btn-kofan shadow-sm"
        data-bs-toggle="modal"
        data-bs-target="#modalHabitacion"
      >
        <font-awesome-icon icon="fa-solid fa-plus" class="me-2" />
        Nueva Habitación
      </button>
    </div>

    <div class="card border-0 shadow-sm rounded-4">
      <div class="table-responsive p-3">
        <table class="table table-hover align-middle">
          <thead class="table-light">
            <tr>
              <th>Nombre</th>
              <th>Precio/Noche</th>
              <th>Capacidad</th>
              <th>Estado</th>
              <th class="text-end">Acciones</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="hab in habitaciones" :key="hab.id">
              <td class="fw-bold text-dark">{{ hab.nombre }}</td>
              <td>${{ hab.precio.toLocaleString() }}</td>
              <td>
                <font-awesome-icon
                  icon="fa-solid fa-user"
                  class="me-1 text-muted"
                />
                {{ hab.capacidad }} pers.
              </td>
              <td>
                <span
                  :class="[
                    'badge rounded-pill',
                    hab.estado === 'Disponible'
                      ? 'bg-success-subtle text-success'
                      : 'bg-warning-subtle text-warning',
                  ]"
                >
                  {{ hab.estado }}
                </span>
              </td>
              <td class="text-end">
                <button class="btn btn-sm btn-light border me-2" title="Editar">
                  <font-awesome-icon
                    icon="fa-solid fa-pen-to-square"
                    class="text-primary"
                  />
                </button>
                <button
                  @click="eliminarHabitacion(hab.id)"
                  class="btn btn-sm btn-light border"
                  title="Eliminar"
                >
                  <font-awesome-icon
                    icon="fa-solid fa-trash"
                    class="text-danger"
                  />
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <div
      class="modal fade"
      id="modalHabitacion"
      tabindex="-1"
      aria-hidden="true"
    >
      <div class="modal-dialog modal-dialog-centered modal-lg">
        <div class="modal-content border-0 shadow-lg">
          <div class="modal-header bg-dark text-white border-0">
            <h5 class="modal-title fw-bold">
              <font-awesome-icon icon="fa-solid fa-bed" class="me-2" />
              Registrar Habitación
            </h5>
            <button
              type="button"
              class="btn-close btn-close-white"
              data-bs-dismiss="modal"
              aria-label="Close"
              @click="resetForm"
            ></button>
          </div>

          <form @submit.prevent="guardarHabitacion">
            <div class="modal-body p-4">
              <div class="row g-3">
                <div class="col-md-8">
                  <label class="form-label fw-bold"
                    >Nombre de la Habitación</label
                  >
                  <input
                    v-model="nuevaHab.nombre"
                    type="text"
                    class="form-control"
                    placeholder="Ej: Suite del Bosque"
                    required
                  />
                </div>
                <div class="col-md-4">
                  <label class="form-label fw-bold">Precio</label>
                  <div class="input-group">
                    <span class="input-group-text">$</span>
                    <input
                      v-model="nuevaHab.precio"
                      type="number"
                      class="form-control"
                      placeholder="0"
                      required
                    />
                  </div>
                </div>
                <div class="col-md-6">
                  <label class="form-label fw-bold">Capacidad Máxima</label>
                  <select v-model="nuevaHab.capacidad" class="form-select">
                    <option v-for="n in 6" :key="n" :value="n">
                      {{ n }} Persona(s)
                    </option>
                  </select>
                </div>
                <div class="col-md-6">
                  <label class="form-label fw-bold">Foto Principal</label>
                  <input type="file" class="form-control" accept="image/*" />
                </div>
                <div class="col-12">
                  <label class="form-label fw-bold"
                    >Descripción / Amenidades</label
                  >
                  <textarea
                    v-model="nuevaHab.descripcion"
                    class="form-control"
                    rows="3"
                    placeholder="Ej: Cama King, Wi-Fi, Vista al río..."
                  ></textarea>
                </div>
              </div>
            </div>

            <div class="modal-footer border-0 p-4 pt-0">
              <button
                type="button"
                class="btn btn-light px-4"
                data-bs-dismiss="modal"
                @click="resetForm"
              >
                Cancelar
              </button>
              <button
                type="submit"
                class="btn btn-kofan px-4"
                data-bs-dismiss="modal"
              >
                Guardar Habitación
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.btn-kofan {
  background-color: #0f3b2a;
  color: white;
  border-radius: 10px;
  font-weight: 500;
  transition: 0.3s;
}

.btn-kofan:hover {
  background-color: #1a5c43;
  color: white;
  transform: translateY(-2px);
}

.card {
  border-radius: 20px;
}

.table thead th {
  font-size: 0.8rem;
  text-transform: uppercase;
  color: #6c757d;
  letter-spacing: 0.5px;
}

.bg-success-subtle {
  background-color: #d1e7dd;
}
.bg-warning-subtle {
  background-color: #fff3cd;
}
</style>
