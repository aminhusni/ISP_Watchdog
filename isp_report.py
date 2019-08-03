from ubidots import ApiClient
import configparser
from pythonping import ping

#Load from config file
config = configparser.ConfigParser()
config.read('config.py')
wdconfig = config['isp_watchdog']
API_Key = wdconfig['API_Key']

#Ready variables from config files
Heartbeat = wdconfig['Heartbeat']
Variable_1 = wdconfig['Variable_1']
IP_1 = wdconfig['IP_1']
Variable_2 = wdconfig['Variable_2']
IP_2 = wdconfig['IP_2']
Variable_3 = wdconfig['Variable_3']
IP_3 = wdconfig['IP_3']

#Connect to Ubidots API
api = ApiClient(token=API_Key)

#Begin to ping with size of 64 bytes (standard)
ping1 = ping(IP_1, size=64)
ping2 = ping(IP_2, size=64)
ping3 = ping(IP_3, size=64)


#Upload ping results
api.save_collection([{'variable': Heartbeat, 'value': 1}, {'variable': Variable_1, 'value': ping1.rtt_avg_ms}, {'variable': Variable_2, 'value': ping2.rtt_avg_ms}, {'variable': Variable_3, 'value': ping3.rtt_avg_ms}])
