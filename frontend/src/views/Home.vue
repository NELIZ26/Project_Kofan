<script setup>
import { useReservaStore } from "@/stores/reserva";

const resStore = useReservaStore();
</script>

<template>
  <main>
    <section id="home">
      <section class="home-content">
        <h1>Descubre la magia de la Amazonía con Kofán</h1>
        <p>
          Kofán donde la selva y el espíritu se encuentran. Un lugar para
          reconectarte con la vida, rodeado del canto de las aves y el murmullo
          natural. Ya sea una escapada romántica o una aventura en familia,
          descubre una experiencia única en el corazón de la Amazonía.
        </p>
        <button @click="resStore.openModal" class="btn btn-primary">Explorar Destinos</button>
      </section>

      <section class="home-image">
        <img class="img" src="../img/portadaimg.png" alt="Casa Kofán" />
      </section>

      <div class="custom-shape-divider-bottom">
        <svg
          data-name="Layer 1"
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 1200 120"
          preserveAspectRatio="none"
        >
          <defs>
            <linearGradient
              id="miGradienteKofan"
              x1="100%"
              y1="0%"
              x2="110%"
              y2="0%"
            >
              <stop offset="0%" style="stop-color: #1a5c43; stop-opacity: 1" />

              <stop
                offset="100%"
                style="stop-color: #0f3b2a; stop-opacity: 1"
              />
            </linearGradient>
          </defs>

          <path
            d="M0,0V120H1200V0c-150,80-350,120-600,120S150,80,0,0Z"
            fill="url(#miGradienteKofan)"
          ></path>
        </svg>
      </div>
    </section>

    <section class="experiencias" id="experiencias">
      <div class="container">
        <div class="text-center mb-5">
          <span class="subtitulo">Vive lo Auténtico</span>
          <h2 class="titulo-seccion">
            Descubre la magia Kofán en cada detalle
          </h2>
          <p class="parfo-seccion">
            Diseñamos experiencias que conectan la esencia ancestral Kofán con
            el confort moderno, creando espacios donde la naturaleza, la cultura
            y el descanso se unen en perfecta armonía.
          </p>
        </div>

        <div class="grid-actividades">
          <div class="card-actividad">
            <div class="icono-wrapper">
              <font-awesome-icon icon="fa-solid fa-leaf" />
            </div>
            <h3>Senderismo</h3>
            <p>
              Camina por senderos sagrados y descubre la biodiversidad
              amazónica.
            </p>
          </div>

          <div class="card-actividad">
            <div class="icono-wrapper">
              <font-awesome-icon icon="fa-solid fa-hands-holding" />
            </div>
            <h3>Cultura Viva</h3>
            <p>
              Conéctate con las tradiciones y saberes de la comunidad Kofán.
            </p>
          </div>

          <div class="card-actividad">
            <div class="icono-wrapper">
              <font-awesome-icon icon="fa-solid fa-moon" />
            </div>
            <h3>Descanso Pleno</h3>
            <p>Habitaciones diseñadas para el bienestar físico y espiritual.</p>
          </div>
        </div>
      </div>

      <div class="custom-shape-divider-botto arco-transicion">
        <svg viewBox="0 0 1200 120" preserveAspectRatio="none">
          <path
            d="M0,0V120H1200V0c-150,80-350,120-600,120S150,80,0,0Z"
            fill="#fffdfc"
          ></path>
        </svg>
      </div>
    </section>

    <section class="servicios" id="servicios">
      <div class="text-center mb-5 w-100 container">
        <span class="subtitulo-blanco">Comodidad Ancestral</span>
        <h2 class="titulo-seccion-blanco">Espacios diseñados para el alma</h2>
      </div>

      <div class="kofan-cards-group">
        <div class="kofan-card-container">
          <div class="kofan-card-wrapper">
            <img
              class="kofan-card-image"
              src="../img/ancestral.jpg"
              alt="Hospedaje"
            />
            <div class="kofan-card-content">
              <h2 class="kofan-card-title">Hospedaje Ancestral</h2>
              <h3 class="kofan-card-subtitle">Confort Natural</h3>
              <p class="kofan-card-text">
                Disfruta de habitaciones diseñadas con materiales locales,
                ofreciendo una conexión directa con la selva.
              </p>
              <a href="#" class="kofan-card-more">Leer más</a>
              <div class="kofan-card-details">
                <span class="kofan-detail-item"
                  ><font-awesome-icon :icon="['fas', 'tag']" />
                  <em> Desde $120.000</em></span
                >
                <span class="kofan-detail-item"
                  ><font-awesome-icon :icon="['fas', 'bed']" />
                  <em> Doble/Simple</em></span
                >
              </div>
              <div class="kofan-card-actions">
                <button class="kofan-btn-primary">Ver Detalles</button>
                <button class="kofan-btn-icon">
                  <font-awesome-icon :icon="['fas', 'heart']" />
                </button>
              </div>
            </div>
          </div>
        </div>

        <div class="kofan-card-container">
          <div class="kofan-card-wrapper">
            <img
              class="kofan-card-image"
              src="../img/casa okfan.jpg"
              alt="Eventos"
            />
            <div class="kofan-card-content">
              <h2 class="kofan-card-title">Salón de Eventos</h2>
              <h3 class="kofan-card-subtitle">Espacios Inspiradores</h3>
              <p class="kofan-card-text">
                Un salón diseñado para eventos corporativos, bodas o talleres
                culturales en un entorno único.
              </p>
              <a href="#" class="kofan-card-more">Ver disponibilidad</a>
              <div class="kofan-card-details">
                <span class="kofan-detail-item"
                  ><font-awesome-icon :icon="['fas', 'users']" />
                  <em> Cap: 50 pers</em></span
                >
                <span class="kofan-detail-item"
                  ><font-awesome-icon :icon="['fas', 'wifi']" />
                  <em> Satelital</em></span
                >
              </div>
              <div class="kofan-card-actions">
                <button class="kofan-btn-primary">Cotizar Evento</button>
                <button class="kofan-btn-icon">
                  <font-awesome-icon :icon="['fas', 'calendar-check']" />
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="divisor-hacia-blanco">
        <svg viewBox="0 0 1200 120" preserveAspectRatio="none">
          <path
            d="M0,0V120H1200V0c-150,80-350,120-600,120S150,80,0,0Z"
            fill="#1a5c43"
          ></path>
        </svg>
      </div>
    </section>

    <section class="info-importante">
      <div class="container">
        <div class="info-grid">
          <div class="info-card shadow-soft">
            <div class="info-header">
              <font-awesome-icon
                icon="fa-solid fa-circle-info"
                class="info-icon"
              />
              <h3>Información Útil</h3>
            </div>
            <ul class="info-list">
              <li>
                <span class="check">✔</span>
                <strong>Check-in:&nbsp;</strong> 03:00 pm&nbsp;
                <strong> Check-out:&nbsp;</strong> 12:00 pm
              </li>
              <li>
                <span class="check">✔</span> Early Check-in sujeto a
                disponibilidad.
              </li>
              <li>
                <span class="cross">✘</span> No se permite el ingreso de comida
                ni bebidas.
              </li>
              <li>
                <span class="cross">✘</span> No se permite el uso de parlantes o
                ruidos fuertes.
              </li>
              <li>
                <span class="check">✔</span> Reserva con el&nbsp;
                <strong> 25% del valor</strong>.
              </li>
            </ul>
          </div>

          <div class="info-card shadow-soft">
            <div class="info-header">
              <font-awesome-icon
                icon="fa-solid fa-shield-halved"
                class="info-icon"
              />
              <h3>Políticas y Legal</h3>
            </div>
            <div class="info-text">
              <p>
                <strong>Menores de edad:</strong> Deben presentar documento de
                identidad y estar acompañados por sus padres (Ley 679 de 2001).
              </p>
              <p class="mt-2">
                <strong>Cancelaciones:</strong> No se realiza devolución de
                dinero. Puedes reprogramar hasta con 7 días de anticipación.
              </p>
            </div>
            <a
              href="https://wa.link/dtc3ys"
              target="_blank"
              class="btn-whatsapp"
            >
              <font-awesome-icon :icon="['fab', 'whatsapp']" /> ¿Tienes dudas?
              Escríbenos
            </a>
          </div>
        </div>
      </div>
      <div class="divisor-hacia-verde">
        <svg viewBox="0 0 1200 120" preserveAspectRatio="none">
          <path
            d="M0,0V120H1200V0c-150,80-350,120-600,120S150,80,0,0Z"
            fill="#fffdfc"
          ></path>
        </svg>
      </div>
    </section>

    <section class="ubicacion" id="donde-estamos">
      <div class="divisor-entrada-verde">
        <svg viewBox="0 0 1200 120" preserveAspectRatio="none">
          <path
            d="M0,0V120H1200V0c-150,80-350,120-600,120S150,80,0,0Z"
            fill="#1a5c43"
          ></path>
        </svg>
      </div>

      <div class="container">
        <div class="text-center mb-5">
          <span class="subtitulo-blanco">¿Cómo llegar?</span>
          <h2 class="titulo-seccion-blanco">
            Nuestra ubicación en el Putumayo
          </h2>
          <p class="parrafo-ubicacion">
            Nos encontramos en <strong>Puerto Asís, Putumayo</strong>. Un
            refugio natural donde la selva comienza a contar sus historias.
          </p>
        </div>

        <div class="mapa-wrapper shadow-soft">
          <iframe
            src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d15958.521652611322!2d-76.5355120619749!3d0.5560764129741063!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8e287e6540874957%3A0x9a11032de2a63510!2sCentro%20Ecoturistico%20Kofan!5e0!3m2!1ses!2sco!4v1762307375610!5m2!1ses!2sco"
            width="100%"
            height="450"
            style="border: 0"
            allowfullscreen
            loading="lazy"
            referrerpolicy="no-referrer-when-downgrade"
          >
          </iframe>
        </div>

        <div class="detalles-llegada">
          <div class="item-llegada">
            <font-awesome-icon icon="fa-solid fa-plane" class="icon-llegada" />
            <p>A solo 15 minutos del Aeropuerto 3 de Mayo.</p>
          </div>
          <div class="item-llegada">
            <font-awesome-icon icon="fa-solid fa-car" class="icon-llegada" />
            <p>Fácil acceso por vía principal con parqueadero privado.</p>
          </div>
        </div>
      </div>
    </section>
  </main>
