SELECT usuario.nombre, usuario.apellido, carrera.nombre, curso.nombre, cita.Fecha, asesorias.Hora, asesorias.lugar 
FROM cita
INNER JOIN asesoriaprofesor ON ( cita.idAsesoriaProfeso = asesoriaprofesor.idAsesorias )
INNER JOIN asesorias ON (asesorias.idAsesorias = asesoriaprofesor.idAsesorias) 
INNER JOIN profesor ON ( profesor.idProfesor = asesoriaprofesor.idProfesor )
INNER JOIN usuario ON ( usuario.idUsuario = profesor.usuario_idUsuario )
INNER JOIN curso ON ( curso.idCurso = cita.idCurso)
INNER JOIN profesorcarrera ON ( profesor.idProfesor = profesorcarrera.idProfesor)
INNER JOIN carrera ON ( carrera.idCarrera = curso.Carrera_idCarrera)
;