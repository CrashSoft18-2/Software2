SELECT usuario.nombre, usuario.apellido, curso.nombre, asesorias.hora, asesorias.lugar, asesorias.dia 
FROM asesorias 
INNER JOIN asesoriaprofesor ON ( asesorias.idAsesorias = asesoriaprofesor.idAsesorias ) 
INNER JOIN profesor ON (profesor.idProfesor = asesoriaprofesor.idProfesor) 
INNER JOIN usuario ON (usuario.idUsuario = profesor.usuario_idUsuario) 
INNER JOIN profesorcurso ON (profesor.idProfesor = profesorcurso.idProfesor)
INNER JOIN curso ON (curso.idCurso = profesorcurso.idCurso);
