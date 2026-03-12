<template>
  <footer class="kofan-footer">
    <div class="container footer-grid">
      <div class="footer-brand">
        <h2 class="footer-logo">Kofán</h2>
        <p>
          Conectando el espíritu humano con la magia de la Amazonía. Un refugio
          de paz, cultura y naturaleza.
        </p>
        <div class="social-links">
          <a href="https://www.instagram.com/ecohotelkofan/" class="social-icon"
            ><font-awesome-icon :icon="['fab', 'instagram']"
          /></a>
          <a href="https://www.facebook.com/ecohotelkofan" class="social-icon"
            ><font-awesome-icon :icon="['fab', 'facebook']"
          /></a>
          <a href="https://www.tiktok.com/@ecohotelkofan?_r=1&_t=ZS-94Lg6dczT2D" class="social-icon"
            ><font-awesome-icon :icon="['fab', 'tiktok']"
          /></a>
        </div>
      </div>

      <div class="footer-links">
        <h3>Navegación</h3>
        <ul>
          <li><a href="#home">Inicio</a></li>
          <li><a href="#experiencias">Experiencias</a></li>
          <li><a href="#servicios">Hospedaje</a></li>
          <li><a href="#donde-estamos">Ubicación</a></li>
        </ul>
      </div>

      <div class="footer-contact">
        <h3>Contacto</h3>
        <p>
          <font-awesome-icon icon="['fa', 'locationDot']" /> Puerto Asís,
          Putumayo
        </p>
        <p><font-awesome-icon icon="['fa', 'phone']" /> +57 322 4225925</p>
        <p>
          <font-awesome-icon icon="['fas', 'envelope']" /> kofancentroecoturistico@gmail.com
        </p>
      </div>
    </div>

    <div class="footer-bottom">
      <div class="container">
        <hr class="footer-line" />
        <div class="bottom-flex">
          <p>&copy; 2026 Kofán Amazonía. Todos los derechos reservados.</p>
          <p>Hecho con ❤️ en el Putumayo</p>
        </div>
      </div>
    </div>
  </footer>
</template>

<style scoped>
.kofan-footer {
  background-color: #0f3b2a; /* Verde oscuro "Noche" */
  color: #e0eee0;
  padding: 80px 20px 20px 20px;
}

.footer-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 50px;
  max-width: 1100px;
  margin: 0 auto;
}

.footer-logo {
  font-family: "Handlee", cursive;
  font-size: 2.5rem;
  color: #fff;
  margin-bottom: 20px;
}

.footer-brand p {
  font-size: 0.95rem;
  line-height: 1.6;
  opacity: 0.8;
}

.social-links {
  display: flex;
  gap: 15px;
  margin-top: 25px;
}

.social-icon {
  width: 40px;
  height: 40px;
  background: rgba(255, 255, 255, 0.1);
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  color: white;
  text-decoration: none;
  transition: all 0.3s ease;
}

.social-icon:hover {
  background: #1a5c43;
  transform: translateY(-5px);
}

.footer-links h3,
.footer-contact h3 {
  color: #fff;
  font-size: 1.2rem;
  margin-bottom: 25px;
  position: relative;
}

.footer-links h3::after,
.footer-contact h3::after {
  content: "";
  position: absolute;
  left: 0;
  bottom: -8px;
  width: 40px;
  height: 2px;
  background: #1a5c43;
}

.footer-links ul {
  list-style: none;
  padding: 0;
}

.footer-links li {
  margin-bottom: 12px;
}

.footer-links a {
  color: #e0eee0;
  text-decoration: none;
  opacity: 0.7;
  transition: 0.3s;
}

.footer-links a:hover {
  opacity: 1;
  padding-left: 5px;
  color: #82a994;
}

.footer-contact p {
  display: flex;
  align-items: center;
  gap: 15px;
  margin-bottom: 15px;
  font-size: 0.95rem;
  opacity: 0.8;
}

/* --- BOTTOM --- */
.footer-line {
  border: 0;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  margin: 40px 0 20px 0;
}

.bottom-flex {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 0.85rem;
  opacity: 0.6;
  flex-wrap: wrap;
  gap: 10px;
}

/* Ajustes para móviles */
@media (max-width: 768px) {
  .footer-grid {
    text-align: center;
    gap: 40px;
  }
  .social-links {
    justify-content: center;
  }
  .footer-links h3::after,
  .footer-contact h3::after {
    left: 50%;
    transform: translateX(-50%);
  }
  .footer-contact p {
    justify-content: center;
  }
  .bottom-flex {
    justify-content: center;
    flex-direction: column;
  }
}
</style>
