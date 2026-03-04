<template>
  <main class="auth-page py-5">
    <div class="container d-flex justify-content-center">
      <div class="register-card shadow-lg row g-0">
        
        <div class="col-lg-4 d-none d-lg-block register-sidebar text-white p-4">
          <div class="h-100 d-flex flex-column justify-content-between">
            <div>
              <h2 class="handlee-font">Únete a la familia</h2>
              <p class="small">Regístrate para vivir experiencias únicas en el corazón del Putumayo.</p>
            </div>
            <img src="../img/Kofan.png" alt="Logo Kofán" class="img-fluid opacity-50">
          </div>
        </div>

        <div class="col-lg-8 p-4 p-md-5 bg-white">
          <div class="text-center mb-4">
            <h2 class="fw-bold verde-kofan">Crear Cuenta</h2>
            <div class="divider mx-auto"></div>
          </div>

          <form @submit.prevent="submit" class="row g-3">
            <div class="col-md-6">
              <label class="form-label fw-semibold">Tipo Persona</label>
              <select v-model="tipoPersona" class="form-select custom-input">
                <option value="">Seleccione...</option>
                <option value="natural">Natural</option>
                <option value="juridica">Jurídica</option>
              </select>
            </div>
            <div class="col-md-6">
              <label class="form-label fw-semibold">Nombre Completo</label>
              <input v-model="nombre" type="text" class="form-control custom-input" placeholder="Ej: Juan Pérez">
            </div>

            <div class="col-md-6">
              <label class="form-label fw-semibold">Tipo Documento</label>
              <select v-model="tipoDocumento" class="form-select custom-input">
                <option value="">Seleccione...</option>
                <option value="cc">Cédula de Ciudadanía</option>
                <option value="ce">Cédula Extranjera</option>
              </select>
            </div>
            <div class="col-md-6">
              <label class="form-label fw-semibold">Número Documento</label>
              <input v-model="documento" type="text" class="form-control custom-input" placeholder="12345678">
            </div>

            <div class="col-md-6">
              <label class="form-label fw-semibold">Correo Electrónico</label>
              <input v-model="email" type="email" class="form-control custom-input" placeholder="correo@ejemplo.com">
            </div>
            <div class="col-md-6">
              <label class="form-label fw-semibold">Teléfono</label>
              <input v-model="telefono" type="tel" class="form-control custom-input" placeholder="+57 3xx xxx xxxx">
            </div>

            <div class="col-12">
              <label class="form-label fw-semibold">Contraseña</label>
              <input v-model="password" type="password" class="form-control custom-input" placeholder="Min. 8 caracteres">
            </div>

            <div class="col-12 mt-4">
              <button class="btn btn-kofan w-100 py-3 shadow-sm">
                Completar Registro
              </button>
            </div>

            <div class="col-12 text-center mt-3">
              <p class="text-muted small">
                ¿Ya tienes una cuenta? 
                <router-link to="/login" class="verde-kofan fw-bold text-decoration-none">Inicia Sesión</router-link>
              </p>
            </div>
          </form>
        </div>
      </div>
    </div>
  </main>
</template>

<script setup>
import { ref } from "vue";
import { useAuthStore } from "../stores/auth"; // Importamos el cerebro de la sesión
import { useRouter } from "vue-router";
import Swal from "sweetalert2";

const auth = useAuthStore();
const router = useRouter();

// Referencias de los campos
const tipoPersona = ref("");
const nombre = ref("");
const tipoDocumento = ref("");
const documento = ref("");
const email = ref("");
const telefono = ref("");
const password = ref("");

const submit = async () => {
  // 1. Validación básica
  if (!nombre.value || !email.value || !password.value || !documento.value) {
    return Swal.fire("Atención", "Por favor completa los campos obligatorios", "warning");
  }

  try {
    // 2. Simulamos la creación del usuario (Aquí irá tu llamada a la API/Firebase)
    const newUser = {
      nombre: nombre.value,
      email: email.value,
      telefono: telefono.value,
      rol: 'cliente'
    };
    
    // Generamos un token ficticio para la sesión
    const mockToken = "token-generado-al-registrar-" + Math.random();

    // 3. ¡MAGIA! Iniciamos sesión automáticamente usando el Store
    auth.login(newUser, mockToken);

    // 4. Notificamos al usuario
    await Swal.fire({
      icon: "success",
      title: "¡Bienvenido a Kofán!",
      text: `Hola ${nombre.value}, tu cuenta ha sido creada con éxito.`,
      timer: 2500,
      showConfirmButton: false
    });

    // 5. Redirigimos al Home o al Perfil
    router.push("/home");

  } catch (error) {
    Swal.fire("Error", "No pudimos crear tu cuenta. Intenta de nuevo.", "error");
  }
};
</script>

<style scoped>
.auth-page {
  background-color: #f8f9fa;
  min-height: 100vh;
  padding-top: 100px; /* Espacio para el Navbar fijo */
  margin-top: 50px;
}

.register-card {
  max-width: 900px;
  width: 100%;
  border-radius: 25px;
  overflow: hidden;
  border: none;
}

.register-sidebar {
  background: linear-gradient(rgba(15, 59, 42, 0.85), rgba(15, 59, 42, 0.85)), 
              url('../img/fondo3.png') center/cover;
}

.verde-kofan {
  color: #0f3b2a;
}

.handlee-font {
  font-family: 'Handlee', cursive;
}

.divider {
  width: 50px;
  height: 4px;
  background-color: #2ecc71;
  border-radius: 2px;
}

.custom-input {
  border: 1px solid #e0e0e0;
  border-radius: 10px;
  padding: 10px 15px;
  background-color: #fdfdfd;
}

.custom-input:focus {
  border-color: #0f3b2a;
  box-shadow: 0 0 0 0.25rem rgba(15, 59, 42, 0.1);
}

.btn-kofan {
  background-color: #0f3b2a;
  color: white;
  border: none;
  border-radius: 12px;
  font-weight: 600;
  transition: all 0.3s ease;
}

.btn-kofan:hover {
  background-color: #1a5c43;
  transform: translateY(-2px);
}
</style>