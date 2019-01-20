#  _                          _                      ___                           
# | |                        | |                    |_  |                          
# | |      __ _   __ _   ___ | |_    __ _ __   __     | |  ___   _ __    __ _  ___ 
# | |     / _` | / _` | / _ \| __|  / _` |\ \ / /     | | / _ \ | '_ \  / _` |/ __|
# | |____| (_| || (_| ||  __/| |_  | (_| | \ V /  /\__/ /| (_) || | | || (_| |\__ \
# \_____/ \__,_| \__, | \___| \__|  \__,_|  \_/   \____/  \___/ |_| |_| \__,_||___/
#                 __/ |                                                            
#                |___/                                                                                                                                                                                                             
# En liten fil som gir deg tips om hvordan bruke "Sensor Board for Micro:bit" fra kitronic.
# Mer info om kortet --> https://www.monkmakes.com/mb_sensor/
# Mikrofon er koblet til pin 0
# Termometer er koblet til pin 1
# Lys-sensor er koblet til pin 2

from microbit import *

# ********************** FUNKSJONER **********************************
# Funksjon som viser sinna fjes når lyden er over et gitt nivå (y)
def skrik(value):	
	y = 1
	if value > y:
		display.show(Image.ANGRY)
		sleep(500)
		display.clear()
	else: 
		display.show(Image.HAPPY)
		sleep(500)
		display.clear()


# ********************** STARTER EN LOOP   ****************************
while True:	
	# Viser lydnivået i tall mellom 1,5 og -1,5 ?? Sender til funksjonen skrik()
	# Denne mikrofonen er ikke veldig bra. Reagerer best på skarpe lyder (klapp etc)
	if button_a.is_pressed():
		display.clear()
		lyd = (pin0.read_analog() - 511) / 100
		#display.scroll(str(lyd)) # kan bare scrolle strenger
		skrik(lyd)

	# Viser temperaturen i celsius
	elif button_b.is_pressed():
		display.clear()
		temp = pin1.read_analog()
		# Regner om spenningen til en celsius verdi
		temp_c = int(temp / 13.33 - 14)
		display.scroll(str(temp_c))

	# Lyssensor (obs - ikke så lett å trykke på begge knappene helt samtidig ...)
	elif button_a.is_pressed() and button_b.is_pressed():
		display.clear()
		# Sensoren returnerer 0 til 1023 hvor 0-3 er mørkt- Verdier over 100 kun utendørs.
		lys = pin2.read_analog()
		# Litt enklere å bruke verdiene om du deler på 10
		lys_2 = lys / 10
		# Runde av til 0 desimaler
		lys_3 = round(lys_2, 0)
		display.scroll(str(lys_3))
