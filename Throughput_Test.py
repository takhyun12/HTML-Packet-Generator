from time import *
from random import *
import string
import threading
import datetime
import requests

def Generate_Packet():
    header_len = uniform(10.0, 36.5)
    arrival_time = datetime.datetime.now()
    dev_eui = ''
    for i in range(8):
        dev_eui += choice(string.ascii_letters + string.digits)  # payload 생성
    app_eui = '0000000000000020'
    direction = 'up'
    proto = 'LoRaWAN'
    action = 'Accept'
    lorawan_mac_hdr = randint(50, 100)
    lorawan_frm_hdr = '0000f01b800000'
    payload = ''
    phypayload = ''
    for i in range(randint(18, 25)):
        phypayload += choice(string.ascii_letters + string.digits)  # payload 생성
    payload_len = round(len(phypayload))
    pktlen = '22'
    fport = '422'
    mtype = '010'
    dev_addr = '00000000000020'
    fctrl = randint(50, 100)
    fcnt = 0000
    fopts = ''
    gwsnr = uniform(3.0, 5.0)
    gwrssi = randint(1, 10)
    gweui = '0000000000000000'
    gwlati = '0000000000000000'
    gwlong = '0000000000000000'
    gwalti = '0'
    createdTime = str(datetime.datetime.now())
    packet_header = {
        'Content-Type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'Postman-Token': "1f6bd319-7d72-4f1c-8a65-6dbe88b7eaa2"
    }

    packet_payload = "DevEUI=" + str(dev_eui) + "\
             &AppEUI=" + str(app_eui) + "\
             &FPort=" + str(fport) + "\
             &DevAddr=" + str(dev_addr) + "\
             &PHYPayload=" + str(phypayload) + "\
             &createdTime=" + str(createdTime) + "\
             &contentSize=30 \
             &gwInfo=gwEUI%3A%200000000000000003%20Lati%3A37.38213%20Long%3A127.11654%20Alti%3A78%20i \
             Rssi%3A1233.5%20Snr%3A254.1%3B%0AgwEUI%3A%200000000000000003%20Lati%3A37.38654%20 \
             Long%3A127.11517%20Alti%3A70%20Rssi%3A1212.5%20Snr%3A210.1%3B%0 \
             AgwEUI%3A%200000000000000003%20Lati%3A37.38743%20 \
             Long%3A127.11234%20Alti%3A72%20Rssi%3A1135.5%20Snr%3A201.1%3B"

    return packet_header, packet_payload

def Simulation(packet_count, packet_interval):
    server_url = 'http://117.16.136.97:4443'
    for packet_number in range(0, packet_count):
        packet_header, packet_payload = Generate_Packet()
        response = requests.request("POST", server_url, data=packet_payload, headers=packet_header)
        response_code = response.text[-2:-1]

        print(str(packet_header))
        sleep(packet_interval)

packet_count = 10000
packet_interval = 0
bots = 10

for i in range(10):
    threading.Thread(target=Simulation, args=(packet_count, packet_interval)).start()
