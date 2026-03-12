<template>
  <main class="galeria-page">
    <section class="galeria-hero text-center text-white">
      <div class="container">
        <h1 class="titulo-galeria">Fragmentos de la Selva</h1>
        <p class="lead">
          Capturando la magia, el color y la vida del Ecohotel Kofán.
        </p>
      </div>
      <div class="custom-shape-divider-bottom">
        <svg viewBox="0 0 1000 100" preserveAspectRatio="none">
          <path
            class="shape-fill"
            d="M421.9,6.5c22.6-2.5,51.5,0.4,75.5,5.3c23.6,4.9,70.9,23.5,100.5,35.7c75.8,32.2,133.7,44.5,192.6,49.7 c23.6,2.1,48.7,3.5,103.4-2.5c54.7-6,106.2-25.6,106.2-25.6V0H0v30.3c0,0,72,32.6,158.4,30.5c39.2-0.7,92.8-6.7,134-22.4 c21.2-8.1,52.2-18.2,79.7-24.2C399.3,7.9,411.6,7.5,421.9,6.5z"
          ></path>
        </svg>
      </div>
    </section>

    <section class="filtros-galeria py-4 text-center">
      <div class="container">
        <div class="d-flex justify-content-center gap-2 flex-wrap">
          <button class="btn btn-outline-success active">Todos</button>
          <button class="btn btn-outline-success">Naturaleza</button>
          <button class="btn btn-outline-success">Experiencias</button>
          <button class="btn btn-outline-success">Instalaciones</button>
        </div>
      </div>
    </section>

    <section class="grid-fotos pb-5">
      <div class="container">
        <div class="masonry-wrapper">
          <div class="masonry-item">
            <img
              src="../img/eventos4.jpg"
              alt="Atardecer"
              class="img-fluid rounded-4"
            />
            <div class="overlay-info">
              <span>Atardecer en el Río</span>
            </div>
          </div>
          <div class="masonry-item">
            <img
              src="../img/ancestral.jpg"
              alt="Atardecer"
              class="img-fluid rounded-4"
            />
            <div class="overlay-info">
              <span>Ancestrakl</span>
            </div>
          </div>
          <div class="masonry-item">
            <img
              src="../img/casa okfan.jpg"
              alt="Maloka"
              class="img-fluid rounded-4"
            />
            <div class="overlay-info">
              <span>Nuestra Maloka Ancestral</span>
            </div>
          </div>
          <div class="masonry-item item-tall">
            <img
              src="../img/eventos3.jpg"
              alt="Fauna"
              class="img-fluid rounded-4"
            />
            <div class="overlay-info">
              <span>Fauna Local</span>
            </div>
          </div>
          <div class="masonry-item">
            <img
              src="../img/eventos5.jpg"
              alt="Comida"
              class="img-fluid rounded-4"
            />
            <div class="overlay-info">
              <span>Gastronomía Amazónica</span>
            </div>
          </div>
          <div class="masonry-item">
            <img
              src="../img/eventos6.jpg"
              alt="Yoga"
              class="img-fluid rounded-4"
            />
            <div class="overlay-info">
              <span>Bienestar y Espíritu</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="galeria-cta py-5 bg-light text-center">
      <div class="container">
        <h3>¿Quieres vivirlo en persona?</h3>
        <button
          class="btn btn-success btn-lg rounded-pill mt-3"
          @click="$router.push('/contacto')"
        >
          Planea tu visita
        </button>
      </div>
    </section>
  </main>
</template>

<style scoped>
.galeria-hero {
  background:
    linear-gradient(rgba(15, 59, 42, 0.8), rgba(15, 59, 42, 0.8)),
    url("../img/fondo3.png") center/cover;
  padding: 120px 0 80px;
  position: relative;
}

.titulo-galeria {
  font-family: "Handlee", cursive;
  font-size: 3.5rem;
}

/* Grid Masonry con CSS Columns */
.masonry-wrapper {
  column-count: 3; /* 3 columnas en escritorio */
  column-gap: 20px;
}

.masonry-item {
  position: relative;
  display: inline-block;
  width: 100%;
  margin-bottom: 20px;
  overflow: hidden;
  border-radius: 20px;
  cursor: pointer;
}

.masonry-item img {
  transition: transform 0.5s ease;
  width: 100%;
  display: block;
}

/* Efecto al pasar el mouse */
.masonry-item:hover img {
  transform: scale(1.1);
}

.overlay-info {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  background: linear-gradient(transparent, rgba(15, 59, 42, 0.9));
  color: white;
  padding: 20px;
  opacity: 0;
  transition: opacity 0.3s ease;
  font-weight: 500;
}

.masonry-item:hover .overlay-info {
  opacity: 1;
}

/* Divisor */
.custom-shape-divider-bottom {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  line-height: 0;
  transform: rotate(180deg);
}

.custom-shape-divider-bottom svg {
  position: relative;
  display: block;
  width: calc(100% + 1.3px);
  height: 40px; /* Modificar para que sea sutil */
}

.shape-fill {
  fill: #fffdfc;
}

/* Responsive */
@media (max-width: 992px) {
  .masonry-wrapper {
    column-count: 2; /* 2 columnas en tablets */
  }
}

@media (max-width: 576px) {
  .masonry-wrapper {
    column-count: 1; /* 1 columna en móviles */
  }
  .titulo-galeria {
    font-size: 2.5rem;
  }
}
</style>
