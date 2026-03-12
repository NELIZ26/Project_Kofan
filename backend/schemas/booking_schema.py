from enum import Enum

from pydantic import BaseModel
from datetime import date
from typing import List, Optional
from pydantic import EmailStr
from datetime import datetime, time, timezone

# Esquema para los acompañantes (se usará dentro de la reserva)

class EstadoReserva(str, Enum):
    PENDIENTE = "pendiente"
    CONFIRMADA = "confirmada"
    CANCELADA = "cancelada"
    FINALIZADA = "finalizada"
    
# 2. Estructura de acompañantes (Se mantiene igual)
class AcompananteSchema(BaseModel):
    nombre_completo: str
    numero_documento: str

# 3. ESQUEMA BASE: Aquí ponemos lo que AMBOS tipos de reserva necesitan
class ReservaBase(BaseModel):
    habitacion_id: str
    fecha_entrada: date
    fecha_salida: date
    monto_total: float
    acompanantes: List[AcompananteSchema] = [] 
    observaciones: Optional[str] = None
    estado: EstadoReserva = EstadoReserva.PENDIENTE

# 4. PARA USUARIOS LOGUEADOS: No pide datos de contacto (se sacan del Token)
class ReservaCreate(ReservaBase):
    pass 

# 5. PARA CLIENTES PÚBLICOS: ¡Aquí inyectamos el celular y el correo!
class ReservaPublicCreate(ReservaBase):
    cliente_nombre: str       # Nombre del invitado
    cliente_email: EmailStr    # El correo que pediste (validado)
    cliente_celular: str       # El celular que pediste

# 6. ESQUEMA DE RESPUESTA: Lo que devolvemos al frontend
class ReservaResponse(ReservaBase):
    id: str
    cliente_id: Optional[str] = None # Puede ser nulo si es invitado
    # Si es invitado, también devolvemos sus datos de contacto
    cliente_nombre: Optional[str] = None
    cliente_email: Optional[EmailStr] = None
    cliente_celular: Optional[str] = None