</template>

<style scoped>
/* --- GLOBALES Y HOME --- */
#home {
  position: relative;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  gap: 30px;
  min-height: 90vh;
  padding: 110px 50px 100px 50px;
  background: linear-gradient(135deg, #0f3b2a 0%, #1a5c43 100%);
  overflow: hidden;
}

/* Contenedor del SVG */
.custom-shape-divider-bottom {
  position: absolute;
  bottom: -1px;
  left: -1px;
  right: -1px;
  width: 100%;
  overflow: hidden;
  line-height: 0;
  pointer-events: none;
  /* Evita que el SVG interfiera con los clics */
}

.custom-shape-divider-bottom svg {
  position: relative;
  display: block;
  width: 100%;
  height: 52px;
  /* Controla qué tan pronunciada es la curva */
  transform: rotate(180deg);
  /* Voltea la curva para que quede hacia abajo */
  background: #fffdfc;
  /* Asegura que el fondo del SVG sea transparente */
}

/* Contenedor del SVG - Experiecias*/
.custom-shape-divider-botto {
  position: absolute;
  bottom: -1px;
  left: -1px;
  right: -1px;
  width: 100%;
  overflow: hidden;
  line-height: 0;
  pointer-events: none;
  /* Evita que el SVG interfiera con los clics */
}

