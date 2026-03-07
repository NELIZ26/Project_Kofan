import { createRouter, createWebHistory } from "vue-router";
import { useAuthStore } from "../stores/auth";
import Home from "../views/Home.vue";
import About from "../views/About.vue";
import Galeria from "../views/GaleriaFotos.vue";
import Contacto from "../views/Contacto.vue";
import Login from "../views/Login.vue";
import Register from "../views/Register.vue";
import AccountLayout from "../views/AccountLayout.vue";
import DatosPersonales from "../views/account/DatosPersonales.vue";
import MisReservas from "../views/account/MisReservas.vue";
import Avisos from "../views/account/Avisos.vue";
import Servicios from "../views/ServiceSelection.vue";
import CatalogoHospedaje from "../views/CatalogoHospedaje.vue";

const routes = [
  { path: "/", redirect: "/home" },
  { path: "/home", name: "home", component: Home },
  { path: "/about", name: "about", component: About },
  { path: "/galeria", name: "galeria", component: Galeria },
  { path: "/servicios", name: "servicios", component: Servicios },
  { path: "/contacto", name: "contacto", component: Contacto },
  {
    path: '/servicios/hospedaje',
    name: 'hospedaje',
    component: CatalogoHospedaje
  },
  {
    path: "/login",
    name: "login",
    component: Login,
    meta: { requiresAuth: false },
  },
  {
    path: "/register",
    name: "register",
    component: Register,
    meta: { requiresAuth: false },
  },
  {
    path: "/account",
    component: AccountLayout,
    meta: { requiresAuth: true },
    children: [
      { path: "datos", name: "account-datos", component: DatosPersonales },
      { path: "reservas", name: "account-reservas", component: MisReservas },
      { path: "avisos", name: "account-avisos", component: Avisos },
      {
        path: "reserva-detalle/:id",
        name: "account-reserva-detalle",
        component: () => import("@/views/account/DetalleReserva.vue"),
      },
    ],
  },
  {
    path: "/:pathMatch(.*)*",
    name: "not-found",
    component: () => import("@/views/NotFound.vue"),
  },
  {
    path: "/admin",
    component: () => import("../views/admin/AdminLayount.vue"),
    children: [
      {
        path: "",
        redirect: { name: "admin-rooms" }, // o admin-rooms, lo que quieras por defecto
      },
      {
        path: "estadisticas",
        name: "admin-stats",
        component: () => import("../views/admin/Stats.vue"),
      },
      {
        path: "habitaciones",
        name: "admin-rooms",
        component: () => import("../views/admin/RoomsManager.vue"),
      },
      {
        path: "usuarios",
        name: "admin-users",
        component: () => import("../views/admin/UsersManager.vue"),
      },
      {
        path: "reservas",
        name: "admin-bookings",
        component: () => import("../views/admin/BookingsManager.vue"),
      },
      {
        path: "galeria",
        name: "admin-gallery",
        component: () => import("../views/admin/GalleryManager.vue"),
      },
    ],
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
  // --- SOLUCIÓN AL PROBLEMA DEL SCROLL ---
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition;
    } else {
      // Siempre vuelve arriba al cambiar de página con un efecto suave
      return { top: 0, behavior: "smooth" };
    }
  },
});

router.beforeEach((to) => {
  const auth = useAuthStore();
  if (to.meta.requiresAuth && !auth.isLogged) {
    console.log("Redireccionando: Acceso no autorizado");
    return "/";
  }
});

export default router;
