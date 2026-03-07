<script setup>
import { ref } from "vue";
import Swal from "sweetalert2";

// 1. Lista de usuarios simulada (Luego vendrá de Firebase/DB)
const usuarios = ref([
  {
    id: 1,
    nombre: "Juan Pérez",
    email: "juan@gmail.com",
    rol: "Cliente",
    estado: "Activo",
  },
  {
    id: 2,
    nombre: "Marta Kofán",
    email: "marta.admin@kofan.com",
    rol: "Admin",
    estado: "Activo",
  },
  {
    id: 3,
    nombre: "Carlos Ruiz",
    email: "carlos@outlook.com",
    rol: "Empleado",
    estado: "Inactivo",
  },
]);

// 2. Estado para el nuevo usuario
const nuevoUsuario = ref({
  nombre: "",
  email: "",
  password: "",
  rol: "Cliente",
});

// 3. Funciones
const guardarUsuario = () => {
  if (
    !nuevoUsuario.value.nombre ||
    !nuevoUsuario.value.email ||
    !nuevoUsuario.value.password
  ) {
    Swal.fire("Error", "Todos los campos son obligatorios", "error");
    return;
  }

  // Simulación de guardado
  usuarios.value.push({
    id: Date.now(),
    ...nuevoUsuario.value,
    estado: "Activo",
  });

  Swal.fire({
    title: "¡Usuario Creado!",
    text: `Se ha registrado a ${nuevoUsuario.value.nombre} con éxito.`,
    icon: "success",
    confirmButtonColor: "#0f3b2a",
  });

  resetForm();
};

const resetForm = () => {
  nuevoUsuario.value = { nombre: "", email: "", password: "", rol: "Cliente" };
};

const cambiarEstado = (id) => {
  const user = usuarios.value.find((u) => u.id === id);
  if (user) {
    user.estado = user.estado === "Activo" ? "Inactivo" : "Activo";
  }
};
</script>

<template>
  <div class="users-manager">
    <div class="d-flex justify-content-between align-items-center mb-4">
      <div>
        <h4 class="fw-bold mb-1">Gestión de Usuarios</h4>
        <p class="text-muted small">
          Administra los accesos y roles de clientes y personal.
        </p>
      </div>
      <button
        class="btn btn-kofan shadow-sm"
        data-bs-toggle="modal"
        data-bs-target="#modalUsuario"
      >
        <font-awesome-icon icon="fa-solid fa-user-plus" class="me-2" />
        Nuevo Usuario
      </button>
    </div>

    <div class="card border-0 shadow-sm rounded-4">
      <div class="table-responsive p-3">
        <table class="table table-hover align-middle">
          <thead class="table-light">
            <tr>
              <th>Nombre</th>
              <th>Email</th>
              <th>Rol</th>
              <th>Estado</th>
              <th class="text-end">Acciones</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="user in usuarios" :key="user.id">
              <td class="fw-bold">{{ user.nombre }}</td>
              <td>{{ user.email }}</td>
              <td>
                <span class="badge bg-light text-dark border px-3">
                  <font-awesome-icon
                    :icon="
                      user.rol === 'Admin'
                        ? 'fa-solid fa-user-shield'
                        : 'fa-solid fa-user'
                    "
                    class="me-1 text-success"
                  />
                  {{ user.rol }}
                </span>
              </td>
              <td>
                <span
                  :class="[
                    'badge rounded-pill',
                    user.estado === 'Activo' ? 'bg-success' : 'bg-secondary',
                  ]"
                >
                  {{ user.estado }}
                </span>
              </td>
              <td class="text-end">
                <button
                  @click="cambiarEstado(user.id)"
                  class="btn btn-sm btn-light border me-2"
                  title="Cambiar Estado"
                >
                  <font-awesome-icon
                    icon="fa-solid fa-rotate"
                    :class="
                      user.estado === 'Activo' ? 'text-warning' : 'text-success'
                    "
                  />
                </button>
                <button class="btn btn-sm btn-light border" title="Eliminar">
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

    <div class="modal fade" id="modalUsuario" tabindex="-1" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content border-0 shadow-lg">
          <div class="modal-header bg-dark text-white border-0">
            <h5 class="modal-title fw-bold">
              <font-awesome-icon icon="fa-solid fa-id-card" class="me-2" />
              Registrar Nuevo Usuario
            </h5>
            <button
              type="button"
              class="btn-close btn-close-white"
              data-bs-dismiss="modal"
              aria-label="Close"
            ></button>
          </div>

          <form @submit.prevent="guardarUsuario">
            <div class="modal-body p-4">
              <div class="mb-3">
                <label class="form-label fw-bold">Nombre Completo</label>
                <input
                  v-model="nuevoUsuario.nombre"
                  type="text"
                  class="form-control shadow-sm"
                  placeholder="Ej: Juan Valdéz"
                  required
                />
              </div>
              <div class="mb-3">
                <label class="form-label fw-bold">Correo Electrónico</label>
                <input
                  v-model="nuevoUsuario.email"
                  type="email"
                  class="form-control shadow-sm"
                  placeholder="usuario@kofan.com"
                  required
                />
              </div>
              <div class="mb-3">
                <label class="form-label fw-bold">Contraseña Temporal</label>
                <input
                  v-model="nuevoUsuario.password"
                  type="password"
                  class="form-control shadow-sm"
                  placeholder="********"
                  required
                />
              </div>
              <div class="mb-0">
                <label class="form-label fw-bold">Rol en el Sistema</label>
                <select
                  v-model="nuevoUsuario.rol"
                  class="form-select shadow-sm"
                >
                  <option value="Cliente">Cliente (Huésped)</option>
                  <option value="Empleado">Empleado (Recepcionista)</option>
                  <option value="Admin">Administrador (Control Total)</option>
                </select>
              </div>
            </div>

            <div class="modal-footer border-0 p-4 pt-0">
              <button
                type="button"
                class="btn btn-light px-4"
                data-bs-dismiss="modal"
              >
                Cancelar
              </button>
              <button
                type="submit"
                class="btn btn-kofan px-4"
                data-bs-dismiss="modal"
              >
                Crear Cuenta
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
</style>
