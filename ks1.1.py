#Màu
den = "\033[1;90m"
luc = "\033[1;32m"
trang = "\033[1;37m"
red = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
lamd = "\033[1;34m"
lam = "\033[1;36m"
purple = "\e[35m"
hong = "\033[1;95m"
# Đánh dấu bản quyền
thanh_xau= trang + "~" + red + "[" + vang+ "⟨⟩" + red + "] " + trang + "➩ "
thanh_dep= trang + "~" + red + "[" + luc + "✓" + red + "] " + trang + "➩ "
##### Cài Thư Viện
import requests, os, sys,json
import socket
try:
        import mechanize
except:
        os.system("pip install mechanize")
        import mechanize
from sys import platform
from datetime import datetime
from time import sleep,strftime
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
import time
import datetime
bug_duoc_cai_lon={'pass':'bongocvidaii'}
datetime_object = datetime.datetime.now()
#IP
def get_ip_from_url(url):
    response = requests.get(url)
    ip_address = socket.gethostbyname(response.text.strip())
    return ip_address
url = "http://kiemtraip.com/raw.php"
ip = get_ip_from_url(url)
def is_connected():
    try:
        import socket
        socket.create_connection(("1.1.1.1", 53))
        return True
    except OSError:
        pass
    return False
headers ={'user-agent':'Mozilla/5.0 (Linux; Android 11; Live 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.28 Mobile Safari/537.36'}
#Logo
banners=f"""
                    ███████╗████████╗ █████╗ ███████╗██╗  ██╗           
                    ██╔════╝╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝       
                    ███████╗   ██║   ███████║███████╗█████╔╝               
                    ╚════██║   ██║   ██╔══██║╚════██║██╔═██╗          
                    ███████║   ██║   ██║  ██║███████║██║  ██╗       
                    ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝      
"""
thongtin=f"""        {luc}Copyright © KINS STASK 2023 🫀 | {vang}Version {hong}1.1 🤞
{red}────────────────────────────────────────────────────────
{tim}             ||||| THÔNG BÁO
{luc}~[●]{red} ➩ {tim}Admin:  {lam}Trung Kiên
{luc}~[●]{lam} Địa chỉ IP hiện tại của bạn là: {red}{ip} 💫
{luc}~[●]{lam} Zalo Support: {red}0338557731
{luc}~[●]{lam} Donate: {red}0338557731
{luc}~[●]{lam} Thời gian hiện tại là: {red}{datetime_object}💭
{red}────────────────────────────────────────────────────────\033[0m"""


def clear ():
    if platform[0:3] == 'lin':
        os.system("clear")
    else:
            os.system("cls")

def banner():
        print('\033[0m',end='')
        clear()
        a=Colorate.Horizontal(Colors.red_to_white, banners)
        for i in range(len(a)):
                sys.stdout.write(a[i])
                sys.stdout.flush()
                #sleep(0.0001)
        print()
        print(thongtin)

try:
        a=f'{red}Vui {luc}Lòng {vang}Chờ{hong}...\033[0m'
        for i in range(len(a)):
                sys.stdout.write(a[i])
                sys.stdout.flush()
                sleep(0.05)
        url=requests.get(f'https://sever.ngocbansub.com/api_by_Ngoc/key.php', headers=headers).json()
        status = url['success']
        ma_key = url['key']
        ip = url['ip']
        link=url['link']
        coun = url['coun']
except:
        print('Sever Key Gặp Lỗi, Hãy Liên Hệ Admin')
        

def bongoc(so):
        a= "────"*so
        for i in range(len(a)):
                sys.stdout.write(a[i])
                sys.stdout.flush()
                sleep(0.003)
        print()

