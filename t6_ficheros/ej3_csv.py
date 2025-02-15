import csv

# Usando csv_reader para leer un fichero csv con cabecera
with open("files/estudiantes.csv", newline="", encoding="utf-8") as file:
    csv_reader = csv.reader(file)
    cabecera = next(csv_reader)
    print("Cabecera:", cabecera)
    for fila in csv_reader:
        estudiante_dict = dict(zip(cabecera, fila))
        print(estudiante_dict)

# Usando dict_reader para leer un fichero csv con cabecera
with open("files/estudiantes.csv", newline="", encoding="utf-8") as file:
    dict_reader = csv.DictReader(file)
    for estudiante in dict_reader:
        print(
            f'{estudiante["Nombre"]} estudia {estudiante["Carrera"]}, tiene {estudiante["Edad"]} años'
        )
