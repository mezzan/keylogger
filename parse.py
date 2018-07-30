import re

keymaps_default_dict = {}
keymaps_shift_dict = {}
keymaps_altgr_dict = {}

def create_keymaps_dict(type):
	keymaps = open('./keymaps/keymaps_' + type + '.txt', 'r')
	keymaps_lines = keymaps.readlines()

	temp_dict = {}

	for line in keymaps_lines:
		#cerco l'inizio e la fine del keycode
		start_digit = re.search('\d', line)
		end_digit = line.rfind(' ')

		temp_dict[line[start_digit.start():end_digit]] = line[end_digit + 1 : len(line) - 1]

	keymaps.close()

	return temp_dict


def clean_logger():
	final_logger = open('final_logger.txt', 'w')

	logger_temp = open('logger_temp.txt', 'r')
	logger_temp_lines = logger_temp.readlines()
	logger_temp.close()

	for count, line in enumerate(logger_temp_lines):

		#se line è la data, la inserrisco nel final logger
		if 'CEST' in line and count + 6 < len(logger_temp_lines) and 'CEST' not in logger_temp_lines[count + 6]:
			final_logger.write(line)
				
		#verifico se è stato premuto un tasto
		elif 'premuto' in line:
			
			#se il tasto premuto è diverso da shift-L, shift-R, AltGr allora inserisco line
			if '42' not in line and '54' not in line and '100' not in line:
				final_logger.write(line)
			
			#se il tasto premuto è shift-L, shift-R o AltGr allora verifico che non sia già stato 
			#inserito al passo precedente lo stesso avviso
			elif line != logger_temp_lines[count - 1]:
				final_logger.write(line)
		
		#se un tasto viene rilasciato, nel final_logger lo inserisco solo se il
		#il tasto in questione è shift-L, shift-R p AltGr
		elif 'rilasciato' in line:
			if '42' in line or '54' in line or '100' in line:
				final_logger.write(line)

	final_logger.close()


 
output = open('output.txt', 'w')

#crea il dizionario dei keycode
keymaps_default_dict = create_keymaps_dict('default')
keymaps_shift_dict = create_keymaps_dict('shift')
keymaps_altgr_dict = create_keymaps_dict('altgr')

#variabili che indicano se i tasti shift-L, shift-R, AltGr sono premuti
shift_pressed = False
alt_gr_pressed = False
caps_lock_pressed = False

clean_logger()
logger = open('final_logger.txt', 'r')

for line in logger.readlines():
	#se line contiene la data, viene inserita nell'output
	if 'CEST' in line:
		output.write('\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n' + line + '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')

	else:
		#cerco gli indici del keycode
		start_digit = re.search('\d', line)
		end_digit = line.rfind(' ')

		keycode = line[start_digit.start():end_digit]

		#output.write(keymaps_default_dict[keycode])

		if 'rilasciato' in line:
			if keycode == '42' or keycode == '54':
				shift_pressed = False
			elif keycode == '100':
				alt_gr_pressed = False

		#verifico è stato premuto il tasto shift-L o shift-R o AltGr
		elif 'premuto' in line:
			if keycode == '42' or keycode == '54': 
				shift_pressed = True 
			elif keycode == '58':
				caps_lock_pressed = not caps_lock_pressed
			elif keycode == '100':
				alt_gr_pressed = True
			else:
				if shift_pressed == True:
					temp_value = keymaps_shift_dict[keycode]
				elif alt_gr_pressed == True:
					temp_value = keymaps_altgr_dict[keycode]
				else:
					temp_value = keymaps_default_dict[keycode]

				if caps_lock_pressed:
					temp_value = temp_value.upper()
				
				output.write(temp_value)
		else:
			print('Parse-Error: unknown line.')




logger.close()
output.close()

