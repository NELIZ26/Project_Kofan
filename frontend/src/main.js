import { createApp } from "vue";
import { createPinia } from "pinia";
import App from "./App.vue";
import router from "./router";

// --- ESTILOS ---
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min.js";
import "bootstrap-icons/font/bootstrap-icons.css";
import "./styles/global.css";

// --- FONTAWESOME ---
import { library } from "@fortawesome/fontawesome-svg-core";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";


// Iconos Sólidos (fas)
import {
  faLeaf,
  faHandsHolding,
  faMoon,
  faTag,
  faBed,
  faHeart,
  faUsers,
  faWifi,
  faCalendarCheck,
  faLocationDot,
  faPhone,
  faEnvelope,
  faCircleInfo,
  faShieldHalved,
  faSeedling,
  faEye,
  faHeartPulse,
  faEarthAmericas,
  faPersonPraying,
  faHandshakeAngle,
  faDroplet, 
  faSun, 
  faMound,
  faPlane,
  faCar,
  faUserGear,
  faBell,
  faRightFromBracket,
  faPlus,
  faHouseChimney,
  faHotel,
  faFilter,
  faTrashCan,
  faMagnifyingGlass,
  faArrowLeft,
  faUser,
  faCompass,
  faSave,
  faCalendarXmark
} from "@fortawesome/free-solid-svg-icons";

// Iconos de Marcas (fab)
import {
  faInstagram,
  faFacebook,
  faTiktok,
  faWhatsapp,
  faFacebookF,
} from "@fortawesome/free-brands-svg-icons";

// Añadir todos los iconos a la librería de una sola vez
library.add(
  faLeaf,
  faHandsHolding,
  faMoon,
  faTag,
  faBed,
  faHeart,
  faUsers,
  faWifi,
  faCalendarCheck,
  faLocationDot,
  faPhone,
  faEnvelope,
  faInstagram,
  faFacebook,
  faTiktok,
  faWhatsapp,
  faCircleInfo,
  faShieldHalved,
  faSeedling,
  faEye,
  faHeartPulse,
  faEarthAmericas,
  faPersonPraying,
  faHandshakeAngle,
  faDroplet,
  faSun,
  faMound,
  faFacebookF,
  faPlane,
  faCar,
  faUserGear,
  faBell,
  faRightFromBracket,
  faPlus,
  faHouseChimney,
  faHotel,
  faFilter,
  faTrashCan,
  faMagnifyingGlass,
  faArrowLeft,
  faUser,
  faCompass,
  faSave,
  faCalendarXmark
);

// --- CREAR LA APP ---
const app = createApp(App);

app.use(createPinia());
app.use(router);

// Registrar el componente globalmente (AHORA SÍ, después de crear 'app')
app.component("font-awesome-icon", FontAwesomeIcon);

app.mount("#app");
