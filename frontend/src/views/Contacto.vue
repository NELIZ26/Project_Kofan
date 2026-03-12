<template>
  <main class="contacto-page">
    <section
      class="contacto-hero text-center text-white d-flex align-items-center"
    >
      <div class="container">
        <h1 class="titulo-contacto">Estamos para escucharte</h1>
        <p class="lead">
          ¿Tienes dudas? Déjanos un mensaje y te responderemos con el alma
          amazónica.
        </p>
      </div>
    </section>

    <section class="info-formulario py-5">
      <div class="container">
        <div class="row g-5">
          <div class="col-lg-5">
            <div class="card-info-contacto p-4 h-100">
              <h2 class="mb-4">Información de Contacto</h2>

              <div class="dato-item d-flex align-items-center mb-4">
                <div class="icon-box me-3">
                  <font-awesome-icon :icon="['fas', 'location-dot']" />
                </div>
                <div>
                  <h5 class="mb-0">Ubicación</h5>
                  <p class="mb-0 text-muted">
                    Vereda Amacayacu, Puerto Asís, Putumayo.
                  </p>
                </div>
              </div>

              <div class="dato-item d-flex align-items-center mb-4">
                <div class="icon-box me-3">
                  <font-awesome-icon :icon="['fas', 'phone']" />
                </div>
                <div>
                  <h5 class="mb-0">Teléfono / WhatsApp</h5>
                  <p class="mb-0 text-muted">+57 300 000 0000</p>
                </div>
              </div>

              <div class="dato-item d-flex align-items-center mb-4">
                <div class="icon-box me-3">
                  <font-awesome-icon :icon="['fas', 'envelope']" />
                </div>
                <div>
                  <h5 class="mb-0">Correo Electrónico</h5>
                  <p class="mb-0 text-muted">info@ecohotelkofan.com</p>
                </div>
              </div>

              <hr class="my-4" />

              <h6>Síguenos en Redes</h6>
              <div class="d-flex gap-3 mt-3" id="socialMedia">
                <a
                  href="https://www.facebook.com/ecohotelkofan"
                  class="social-btn"
                  ><font-awesome-icon :icon="['fab', 'facebook-f']"
                /></a>
                <a
                  href="https://www.instagram.com/ecohotelkofan/"
                  class="social-btn"
                  ><font-awesome-icon :icon="['fab', 'instagram']"
                /></a>
                <a href="https://wa.link/gjt05p" class="social-btn"
                  ><font-awesome-icon :icon="['fab', 'whatsapp']"
                /></a>
              </div>
            </div>
          </div>

          <div class="col-lg-7">
            <div class="form-wrapper p-4">
              <h2 class="mb-4">Envíanos un mensaje</h2>
              <form @submit.prevent="enviarFormulario">
                <div class="row">
                  <div class="col-md-6 mb-3">
                    <label class="form-label">Nombre Completo</label>
                    <input
                      v-model="nombre"
                      type="text"
                      class="form-control custom-input"
                      placeholder="Tu nombre"
                      required
                    />
                  </div>
                  <div class="col-md-6 mb-3">
                    <label class="form-label">Correo Electrónico</label>
                    <input
                      v-model="email"
                      type="email"
                      class="form-control custom-input"
                      placeholder="correo@ejemplo.com"
                      required
                    />
                  </div>
                </div>
                <div class="mb-3">
                  <label class="form-label">Asunto</label>
                  <select v-model="asunto" class="form-select custom-input">
                    <option selected disabled>Selecciona una opción</option>
                    <option>Información de Reservas</option>
                    <option>Eventos y Grupos</option>
                    <option>Sugerencias</option>
                  </select>
                </div>
                <div class="mb-4">
                  <label class="form-label">Mensaje</label>
                  <textarea
                    v-model="mensaje"
                    class="form-control custom-input"
                    rows="5"
                    placeholder="Cuéntanos en qué podemos ayudarte..."
                  ></textarea>
                </div>
                <button type="submit" class="btn btn-kofan-submit w-100 py-3">
                  Enviar Mensaje
                </button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="mapa-section">
      <iframe
        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d31899.70461621379!2d-76.516666!3d0.5!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8e2f89366f68853f%3A0x8975a507a276b15e!2sPuerto%20As%C3%ADs%2C%20Putumayo!5e0!3m2!1ses!2sco!4v1700000000000!5m2!1ses!2sco"
        width="100%"
        height="450"
        style="border: 0"
        allowfullscreen
        loading="lazy"
      >
      </iframe>
    </section>
  </main>
</template>

<script>
export default {
  name: "Contacto",
  methods: {
    enviarFormulario() {
      // Handle form submission here
      console.log("Formulario enviado");
    },
  },
};
</script>

<style scoped>
.contacto-hero {
  background:
    linear-gradient(rgba(15, 59, 42, 0.7), rgba(15, 59, 42, 0.7)),
    url("../img/entradaKofan.jpg") center/cover;
  height: 40vh;
}

.titulo-contacto {
  font-family: "Handlee", cursive;
  font-size: 3.5rem;
}

.card-info-contacto {
  background: #1a5c43;
  color: white;
  border-radius: 30px;
}

.icon-box {
  width: 50px;
  height: 50px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.2rem;
  color: #2ecc71;
}

h6 {
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 1.2rem;
}
#socialMedia {
  display: flex;
  justify-content: center;
  align-items: center;

}

.social-btn {
  width: 40px;
  height: 40px;
  background: white;
  color: #0f3b2a;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  text-decoration: none;
  transition: all 0.3s ease;
}

.social-btn:hover {
  background: #2ecc71;
  color: white;
  transform: translateY(-3px);
}

.custom-input {
  border: 1px solid #dee2e6;
  padding: 12px;
  border-radius: 10px;
  transition: all 0.3s;
  resize: none; /* Evita que el usuario deforme el cuadro de texto */
}

.custom-input:focus {
  border-color: #0f3b2a;
  box-shadow: 0 0 0 0.25rem rgba(15, 59, 42, 0.1);
}

.btn-kofan-submit {
  background: #0f3b2a;
  color: white;
  border-radius: 10px;
  font-weight: 600;
  border: none;
  transition: background 0.3s;
}

.btn-kofan-submit:hover {
  background: #1a5c43;
}

@media (max-width: 768px) {
  .titulo-contacto {
    font-size: 2.5rem;
  }
}
</style>

<script setup>
import { ref } from "vue";
import Swal from "sweetalert2"; // Importamos la librería

// Creamos referencias para los campos (puedes añadir más)
const nombre = ref("");
const email = ref("");
const asunto = ref("Selecciona una opción");
const mensaje = ref("");

const enviarFormulario = () => {
  // Aquí iría tu lógica de envío a Firebase o API

  // Mostramos la alerta de éxito
  Swal.fire({
    title: "¡Mensaje Enviado!",
    text: "Gracias por contactarnos. En breve un guía Kofán se comunicará contigo.",
    icon: "success",
    confirmButtonColor: "#0f3b2a", // Tu verde institucional
    confirmButtonText: "Entendido",
    background: "#fffdfc",
    backdrop: `rgba(15,59,42,0.4)`, // Un fondo oscuro verdoso detrás de la alerta
  });

  // Limpiamos los campos después del envío
  nombre.value = "";
  email.value = "";
  mensaje.value = "";
  asunto.value = "Selecciona una opción";
};
</script>