.custom-shape-divider-botto svg {
  position: relative;
  display: block;
  width: 100%;
  height: 52px;
  /* Controla qué tan pronunciada es la curva */
  transform: rotate(180deg);
  /* Voltea la curva para que quede hacia abajo */
  background: #1a5c43;
  /* Asegura que el fondo del SVG sea transparente */
}

.home-content {
  flex: 1;
  color: white;
  animation: slideInLeft 1.2s ease-out;
}

.home-content h1 {
  font-size: 3.5rem;
  font-family: "Handlee", cursive;
  font-weight: 700;
}

.home-image {
  flex: 1;
  display: flex;
  justify-content: center;
}

.img {
  max-width: 100%;
  max-height: 500px;
  border-radius: 20px;
  animation: float 6s ease-in-out infinite;
}

/* --- SECCIÓN EXPERIENCIAS --- */
.experiencias {
  position: relative;
  padding: 80px 20px 120px 20px;
  color: #2c3e50;
  background: #fffdfc;
}

.titulo-seccion {
  font-family: "Handlee", cursive;
  font-size: 2.8rem;
  color: #0f3b2a;
  margin: 15px 0;
}

.subtitulo {
  text-transform: uppercase;
  letter-spacing: 2px;
  color: #1a5c43;
  font-weight: 700;
}

