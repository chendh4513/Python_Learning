import requests

url = 'http://10.9.1.3/a79.htm?wlanuserip=10.70.237.243&wlanacname=&wlanacip=221.178.234.24'

header = {
'Accept': '*/*',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Connection': 'keep-alive',
'Cookie': 'PHPSESSID=l6ch73s300ij3uir2ibeh12ihu',
'Host': '10.9.1.3:801',
'Referer': 'http://10.9.1.3/a79.htm?wlanuserip=10.70.237.243&wlanacname=&wlanacip=221.178.234.24',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
}

data = {
'c': 'Portal',
'a': 'login',
'callback': 'dr1003',
'login_method': '1',
'user_account': ',b,1809404007',
'user_password': '11054513',
'wlan_user_ip': '10.70.237.243',
'wlan_user_ipv6': '',
'wlan_user_mac': '000000000000',
'wlan_ac_ip': '221.178.234.24',
'wlan_ac_name':'',
'jsVersion': '3.3.3',
}

response = requests.post(url, data, headers=header).status_code

print("回应代码")
