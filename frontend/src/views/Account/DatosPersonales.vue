<script setup>
import { ref } from "vue";
import { useAuthStore } from "@/stores/auth";
import Swal from "sweetalert2";

const auth = useAuthStore();

// 1. Estado reactivo (Iniciamos con los datos del auth o vacíos)
const formData = ref({
  tipo_persona: "Natural",
  nombres_apellidos: auth.user?.nombre || "Nelson Contreras",
  nombre_empresa: "",
  tipo_documento: "CC",
  numero_documento: auth.user?.documento || "",
  correo: auth.user?.email || "nelson@gmail.com",
  fecha_nacimiento: "",
  telefono: auth.user?.telefono || "",
  direccion: ""
});

// 2. Función de guardado con SweetAlert2
const saveProfile = async () => {
  // Aquí simularíamos la petición al servidor
  console.log("Enviando a API:", formData.value);

  const result = await Swal.fire({
    title: '¿Confirmar cambios?',
    text: "Se actualizará tu información de perfil",
    icon: 'question',
    showCancelButton: true,
    confirmButtonColor: '#0f3b2a',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Sí, guardar',
    cancelButtonText: 'Cancelar'
  });

  if (result.isConfirmed) {
    Swal.fire({
      title: '¡Actualizado!',
      text: 'Tus datos se han guardado correctamente.',
      icon: 'success',
      confirmButtonColor: '#0f3b2a'
    });
  }
};
</script>

<template>
  <div class="perfil-section">
    <div class="d-flex justify-content-between align-items-center mb-4">
      <div>
        <h3 class="fw-bold verde-kofan mb-0">Mi Perfil</h3>
        <p class="text-muted small">
          {{ formData.tipo_persona === 'Natural' ? 'Gestiona tu información personal' : 'Datos de cuenta corporativa' }}
        </p>
      </div>
      <div class="badge-tipo shadow-sm">
        {{ formData.tipo_persona }}
      </div>
    </div>

    <form @submit.prevent="saveProfile" class="p-2">
      <div class="row g-4">
        <div class="col-md-6">
          <div class="mb-3">
            <label class="form-label fw-bold text-secondary small">Tipo de Persona</label>
            <select class="form-select kofan-input" v-model="formData.tipo_persona">
              <option value="Natural">Persona Natural</option>
              <option value="Jurídica">Persona Jurídica (Empresa)</option>
            </select>
          </div>

          <div class="mb-3">
            <label class="form-label fw-bold text-secondary small">
              {{ formData.tipo_persona === 'Natural' ? 'Nombres y Apellidos' : 'Razón Social / Empresa' }}
            </label>
            <input 
              v-if="formData.tipo_persona === 'Natural'" 
              type="text" class="form-control kofan-input" v-model="formData.nombres_apellidos"
              placeholder="Ej: Nelson Contreras"
            />
            <input 
              v-else 
              type="text" class="form-control kofan-input" v-model="formData.nombre_empresa"
              placeholder="Nombre de la empresa"
            />
          </div>

          <div class="mb-3">
            <label class="form-label fw-bold text-secondary small">Tipo de Documento</label>
            <select v-if="formData.tipo_persona === 'Natural'" class="form-select kofan-input" v-model="formData.tipo_documento">
              <option value="CC">Cédula de Ciudadanía</option>
              <option value="CE">Cédula de Extranjería</option>
              <option value="PASAPORTE">Pasaporte</option>
            </select>
            <input v-else type="text" class="form-control kofan-input" value="NIT" disabled />
          </div>

          <div class="mb-3">
            <label class="form-label fw-bold text-secondary small">
              {{ formData.tipo_persona === 'Natural' ? 'Número de Documento' : 'NIT' }}
            </label>
            <input type="text" class="form-control kofan-input" v-model="formData.numero_documento" placeholder="Número de identificación"/>
          </div>
        </div>

        <div class="col-md-6">
          <div class="mb-3" v-if="formData.tipo_persona === 'Natural'">
            <label class="form-label fw-bold text-secondary small">Fecha de Nacimiento</label>
            <input type="date" class="form-control kofan-input" v-model="formData.fecha_nacimiento" />
          </div>

          <div class="mb-3">
            <label class="form-label fw-bold text-secondary small">Correo Electrónico</label>
            <input type="email" class="form-control kofan-input" v-model="formData.correo" readonly />
            <small class="text-muted" style="font-size: 0.7rem;">El correo no se puede cambiar por seguridad.</small>
          </div>

          <div class="mb-3">
            <label class="form-label fw-bold text-secondary small">Teléfono de Contacto</label>
            <input type="text" class="form-control kofan-input" v-model="formData.telefono" placeholder="Ej: +57 310..."/>
          </div>

          <div class="mb-3">
            <label class="form-label fw-bold text-secondary small">Dirección de Residencia</label>
            <input type="text" class="form-control kofan-input" v-model="formData.direccion" placeholder="Calle, Carrera, Ciudad..."/>
          </div>

          <div class="mt-4 d-flex justify-content-end">
            <button type="submit" class="btn btn-kofan-primary px-5 shadow-sm">
              <font-awesome-icon icon="save" class="me-2" /> Guardar Cambios
            </button>
          </div>
        </div>
      </div>
    </form>
  </div>
</template>

<style scoped>
.verde-kofan { color: #0f3b2a; }

.badge-tipo {
  background-color: #f0fdf4;
  color: #157347;
  padding: 8px 16px;
  border-radius: 30px;
  font-size: 0.85rem;
  font-weight: 700;
  border: 1px solid #2ecc71;
}

.kofan-input {
  border-radius: 12px;
  border: 1px solid #e0e0e0;
  padding: 10px 15px;
  background-color: #fcfcfc;
  transition: all 0.3s ease;
}

.kofan-input:focus {
  border-color: #0f3b2a;
  box-shadow: 0 0 0 0.25rem rgba(15, 59, 42, 0.1);
  background-color: #fff;
}

.kofan-input[readonly] {
  background-color: #f4f4f4;
  cursor: not-allowed;
}

.btn-kofan-primary {
  background-color: #0f3b2a;
  color: white;
  border: none;
  border-radius: 12px;
  padding: 12px;
  font-weight: 600;
  transition: all 0.3s;
}

.btn-kofan-primary:hover {
  background-color: #1a5c43;
  transform: translateY(-2px);
}
</style>