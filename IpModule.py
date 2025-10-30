import requests


def get_ip():
    sites = [
        'https://api.ipify.org',
        'https://ident.me',
        'https://checkip.amazonaws.com'
    ]

    for site in sites:
        try:
            return requests.get(site, timeout=1).text.strip()
        except:
            continue
    return "ошибка"


IpAddress = get_ip()
