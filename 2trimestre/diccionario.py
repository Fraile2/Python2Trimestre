alumno1={
    "Nombre": "Alejandro",
    "Edad":20,
    "Soltero": False
}

alumno1["Apellidos"]="Fraile"
print(alumno1)

alumno1["Apellidos"]="Fraile del Olmo"
for item in alumno1:
    print(alumno1[item])