.grid-actividades {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 30px;
  max-width: 1100px;
  margin: 0 auto;
}

.card-actividad {
  text-align: center;
  padding: 30px;
  transition: transform 0.3s ease;
}

.icono-wrapper {
  width: 80px;
  height: 80px;
  background-color: #f0f7f4;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 20px;
  color: #1a5c43;
  font-size: 2rem;
}

/* --- SECCIÓN SERVICIOS --- */
.servicios {
  position: relative;
  /* ESTO ES VITAL */
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 100px 20px 150px 20px;
  /* Dale mucho espacio abajo para que se vea */
  background: #1a5c43;
  color: white;
  z-index: 1;
  /* Crea un contexto de apilamiento */
}

/* --- EL DIVISOR / SERVICIOS --- */
.divisor-hacia-blanco {
  position: absolute;
  bottom: -1px;
  /* Un pequeño margen negativo para evitar líneas blancas */
  left: -1px;
  right: -1px;
  width: 100%;
  line-height: 0;
  z-index: 1;
  /* Forzamos que esté al frente */
  pointer-events: none;
  /* Para que no bloquee clics en botones cercanos */
}

.divisor-hacia-blanco svg {
  position: relative;
  display: block;
  width: 100%;
  height: 52px;
  /* Que ocupe todo el contenedor de 100px */
  transform: rotate(180deg);
  /*fill: #4c2b1a; /* El color de la sección de abajo (Información) */
  background: #fffdfc;
  /* Asegura que el fondo del SVG sea transparente */
}

.kofan-cards-group {
  display: flex;
  flex-direction: column;
  gap: 30px;
  width: 100%;
  max-width: 1300px;
}

.subtitulo-blanco {
  color: #82a994;
  text-transform: uppercase;
  font-weight: 700;
  letter-spacing: 2px;
}

.titulo-seccion-blanco {
  font-family: "Handlee", cursive;
  font-size: 2.8rem;
  color: #fff;
  margin-bottom: 40px;
}

/* --- ESTILOS TARJETAS (KOFAN CARD) --- */
.kofan-card-container {
  display: flex;
  justify-content: center;
  padding: 1rem;
}

.kofan-card-wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background: #fff;
  border-radius: 36px;
  padding: 8px;
  /* Espacio mínimo para el borde blanco */
  width: 100%;
  position: relative;
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.2);
}

.kofan-card-image {
  position: absolute;
  inset: 8px;
  width: calc(100% - 16px);
  height: calc(100% - 16px);
  object-fit: cover;
  border-radius: 28px;
}

.kofan-card-content {
  position: relative;
  z-index: 1;
  /* AJUSTE MÓVIL: Padding balanceado para que el texto no pegue a los bordes */
  padding: 160px 25px 30px 25px;
  /* DEGRADADO MÁS SUAVE: Usamos un verde muy oscuro (0, 20, 10) en lugar de negro */
  background: linear-gradient(
    180deg,
    transparent 0%,
    rgba(0, 20, 10, 0.75) 100%
  );
  color: #fff;
  border-radius: inherit;
  width: 100%;
  box-sizing: border-box;
  /* Asegura que el padding no ensanche la tarjeta */
}