banner()
print(f"""{hong}┏━━━━━━━━━━━━━━━━━━━━━┓
{hong}┃  {vang}Tool {tim}Trao {lam}Đổi {hong}Sub  {red}┃
{red}┗━━━━━━━━━━━━━━━━━━━━━┛ """)
print(f'{thanh_xau}{luc}Nhập {hong}[{vang}1{red}] {luc}Để Chạy Tool Cày Xu TDS Facebook {vang}[v1]')
print(f'{thanh_xau}{luc}Nhập {hong}[{vang}2{red}] {luc}Để Chạy Tool Cày Xu TDS Tiktok')
print(f'{thanh_xau}{luc}Nhập {hong}[{vang}3{red}] {luc}Để Chạy Tool Cày Xu TDS Facebook Pro5')
bongoc(14)
print(f"""{hong}┏━━━━━━━━━━━━━━━━━━━━━━━┓
{hong}┃  {vang}Tool {tim}Tương {lam}Tác {hong}Chéo  {red}┃
{red}┗━━━━━━━━━━━━━━━━━━━━━━━┛""")
print(f'{thanh_xau}{luc}Nhập {hong}[{vang}4{red}] {luc}Để Chạy Tool Cày Xu TTC Tiktok [Lỗi]')
print(f'{thanh_xau}{luc}Nhập {hong}[{vang}5{red}] {luc}Để Chạy Tool Cày Xu TTC Vipig{red}')
bongoc(14)
print(f"""{hong}┏━━━━━━━━━━━━━━━━━┓
{hong}┃  {vang}Tiện {tim}Ích {lam}Khác  {red}┃
{red}┗━━━━━━━━━━━━━━━━━┛""")
print(f'{thanh_xau}{luc}Nhập {hong}[{vang}6{red}] {luc}Để Chạy Tool Get Token Pro5 ')
print(f'{thanh_xau}{luc}Nhập {hong}[{vang}7{red}] {luc}Để Chạy Tool Reg Page Pro5 ')
print(f'{thanh_xau}{luc}Nhập {hong}[{vang}8{red}] {luc}Để Chạy Tool Buff Follow Bằng Page Pro5 ')
print(f'{thanh_xau}{luc}Nhập {hong}[{vang}9{red}] {luc}Để Chạy Tool Buff View Story Bằng Page Pro5 {red}')
print(f'{thanh_xau}{luc}Nhập {hong}[{vang}10{red}] {luc}Để Chạy Tool Spam SMS {red}')
print(f'{thanh_xau}{luc}Nhập {hong}[{vang}11.1{red}] {luc}Để Chạy Tool Buff View Ảo TikTok {red}')
print(f'{thanh_xau}{luc}Nhập {hong}[{vang}11.2{red}] {luc}Để Chạy Tool Buff Tim Ảo TikTok {red}')
print(f'{thanh_xau}{luc}Nhập {hong}[{vang}12{red}] {luc}Để Chạy Tool Encode {red}')
bongoc(14)
print(f"""{hong}┏━━━━━━━━━━━━━━━━━┓
{hong}┃{vang}Tiện {tim}Ích {lam}Facebook{red}┃
{red}┗━━━━━━━━━━━━━━━━━┛""")
print(f'{thanh_xau}{luc}Nhập {hong}[{vang}14{red}] {luc}Để Chạy Tool Spam Messenger Bằng Page Pro5 ')
bongoc(14)
print(f"""{hong}┏━━━━━━━━━━━━━━━━━┓
{hong}┃  {vang}Thoát {tim}Tools    {red}┃
{red}┗━━━━━━━━━━━━━━━━━┛""")
print(f'{thanh_xau}{luc}Nhập {hong}[{vang}15{red}] {luc}Để Thoát Tools')
bongoc(14)

chon = input(f'{thanh_xau}{luc}Nhập Số {trang}: {vang}')
try:
        if chon == '1':
                run = requests.post('https://run.mocky.io/v3/1ba6906f-07a8-4b9f-9b2b-63f658b0af80', headers=headers, data=bug_duoc_cai_lon).text
        elif chon == '2':
                run = requests.post('https://run.mocky.io/v3/2c1438a7-4844-42f0-8282-90591d07b717', headers=headers, data=bug_duoc_cai_lon).text
        elif chon == '3':
                run = requests.post('https://run.mocky.io/v3/d1b21a5a-9fcd-4e8d-aba0-79b47e9c6d4b', headers=headers, data=bug_duoc_cai_lon).text
        elif chon == '4':
                run = requests.post('https://sever.ngocbansub.com/python/ttctik.php', headers=headers, data=bug_duoc_cai_lon).text
        elif chon == '5':
                run = requests.post('https://run.mocky.io/v3/f76e3c29-3ccb-4f92-8c91-b5b6dcc68c6b', headers=headers, data=bug_duoc_cai_lon).text
        elif chon == '6':
                run = requests.post('https://run.mocky.io/v3/eb5ca80e-d59d-49e3-9dc5-80b831264007', headers=headers, data=bug_duoc_cai_lon).text
        elif chon == '7':
                run = requests.post('https://run.mocky.io/v3/accb7665-9819-4cd4-aa93-826a2c70fd5a', headers=headers, data=bug_duoc_cai_lon).text
        elif chon == '8':
                run = requests.post('https://run.mocky.io/v3/258ea6fd-8dc0-4e76-9881-1f4a1a358c54', headers=headers, data=bug_duoc_cai_lon).text
        elif chon == '9':
                run = requests.post('https://run.mocky.io/v3/14a346b0-0411-4d97-9b01-d0d645561195', headers=headers, data=bug_duoc_cai_lon).text
        elif chon == '10':
                run = requests.post('https://run.mocky.io/v3/3a3048c5-8748-434b-9b36-743dab294fc0', headers=headers, data=bug_duoc_cai_lon).text
        elif chon == '11.1':
          run = requests.post('https://run.mocky.io/v3/ca1632cf-d88c-4d04-a6f4-6494775426b4', headers=headers, data=bug_duoc_cai_lon).text
        elif chon == '11.2':
          run = requests.post('https://run.mocky.io/v3/9978ce95-fff2-4418-bfa2-5784544c5225', headers=headers, data=bug_duoc_cai_lon).text
        elif chon == '12':
                run = requests.post('https://run.mocky.io/v3/80db8304-6848-429f-8eab-845055d3ba86', headers=headers, data=bug_duoc_cai_lon).text
        elif chon == '14':
                run = requests.post('https://run.mocky.io/v3/ff15070a-80bf-4bcb-b63c-6d659f5904ef', headers=headers, data=bug_duoc_cai_lon).text 
        elif chon == '15':
                run = requests.post('https://run.mocky.io/v3/13ff7ee8-0748-4c62-814b-604e7182b6fb', headers=headers, data=bug_duoc_cai_lon).text
        else:
                run = "print(red+'Lựa Chọn Không Xác Định') "
except:
        if not is_connected():
                print(red+'Hãy Kiểm Tra Kết Nối Mạng !!! ')
        else:
                print (red+'Sever Gặp Lỗi Hãy Liên Hệ Admin !!! ')
       
exec(run)
