from time import *
from random import *
import string
import threading
import datetime
import requests

class HTTP_Request(object):
    def __init__(self, port, dev_eui):
        self.url = 'http://117.16.136.97:4443'
        # LoRaWAN 패킷 구조 정의
        self.header_len = uniform(10.0, 36.5)
        self.arrival_time = datetime.datetime.now()
        self.dev_eui = dev_eui
        self.app_eui = '0000000000000020'
        self.direction = 'up'
        self.proto = 'LoRaWAN'
        self.action = 'Accept'
        self.lorawan_mac_hdr = randint(50, 100)
        self.lorawan_frm_hdr = '0000f01b800000'
        self.payload = ''
        self.phypayload = ''
        for i in range(randint(18, 25)):
            self.phypayload += choice(string.ascii_letters + string.digits)  # payload 생성
        self.payload_len = round(len(self.payload) / 2)
        self.pktlen = '22'
        self.fport = port
        self.mtype = '010'
        self.dev_addr = '00000000000020'
        self.fctrl = randint(50, 100)
        self.fcnt = 0000
        self.fopts = ''
        self.gwsnr = uniform(3.0, 5.0)
        self.gwrssi = randint(1, 10)
        self.gweui = '0000000000000000'
        self.gwlati = '0000000000000000'
        self.gwlong = '0000000000000000'
        self.gwalti = '0'
        self.createdTime = str(datetime.datetime.now())

        self.payload = "DevEUI=" + str(self.dev_eui) + "\
                 &AppEUI=" + str(self.app_eui) + "\
                 &FPort=" + str(self.fport) + "\
                 &DevAddr=" + str(self.dev_addr) + "\
                 &PHYPayload=" + str(self.phypayload) + "\
                 &createdTime=" + str(self.createdTime) + "\
                 &contentSize=30 \
                 &gwInfo=gwEUI%3A%200000000000000003%20Lati%3A37.38213%20Long%3A127.11654%20Alti%3A78%20i \
                 Rssi%3A1233.5%20Snr%3A254.1%3B%0AgwEUI%3A%200000000000000003%20Lati%3A37.38654%20 \
                 Long%3A127.11517%20Alti%3A70%20Rssi%3A1212.5%20Snr%3A210.1%3B%0 \
                 AgwEUI%3A%200000000000000003%20Lati%3A37.38743%20 \
                 Long%3A127.11234%20Alti%3A72%20Rssi%3A1135.5%20Snr%3A201.1%3B"
        self.headers = {
            'Content-Type': "application/x-www-form-urlencoded",
            'cache-control': "no-cache",
            'Postman-Token': "1f6bd319-7d72-4f1c-8a65-6dbe88b7eaa2"
            }

    def Message_Simulation(self, limit, interval):
        for msg_count in range(0, limit):
            try:
                response = requests.request("POST", self.url, data=self.payload, headers=self.headers)
                response_code = response.text[-2:-1]
                #print('[>] Request : '+  self.payload.replace(' ','*'))
                print('[>] Response code : ' + response_code.replace('9','0'))
                sleep(interval)  # 지정한 주기만큼 대기
            except: pass

def Legitimate_Traffic(bot):
    for i in range(bot):
        threading.Thread(target=HTTP_Request('80', 'QWIDMC123123ddqd123').Message_Simulation, args=(100000, 10)).start()
        threading.Thread(target=HTTP_Request('443', '129CNDSVJQQWQCZXQQQ').Message_Simulation, args=(100000, 15)).start()
        threading.Thread(target=HTTP_Request('443', 'vfkdvw8QWD11233W12C').Message_Simulation, args=(100000, 17)).start()
        threading.Thread(target=HTTP_Request('443', 'C128DMVFV9812DQWDQ').Message_Simulation, args=(100000, 20)).start()
        threading.Thread(target=HTTP_Request('443', '12DJCJC123412UDCJC').Message_Simulation, args=(100000, 14)).start()
        threading.Thread(target=HTTP_Request('8080', '1239FCMJV9121D3DF').Message_Simulation, args=(100000, 60)).start()

Legitimate_Traffic(bot=1)