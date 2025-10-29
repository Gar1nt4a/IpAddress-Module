import socket
import random

def get_external_ip():
    dns_servers = [
        '8.8.8.8',
        '8.8.4.4',
        '1.1.1.1',
        '1.0.0.1',
        '9.9.9.9',
        '149.112.112.112',
        '208.67.222.222',
        '208.67.220.220',
        '64.6.64.6',
        '64.6.65.6',
        '84.200.69.80',
        '84.200.70.40',
        '8.26.56.26',
        '8.20.247.20',
        '195.46.39.39',
        '195.46.39.40',
        '77.88.8.8',
        '77.88.8.1',
        '176.103.130.130',
        '176.103.130.131',
        '156.154.70.1',
        '156.154.71.1',
        '198.101.242.72',
        '23.253.163.53',
        '216.146.35.35',
        '216.146.36.36',
        '37.235.1.174',
        '37.235.1.177',
        '89.233.43.71',
        '91.239.100.100',
        '74.82.42.42',
        '109.69.8.51'
    ]

    random.shuffle(dns_servers)

    for dns_server in dns_servers:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                s.settimeout(5)
                s.connect((dns_server, 53))
                ip = s.getsockname()[0]
                if ip and ip.count('.') == 3 and not ip.startswith(('127.', '192.168.', '10.', '172.')):
                    return ip
        except:
            continue

    return None

IpAddress = get_external_ip()
