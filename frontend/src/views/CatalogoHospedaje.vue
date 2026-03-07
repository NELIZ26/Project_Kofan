<template>
  <div id="contenido1" class="bg-light-kofan">
    <div class="header-section text-center py-5">
      <font-awesome-icon
        icon="fa-solid fa-mountain-sun"
        class="verde-kofan mb-3 fs-1"
      />
      <h1 class="fw-bold verde-kofan">Nuestros Alojamientos</h1>
      <p class="text-muted container" style="max-width: 700px">
        Desconéctate del mundo y reconéctate con la tierra. Elige entre la
        privacidad de nuestras cabañas artesanales o la calidez de nuestras
        habitaciones tradicionales.
      </p>
    </div>

    <section class="container mb-5" id="seccionCabanas">
      <div class="d-flex align-items-center mb-4">
        <div class="linea-verde"></div>
        <h2 class="mx-3 fw-bold verde-kofan">Cabañas Independientes</h2>
      </div>

      <div class="cards-grid">
        <div
          v-for="c in cabanasIndependientes"
          :key="c.id"
          class="card-kofan-v2"
        >
          <div class="img-container">
            <img :src="c.image" :alt="c.name" />
            <div class="badge-precio">{{ formatPrice(c.price) }}</div>
          </div>
          <div class="content p-4">
            <h4 class="fw-bold mb-2">{{ c.name }}</h4>
            <p class="text-muted small flex-grow-1">{{ c.description }}</p>
            <div
              class="footer-card d-flex justify-content-between align-items-center"
            >
              <span class="capacidad"
                ><font-awesome-icon icon="fa-solid fa-users" />
                {{ c.capacity }} pers.</span
              >
              <button class="btn-reservar-kofan" @click="reserva.openModal()">
                Reservar Ahora
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="container pb-5" id="seccionHabitaciones">
      <div class="d-flex align-items-center mb-4">
        <div class="linea-verde"></div>
        <h2 class="mx-3 fw-bold verde-kofan">Habitaciones en Maloka</h2>
      </div>

      <div class="cards-grid">
        <div v-for="h in habitacionesMaloka" :key="h.id" class="card-kofan-v2">
          <div class="img-container">
            <img :src="h.image" :alt="h.name" />
            <div class="badge-precio">{{ formatPrice(h.price) }}</div>
          </div>
          <div class="content p-4">
            <h4 class="fw-bold mb-2">{{ h.name }}</h4>
            <p class="text-muted small flex-grow-1">{{ h.description }}</p>
            <div
              class="footer-card d-flex justify-content-between align-items-center"
            >
              <span class="capacidad"
                ><font-awesome-icon icon="fa-solid fa-bed" />
                {{ h.capacity }} pers.</span
              >
              <button class="btn-reservar-kofan" @click="reserva.openModal()">
                Reservar Ahora
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { computed } from "vue";
import { useReservaStore } from "../stores/reserva.js";

const images = import.meta.glob("../img/habitacion*.jpg", {
  eager: true,
  import: "default",
});
const reserva = useReservaStore();

const formatPrice = (v) =>
  v.toLocaleString("es-CO", {
    style: "currency",
    currency: "COP",
    maximumFractionDigits: 0,
  });

// DATA ORGANIZADA
const allAccommodations = [
  {
    id: 1,
    type: "cabana",
    name: "Cabaña Ancestral",
    capacity: "2",
    price: 120000,
    description: "Privacidad total con vista al sendero botánico.",
    image: images["../img/habitacion1.jpg"],
  },
  {
    id: 2,
    type: "cabana",
    name: "Nido de Selva",
    capacity: "2",
    price: 140000,
    description: "Arquitectura en madera con ventanales panorámicos.",
    image: images["../img/habitacion2.jpg"],
  },
  {
    id: 3,
    type: "habitacion",
    name: "Habitación Familiar Maloka",
    capacity: "6",
    price: 200000,
    description: "Ubicada en la estructura principal, ideal para grupos.",
    image: images["../img/habitacion3.jpg"],
  },
  {
    id: 4,
    type: "habitacion",
    name: "Suite Kofán",
    capacity: "8",
    price: 150000,
    description: "Nuestra habitación más amplia con balcones internos.",
    image: images["../img/habitacion4.jpg"],
  },
  {
    id: 5,
    type: "habitacion",
    name: "Suite Kofán",
    capacity: "8",
    price: 150000,
    description: "Nuestra habitación más amplia con balcones internos.",
    image: images["../img/habitacion5.jpg"],
  },
  {
    id: 6,
    type: "habitacion",
    name: "Suite Kofán",
    capacity: "8",
    price: 150000,
    description: "Nuestra habitación más amplia con balcones internos.",
    image: images["../img/habitacion6.jpg"],
  },
  {
    id: 7,
    type: "cabana",
    name: "Nido de Selva",
    capacity: "2",
    price: 140000,
    description: "Arquitectura en madera con ventanales panorámicos.",
    image: images["../img/habitacion6.jpg"],
  },
  {
    id: 8,
    type: "cabana",
    name: "Nido de Selva",
    capacity: "2",
    price: 140000,
    description: "Arquitectura en madera con ventanales panorámicos.",
    image: images["../img/habitacion5.jpg"],
  },
  // Agrega los demás aquí según su tipo...
];

const cabanasIndependientes = computed(() =>
  allAccommodations.filter((a) => a.type === "cabana"),
);
const habitacionesMaloka = computed(() =>
  allAccommodations.filter((a) => a.type === "habitacion"),
);
</script>

<style scoped>
.bg-light-kofan {
  background-color: #f8fcf9;
  min-height: 100vh;
  margin-top: 60px;
}
.verde-kofan {
  color: #0f3b2a;
}

.linea-verde {
  height: 4px;
  width: 50px;
  background-color: #2ecc71;
  border-radius: 2px;
}

.cards-grid {
  display: grid;
  gap: 2.5rem;
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
}

.card-kofan-v2 {
  background: white;
  border-radius: 30px;
  overflow: hidden;
  box-shadow: 0 15px 35px rgba(0, 0, 0, 0.05);
  transition: all 0.4s ease;
  display: flex;
  flex-direction: column;
  border: 1px solid rgba(15, 59, 42, 0.05);
}

.card-kofan-v2:hover {
  transform: translateY(-12px);
  box-shadow: 0 25px 50px rgba(15, 59, 42, 0.15);
}

.img-container {
  position: relative;
  height: 250px;
  overflow: hidden;
}

.img-container img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.6s ease;
}

.card-kofan-v2:hover .img-container img {
  transform: scale(1.1);
}

.badge-precio {
  position: absolute;
  bottom: 15px;
  right: 15px;
  background: #0f3b2a;
  color: white;
  padding: 8px 18px;
  border-radius: 50px;
  font-weight: 700;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
}

.content {
  flex-grow: 1;
  display: flex;
  flex-direction: column;
}

.capacidad {
  font-size: 0.9rem;
  font-weight: 600;
  color: #1a5c43;
}

.btn-reservar-kofan {
  background: #0f3b2a;
  color: white;
  border: none;
  padding: 10px 22px;
  border-radius: 15px;
  font-weight: 600;
  transition: 0.3s;
}

.btn-reservar-kofan:hover {
  background: #2ecc71;
  transform: scale(1.05);
}

@media (max-width: 768px) {
  .cards-grid {
    grid-template-columns: 1fr;
  }
}
</style>
