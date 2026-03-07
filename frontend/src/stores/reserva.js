import { defineStore } from "pinia";
import { ref, reactive, computed } from "vue";
import Swal from "sweetalert2";

export const useReservaStore = defineStore("reserva", () => {
  // --- ESTADO ---
  const isModalOpen = ref(false);
  const personType = ref("natural");

  const form = reactive({
    nombres: "",
    tipoDocumento: "",
    correo: "",
    fechaNacimiento: "",
    numDocumento: "",
    telefono: "",
    cantidadPersonas: "2",
    habitacion: "Cabana2",
    fechaReserva: "",
  });

  const errors = reactive({
    nombres: false,
    tipoDocumento: false,
    correo: false,
    fechaNacimiento: false,
    numDocumento: false,
    telefono: false,
    fechaReserva: false,
  });

  // --- COMPUTADOS ---
  const minDate = computed(() => new Date().toISOString().split("T")[0]);

  const labelNombres = computed(() =>
    personType.value === "juridica" ? "Razón Social" : "Nombres y Apellidos",
  );

  const placeholderNombres = computed(() =>
    personType.value === "juridica" ? "Ej: Empresa SAS" : "Ej: Juan Pérez",
  );

  const labelNumDoc = computed(() =>
    personType.value === "juridica" ? "NIT" : "Número de Documento",
  );

  // --- ACCIONES / FUNCIONES ---
  const openModal = () => {
    isModalOpen.value = true;
    clearErrors();
  };

  const closeModal = () => {
    isModalOpen.value = false;
  };

  const setPersonType = (type) => {
    personType.value = type;
  };

  const clearErrors = () => {
    Object.keys(errors).forEach((key) => (errors[key] = false));
  };

  const resetForm = () => {
    form.nombres = "";
    form.tipoDocumento = "";
    form.correo = "";
    form.fechaNacimiento = "";
    form.numDocumento = "";
    form.telefono = "";
    form.fechaReserva = "";
    form.cantidadPersonas = "2";
    form.habitacion = "Cabana2";
    personType.value = "natural";
    clearErrors();
  };

  const validateForm = () => {
    let isValid = true;
    clearErrors();

    if (!form.nombres.trim()) {
      errors.nombres = true;
      isValid = false;
    }

    if (personType.value === "natural") {
      if (!form.tipoDocumento) {
        errors.tipoDocumento = true;
        isValid = false;
      }
    }

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!form.correo || !emailRegex.test(form.correo)) {
      errors.correo = true;
      isValid = false;
    }

    if (!form.numDocumento) {
      errors.numDocumento = true;
      isValid = false;
    }
    if (!form.telefono) {
      errors.telefono = true;
      isValid = false;
    }
    if (!form.fechaReserva) {
      errors.fechaReserva = true;
      isValid = false;
    }

    return isValid;
  };

  // ✅ FUNCIÓN DE ENVÍO INTEGRADA CON WHATSAPP
  const handleSubmit = async () => {
    if (validateForm()) {
      // 1. Alerta de procesamiento
      Swal.fire({
        title: "Procesando Reserva...",
        text: "Estamos conectando con la maloka principal",
        allowOutsideClick: false,
        didOpen: () => {
          Swal.showLoading();
        },
      });

      // Simulación de guardado en DB (2 segundos)
      setTimeout(async () => {
        // 2. Preparar mensaje de WhatsApp
        const telefonoHotel = "573124225925";
        const mensajeWA = `¡Hola Ecohotel Kofán! 🌿%0A` +
                          `Me gustaría confirmar una reserva:%0A%0A` +
                          `👤 *Nombre:* ${form.nombres}%0A` +
                          `🆔 *Doc:* ${form.numDocumento}%0A` +
                          `🏨 *Alojamiento:* ${form.habitacion}%0A` +
                          `👥 *Huéspedes:* ${form.cantidadPersonas}%0A` +
                          `📅 *Check-In:* ${form.fechaReserva}%0A%0A` +
                          `Espero instrucciones de pago.`;

        // 3. Alerta de éxito antes de redirigir
        await Swal.fire({
          icon: "success",
          title: "¡Solicitud Registrada!",
          text: `Gracias ${form.nombres}, ahora te redirigiremos a WhatsApp para finalizar tu pago.`,
          confirmButtonColor: "#0f3b2a",
          confirmButtonText: "Ir a WhatsApp 💬",
        });

        // 4. Abrir WhatsApp y limpiar todo
        window.open(`https://wa.me/${telefonoHotel}?text=${mensajeWA}`, '_blank');
        
        closeModal();
        resetForm();
      }, 2000);

    } else {
      Swal.fire({
        icon: "error",
        title: "Formulario Incompleto",
        text: "Por favor, revisa los campos marcados en rojo.",
        confirmButtonColor: "#e74c3c",
      });
    }
  };

  return {
    isModalOpen,
    personType,
    form,
    errors,
    minDate,
    labelNombres,
    placeholderNombres,
    labelNumDoc,
    openModal,
    closeModal,
    setPersonType,
    handleSubmit,
    resetForm, // Exportado para uso manual si se requiere
  };
});