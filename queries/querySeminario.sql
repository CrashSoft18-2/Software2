Select usuario.nombre, usuario.apellido, seminario.tema, seminario.fechaHora, seminario.lugar
from seminario
INNER JOIN profesor ON (seminario.idProfesor = profesor.idProfesor)
INNER JOIN usuario ON (usuario.idUsuario = profesor.usuario_idUsuario );