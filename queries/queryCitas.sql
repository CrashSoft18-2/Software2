SELECT usuario.nombre, usuario.apellido, carrera.nombre, curso.nombre, cita.Fecha, asesorias.Hora, asesorias.lugar, consultas.consulta
FROM cita
INNER JOIN asesorias ON (asesorias.idAsesorias = cita.idAsesoriaProfeso) 
INNER JOIN asesoriaprofesor ON ( asesorias.idAsesorias = asesoriaprofesor.idAsesorias )
INNER JOIN profesor ON ( profesor.idProfesor = asesoriaprofesor.idProfesor )
INNER JOIN usuario ON ( usuario.idUsuario = profesor.usuario_idUsuario )
INNER JOIN profesorcurso ON (profesor.idProfesor = profesorcurso.idProfesor)
INNER JOIN curso ON ( curso.idCurso = profesorcurso.idCurso)
INNER JOIN profesorcarrera ON ( profesor.idProfesor = profesorcarrera.idProfesor)
INNER JOIN carrera ON ( carrera.idCarrera = profesorcarrera.idCarrera)
INNER JOIN consultas ON ( consultas.idCita = cita.idCita )
;