.kofan-card-title {
  font-family: "Handlee", cursive;
  font-size: 1.8rem;
}

.kofan-card-subtitle {
  font-size: 1rem;
  color: #ccc;
  margin-bottom: 15px;
}

.kofan-card-text {
  font-size: 0.9rem;
  margin-bottom: 15px;
  height: 60px;
  overflow: hidden;
}

.kofan-card-details {
  display: flex;
  gap: 15px;
  margin-top: 10px;
  margin-bottom: 10px;
  font-size: 0.85rem;
}

.kofan-btn-primary {
  flex: 1;
  background: #1a5c43;
  color: white;
  border: none;
  padding: 10px;
  border-radius: 20px;
  font-weight: 600;
  padding: 5px 20px;
}

.kofan-btn-icon {
  width: 45px;
  height: 45px;
  border-radius: 50%;
  border: none;
  background: rgba(255, 255, 255, 0.2);
  color: white;
  margin-left: 10px;
}

/* --- ESTILOS INFORMACIÓN IMPORTANTE --- */
.info-importante {
  position: relative;
  /* ESTO ES VITAL */
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 100px 20px 150px 20px;
  background-color: #fffdfc;
  /* Fondo suave para contraste */
  z-index: 1;
  /* Crea un contexto de apilamiento para el divisor */
}

/* --- EL DIVISOR --- */
.divisor-hacia-verde {
  position: absolute;
  bottom: -1px;
  /* Un pequeño margen negativo para evitar líneas blancas */
  left: -1px;
  right: -1px;
  width: 100%;
  line-height: 0;
  z-index: 1;
  /* Forzamos que esté al frente */
  pointer-events: none;
  /* Para que no bloquee clics en botones cercanos */
}

.divisor-hacia-verde svg {
  position: relative;
  display: block;
  width: 100%;
  height: 52px;
  /* Que ocupe todo el contenedor de 100px */
  transform: rotate(180deg);
  /*fill: #4c2b1a; /* El color de la sección de abajo (Información) */
  background: #1a5c43;
  /* Asegura que el fondo del SVG sea transparente */
}

.info-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 30px;
  max-width: 1100px;
  margin: 0 auto;
}

.info-card {
  background: white;
  padding: 40px;
  border-radius: 30px;
  border-left: 6px solid #1a5c43;
  /* Detalle de marca en el borde */
  box-shadow: 0 15px 35px rgba(0, 0, 0, 0.05);
  display: flex;
  flex-direction: column;
}

.info-header {
  display: flex;
  align-items: center;
  gap: 15px;
  margin-bottom: 25px;
}

.info-icon {
  font-size: 1.6rem;
  color: #1a5c43;
}

.info-header h3 {
  font-family: "Handlee", cursive;
  font-size: 1.8rem;
  color: #0f3b2a;
  margin: 0;
}

.info-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.info-list li {
  margin-bottom: 15px;
  font-size: 1rem;
  line-height: 1.5;
  color: #444;
  display: flex;
  align-items: flex-start;
}

.check {
  color: #28a745;
  font-weight: bold;
  margin-right: 10px;
}

.cross {
  color: #dc3545;
  font-weight: bold;
  margin-right: 10px;
}

.info-text p {
  font-size: 0.95rem;
  color: #555;
  line-height: 1.6;
}

.mt-2 {
  margin-top: 1rem;
}

/* Botón de WhatsApp integrado en la tarjeta */
.btn-whatsapp {
  margin-top: auto;
  /* Empuja el botón al fondo si una tarjeta es más larga */
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  background-color: #198754;
  color: white;
  padding: 14px;
  border-radius: 18px;
  text-decoration: none;
  font-weight: bold;
  transition: all 0.3s ease;
}

.btn-whatsapp:hover {
  background-color: #20ba5a;
  transform: translateY(-3px);
  box-shadow: 0 5px 15px rgba(37, 211, 102, 0.3);
}

