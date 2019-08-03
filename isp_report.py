from ubidots import ApiClient
import configparser
from pythonping import ping

config = configparser.ConfigParser()
config.read('config.py')
wdconfig = config['isp_watchdog']
API_Key = wdconfig['API_Key']

Variable_1 = wdconfig['Variable_1']
IP_1 = wdconfig['IP_1']
Variable_2 = wdconfig['Variable_2']
IP_2 = wdconfig['IP_2']
Variable_3 = wdconfig['Variable_3']
IP_3 = wdconfig['IP_3']

api = ApiClient(token=API_Key)

var1 = api.get_variable(Variable_1)
var2 = api.get_variable(Variable_2)
var3 = api.get_variable(Variable_3)

ping1 = ping(IP_1, size=64)
ping2 = ping(IP_2, size=64)
ping3 = ping(IP_3, size=64)

api.save_collection([{'variable': Variable_1, 'value': ping1.rtt_avg_ms}, {'variable': Variable_2, 'value': ping2.rtt_avg_ms}, {'variable': Variable_3, 'value': ping3.rtt_avg_ms}])
