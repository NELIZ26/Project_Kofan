<template>
  <div class="avisos-container">
    <div class="d-flex justify-content-between align-items-center mb-4">
      <h3 class="fw-bold verde-kofan">Centro de Avisos</h3>
      <button class="btn btn-sm btn-outline-secondary">Marcar todos como leídos</button>
    </div>

    <div class="list-group gap-3">
      <div class="aviso-card info shadow-sm p-3 d-flex align-items-start gap-3">
        <div class="icon-box bg-success-light text-success">
          <font-awesome-icon icon="bell" />
        </div>
        <div class="flex-grow-1">
          <div class="d-flex justify-content-between">
            <h6 class="fw-bold mb-1">¡Reserva Confirmada!</h6>
            <small class="text-muted">Hace 2 horas</small>
          </div>
          <p class="mb-0 text-secondary small">Tu estancia en la "Maloka Ancestral" ha sido aprobada. ¡Te esperamos con los brazos abiertos!</p>
        </div>
      </div>

      <div class="aviso-card promo shadow-sm p-3 d-flex align-items-start gap-3">
        <div class="icon-box bg-warning-light text-warning">
          <font-awesome-icon icon="bed" class="verde-kofan" />
        </div>
        <div class="flex-grow-1">
          <div class="d-flex justify-content-between">
            <h6 class="fw-bold mb-1">Cena Romántica 20% OFF</h6>
            <small class="text-muted">Ayer</small>
          </div>
          <p class="mb-0 text-secondary small">Por ser cliente frecuente, tienes un descuento especial en nuestra cena bajo las estrellas.</p>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.verde-kofan { color: #0f3b2a; }

.aviso-card {
  border-radius: 15px;
  background: white;
  border-left: 5px solid transparent;
  transition: transform 0.2s;
}

.aviso-card:hover {
  transform: translateX(5px);
}

.aviso-card.info { border-left-color: #2ecc71; }
.aviso-card.promo { border-left-color: #f1c40f; }

.icon-box {
  width: 45px;
  height: 45px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.bg-success-light { background: #e0fdf0; }
.bg-warning-light { background: #fff9db; }
</style>