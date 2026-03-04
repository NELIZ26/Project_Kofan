import { defineStore } from "pinia";
import { ref, reactive, computed } from "vue";
import Swal from "sweetalert2";

export const useReservaStore = defineStore("reserva", () => {
  // --- ESTADO ---
  const isModalOpen = ref(false);
  const showSuccess = ref(false); // Mantener por si acaso, aunque SweetAlert lo reemplaza
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
      if (!form.fechaNacimiento) {
        errors.fechaNacimiento = true;
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

  // ✅ FUNCIÓN DE ENVÍO CON SWEETALERT
  const handleSubmit = async () => {
    if (validateForm()) {
      Swal.fire({
        title: "Procesando Reserva...",
        text: "Estamos conectando con la maloka principal",
        target: "body", // <--- ESTO ES LA CLAVE
        allowOutsideClick: false,
        didOpen: () => {
          Swal.showLoading();
        },
      });

      setTimeout(() => {
        Swal.fire({
          icon: "success",
          title: "¡Reserva Registrada!",
          text: `Gracias ${form.nombres}, hemos recibido tu solicitud.`,
          target: "body", // <--- TAMBIÉN AQUÍ
          confirmButtonColor: "#0f3b2a",
          confirmButtonText: "¡Excelente!",
          backdrop: `rgba(15, 59, 42, 0.4)`,
        });

        closeModal();
        resetForm();
      }, 2000);
    } else {
      Swal.fire({
        icon: "error",
        title: "Formulario Incompleto",
        text: "Por favor, revisa los campos marcados en rojo.",
        target: "body", // <--- Y AQUÍ
        confirmButtonColor: "#e74c3c",
      });
    }
  };

  const closeSuccessMessage = () => {
    showSuccess.value = false;
    isModalOpen.value = false;
  };

  return {
    isModalOpen,
    showSuccess,
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
    closeSuccessMessage,
  };
});
