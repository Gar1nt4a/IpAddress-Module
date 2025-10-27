import requests
import random


def get_external_ip():
    ip_services = [
        'https://api.ipify.org',
        'https://ident.me',
        'https://checkip.amazonaws.com',
        'https://ipinfo.io/ip',
        'https://ifconfig.me/ip',
        'https://icanhazip.com'
    ]

    random.shuffle(ip_services)

    for service in ip_services:
        try:
            response = requests.get(service, timeout=5)
            if response.status_code == 200:
                ip = response.text.strip()
                if ip.count('.') == 3 and not ip.startswith(('127.', '192.168.', '10.', '172.')):
                    return ip
        except (requests.exceptions.RequestException, requests.exceptions.Timeout):
            continue

    try:
        response = requests.get('https://api.ipify.org', timeout=10)
        return response.text.strip()
    except (requests.exceptions.RequestException, requests.exceptions.Timeout):
        return None


IpAddress = get_external_ip()