/* --- SECCIÓN UBICACIÓN --- */
.ubicacion {
  position: relative;
  background-color: #1a5c43;
  /* Volvemos al verde Kofán */
  padding: 100px 20px;
  color: white;
  margin-top: -1px;
  /* Evita grietas visuales */
}

/* El arco que viene de la sección blanca anterior */
.divisor-entrada-verde {
  position: absolute;
  top: -1px;
  /* Pegado arriba */
  left: 0;
  width: 100%;
  line-height: 0;
  z-index: 10;
}

.divisor-entrada-verde svg {
  display: block;
  width: 100%;
  height: 60px;
  /* NO rotamos, para que la curva mire hacia arriba y reciba el blanco */
}

.parrafo-ubicacion {
  max-width: 700px;
  margin: 0 auto 30px;
  color: #e0eee0;
  font-size: 1.1rem;
  line-height: 1.6;
}

/* Contenedor del Mapa */
.mapa-wrapper {
  max-width: 1000px;
  margin: 0 auto;
  border-radius: 30px;
  overflow: hidden;
  /* Para que el mapa respete las esquinas redondeadas */
  border: 8px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
}

/* Detalles de llegada */
.detalles-llegada {
  display: flex;
  justify-content: center;
  gap: 40px;
  margin-top: 40px;
  flex-wrap: wrap;
}

.item-llegada {
  display: flex;
  align-items: center;
  gap: 15px;
  background: rgba(255, 255, 255, 0.05);
  padding: 15px 25px;
  border-radius: 20px;
}

.icon-llegada {
  font-size: 1.5rem;
  color: #82a994;
}

.item-llegada p {
  margin: 0;
  font-size: 0.95rem;
}

/* Responsive */
@media (max-width: 768px) {
  .ubicacion {
    padding: 80px 15px;
  }

  .item-llegada {
    width: 100%;
    justify-content: center;
  }
}

/* Ajustes para móviles */
@media (max-width: 768px) {
  .info-card {
    padding: 30px 20px;
  }

  .info-header h3 {
    font-size: 1.5rem;
  }
}

/* --- RESPONSIVE / ESCRITORIO --- */
@media (min-width: 1100px) {
  .kofan-cards-group {
    flex-direction: row;
    align-items: stretch;
    gap: 40px;
  }

  .kofan-card-container {
    flex: 1;
  }

  .kofan-card-wrapper {
    flex-direction: row;
    padding: 24px;
    min-height: 380px;
  }

  .kofan-card-image {
    position: static;
    width: 45%;
    height: 320px;
    margin-left: -50px;
    box-shadow: 10px 10px 30px rgba(0, 0, 0, 0.2);
    flex-shrink: 0;
  }

  .kofan-card-content {
    background: transparent;
    /* Quitamos el degradado en PC */
    color: #333;
    /* AJUSTE ESCRITORIO: Quitamos el padding superior excesivo y damos espacio a la izquierda */
    padding: 20px 20px 20px 45px;
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    /* Alinea el texto a la izquierda en PC */
    text-align: left;
  }

  .kofan-card-title {
    color: #0f3b2a;
    margin-bottom: 10px;
  }

  .kofan-card-text {
    color: #555;
    height: auto;
    margin-bottom: 20px;
  }

  .kofan-card-subtitle {
    color: #777;
  }

  .kofan-btn-icon {
    background: #eee;
    color: #1a5c43;
  }

  .kofan-card-details {
    justify-content: flex-start;
  }
}

@media (max-width: 992px) {
  #home {
    flex-direction: column;
    text-align: center;
  }

  .home-content h1 {
    font-size: 2.5rem;
  }
}

/* ANIMACIONES */
@keyframes float {
  0%,
  100% {
    transform: translateY(0);
  }

  50% {
    transform: translateY(-20px);
  }
}

@keyframes slideInLeft {
  from {
    opacity: 0;
    transform: translateX(-60px);
  }

  to {
    opacity: 1;
    transform: translateX(0);
  }
}
</style>
