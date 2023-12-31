import requests
from pyfiglet import Figlet

pro = 'd'
while pro == 'd':
    def get_info_by_ip(ip='127.0.0.1'):
        try:
            response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
            # print(response)

            data = {
                '[IP]': response.get('query'),
                '[Int prov]': response.get('isp'),
                '[Org]': response.get('org'),
                '[Country]': response.get('country'),
                '[Region Name]': response.get('regionName'),
                '[City]': response.get('city'),
                '[ZIP]': response.get('zip'),
                '[Lat]': response.get('lat'),
                '[Lon]': response.get('lon'),
            }

            for k, v in data.items():
                print(f'{k} : {v}')

        except requests.exceptions.ConnectionError:
            print('[!] Please check your connection!')


    def main():
        preview_text = Figlet(font='slant_relief')
        print(preview_text.renderText('RUS IP'))
        ip = input('Please enter a target IP: ')

        get_info_by_ip(ip=ip)


    if __name__ == '__main__':
        main()
    pro = input('Please enter "d" next or any key quit: ')
