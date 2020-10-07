import urequests as requests
import config
import machine
import time


def do_connect():
	import network
	wlan = network.WLAN(network.STA_IF)
	wlan.active(True)
	if not wlan.isconnected():
		print('connecting to network...')
		wlan.connect(config.wifi_ssid, config.wifi_password)
		while not wlan.isconnected():
			pass
	print('network config:', wlan.ifconfig())

do_connect()

button = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)

endpoint_ip = config.endpoint_ip_address
http_url = "http://" + endpoint_ip + "/putxml"

headers = {'Authorization': 'Basic AUTHGOESHERE', 
			'Content-Type': 'application/xml'
			} 

xml = """
<Command>
    <Audio>
        <Microphones>
            <ToggleMute command='True'>
            </ToggleMute>
        </Microphones>
    </Audio>
</Command>
"""

def sendMuteToggle():
	requests.post(http_url, headers=headers, data=xml)
	return


while True:
	if not button.value():
		print("Detected button press. Sending mute")
		try:
			sendMuteToggle()
		except:
			pass
		


