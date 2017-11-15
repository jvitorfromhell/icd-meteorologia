input_file = open("dados_original_bdmep_semcabecalho.txt", 'r')

for line in input_file:
	print line.replace(';', ',').replace(',,', ',0,').replace(',,', ',0,').replace(',\n','')