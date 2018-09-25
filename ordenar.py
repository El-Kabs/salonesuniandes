import json

d = {}
k = {}

with open('salones2.txt', 'r') as f:
    content = f.readlines()
        # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    for x in content:
        k[x] = [{},{},{},{},{},{}]
			
with open("data.json", "rb") as f:
    d = json.load(f)

for key in d.keys():
	lunes = [1]
	martes = [1]
	miercoles = [1]
	jueves = [1]
	viernes = [1]
	sabado= [1]
	for x in d[key]:
		x = str(x)
		if('1'==x):
			pass
		else:
			nArreglo = x.split(";;")
			dia = nArreglo[0]
			horario = nArreglo[1]
			horarioN = horario[:-2]
			if("L" in x):
				lunes.append(horarioN)
			elif("M" in x):
				martes.append(horarioN)
			elif("I" in x):
				miercoles.append(horarioN)
			elif("J" in x):
				jueves.append(horarioN)
			elif("V" in x):
				viernes.append(horarioN)
			elif("S" in x):
				sabado.append(horarioN)
			k[key][0] = (lunes)
			k[key][1] = (martes)
			k[key][2] = (miercoles)
			k[key][3] = (jueves)
			k[key][4] = (viernes)
			k[key][5] = (sabado)


with open('data2.json', 'w') as fp:
    json.dump(k, fp)

with open('data2.json', 'r') as fp:
	data = fp.read().replace('1, ', '')
	print(data)