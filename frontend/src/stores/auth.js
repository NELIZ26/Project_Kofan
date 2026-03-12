import { defineStore } from 'pinia';
import { ref, computed } from 'vue';

export const useAuthStore = defineStore('auth', () => {
  // --- ESTADO ---
  const user = ref(null); // Aquí guardaremos { nombre, email, rol, etc. }
  const token = ref(localStorage.getItem('userToken') || null);

  // --- GETTERS (Computed) ---
  const isLogged = computed(() => !!token.value);

  // --- ACCIONES (Métodos) ---
  
  // 1. Iniciar Sesión
  const login = (userData, userToken) => {
    user.value = userData;
    token.value = userToken;
    localStorage.setItem('userToken', userToken);
    // Podrías guardar también el objeto user si lo necesitas persistente
    localStorage.setItem('userData', JSON.stringify(userData));
  };

  // 2. Cerrar Sesión
  const logout = () => {
    user.value = null;
    token.value = null;
    localStorage.removeItem('userToken');
    localStorage.removeItem('userData');
  };

  return { user, token, isLogged, login, logout };
});

