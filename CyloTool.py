#!/usr/bin/python

import random
import requests
from time import sleep
import os, signal, sys
from rich.console import Console
from rich.prompt import Prompt, IntPrompt
from rich.text import Text
from rich.style import Style
import pystyle
from pystyle import Colors, Colorate

from cylo import Bubcyz

__CHANNEL_USERNAME__ = "CyloToolChannel"
__GROUP_USERNAME__   = "CyloToolChat"

def signal_handler(sig, frame):
    print("\n Bye Bye...")
    sys.exit(0)

def gradient_text(text, colors):
    lines = text.splitlines()
    height = len(lines)
    width = max(len(line) for line in lines)
    colorful_text = Text()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != ' ':
                color_index = int(((x / (width - 1 if width > 1 else 1)) + (y / (height - 1 if height > 1 else 1))) * 0.5 * (len(colors) - 1))
                color_index = min(max(color_index, 0), len(colors) - 1)  # Ensure the index is within bounds
                style = Style(color=colors[color_index])
                colorful_text.append(char, style=style)
            else:
                colorful_text.append(char)
        colorful_text.append("\n")
    return colorful_text

def banner(console):
    os.system('cls' if os.name == 'nt' else 'clear')    
    
    brand_name =  "                ╔═══╗───╔╗──╔════╗────╔╗\n"
    brand_name += "                ║╔═╗║───║║──║╔╗╔╗║────║║\n"
    brand_name += "                ║║─╚╬╗─╔╣║╔═╩╣║║╠╩═╦══╣║\n"
    brand_name += "                ║║─╔╣║─║║║║╔╗║║║║╔╗║╔╗║║\n"
    brand_name += "                ║╚═╝║╚═╝║╚╣╚╝║║║║╚╝║╚╝║╚╗\n"
    brand_name += "                ╚═══╩═╗╔╩═╩══╝╚╝╚══╩══╩═╝\n"
    brand_name += "                ────╔═╝║\n"
    brand_name += "                ────╚══╝\n"
    colors = [
        "rgb(255,0,0)", "rgb(255,69,0)", "rgb(255,140,0)", "rgb(255,215,0)", "rgb(173,255,47)", 
        "rgb(0,255,0)", "rgb(0,255,255)", "rgb(0,191,255)", "rgb(0,0,255)", "rgb(139,0,255)",
        "rgb(255,0,255)"
    ]
    colorful_text = gradient_text(brand_name, colors)
    console.print(colorful_text)
    print(Colorate.Horizontal(Colors.rainbow, '=================================================================='))
    print(Colorate.Horizontal(Colors.rainbow, '\t              กรุณาออกจากระบบ cpm ก่อนที่จะใช้เครื่องมือนี้'))
    print(Colorate.Horizontal(Colors.rainbow, '        ไม่อนุญาตให้แชร์รหัสการเข้าถึงของคุณและอาจทำให้คุณถูกบล็อกได้'))
    print(Colorate.Horizontal(Colors.rainbow, f' ‌          โทรเลข: @{__CHANNEL_USERNAME__} 𝐎𝐫 @{__GROUP_USERNAME__}'))
    print(Colorate.Horizontal(Colors.rainbow, '=================================================================='))

def load_player_data(cpm):
    response = cpm.get_player_data()
    if response.get('ok'):
        data = response.get('data')
        if 'floats' in data and 'localID' in data and 'money' in data and 'coin' in data:
        
            print(Colorate.Horizontal(Colors.rainbow, '==========[ รายละเอียดผู้เล่น ]=========='))
            
            print(Colorate.Horizontal(Colors.rainbow, f'ชื่อ       : {(data.get("Name") if "Name" in data else "UNDEFINED")}.'))
                
            print(Colorate.Horizontal(Colors.rainbow, f'รหัสท้องถิ่น : {data.get("localID")}.'))
            
            print(Colorate.Horizontal(Colors.rainbow, f'เงิน       : {data.get("money")}.'))
            
            print(Colorate.Horizontal(Colors.rainbow, f'เหรียญ    : {data.get("coin")}.'))
            
        else:
            print(Colorate.Horizontal(Colors.rainbow, '- ข้อผิดพลาด: บัญชีใหม่ส่วนใหญ่ต้องลงชื่อเข้าใช้เกมอย่างน้อยหนึ่งครั้ง !.'))
            exit(1)
    else:
        print(Colorate.Horizontal(Colors.rainbow, '- ข้อผิดพลาด: ดูเหมือนว่าการเข้าสู่ระบบของคุณไม่ได้ตั้งค่าอย่างถูกต้อง !.'))
        exit(1)


def load_key_data(cpm):

    data = cpm.get_key_data()
    
    print(Colorate.Horizontal(Colors.rainbow, '========[ เข้าถึงรายละเอียดที่สำคัญ ]========'))
    
    print(Colorate.Horizontal(Colors.rainbow, f'คีย์การเข้าถึง : {data.get("access_key")}.'))
    
    print(Colorate.Horizontal(Colors.rainbow, f'รหัสโทรเลข : {data.get("telegram_id")}.'))
    
    print(Colorate.Horizontal(Colors.rainbow, f'สมดุล      : {(data.get("coins") if not data.get("is_unlimited") else "Unlimited")}.'))
        
    

def prompt_valid_value(content, tag, password=False):
    while True:
        value = Prompt.ask(content, password=password)
        if not value or value.isspace():
            print(Colorate.Horizontal(Colors.rainbow, f'{tag} ไม่สามารถเว้นว่างหรือเว้นวรรคได้ โปรดลองอีกครั้ง'))
        else:
            return value
            
def load_client_details():
    response = requests.get("http://ip-api.com/json")
    data = response.json()
    print(Colorate.Horizontal(Colors.rainbow, '=============[ ที่ตั้ง ]============='))
    print(Colorate.Horizontal(Colors.rainbow, f'ที่อยู่ไอพี   : {data.get("query")}.'))
    print(Colorate.Horizontal(Colors.rainbow, f'ที่ตั้ง      : {data.get("city")} {data.get("regionName")} {data.get("countryCode")}.'))
    print(Colorate.Horizontal(Colors.rainbow, f'ประเทศ    : {data.get("country")} {data.get("zip")}.'))
    print(Colorate.Horizontal(Colors.rainbow, '===============[ เมนู ]==============='))

def interpolate_color(start_color, end_color, fraction):
    start_rgb = tuple(int(start_color[i:i+2], 16) for i in (1, 3, 5))
    end_rgb = tuple(int(end_color[i:i+2], 16) for i in (1, 3, 5))
    interpolated_rgb = tuple(int(start + fraction * (end - start)) for start, end in zip(start_rgb, end_rgb))
    return "{:02x}{:02x}{:02x}".format(*interpolated_rgb)

def rainbow_gradient_string(customer_name):
    modified_string = ""
    num_chars = len(customer_name)
    start_color = "{:06x}".format(random.randint(0, 0xFFFFFF))
    end_color = "{:06x}".format(random.randint(0, 0xFFFFFF))
    for i, char in enumerate(customer_name):
        fraction = i / max(num_chars - 1, 1)
        interpolated_color = interpolate_color(start_color, end_color, fraction)
        modified_string += f'[{interpolated_color}]{char}'
    return modified_string

if __name__ == "__main__":
    console = Console()
    signal.signal(signal.SIGINT, signal_handler)
    while True:
        banner(console)
        acc_email = prompt_valid_value("[bold][?] อีเมลบัญชี[/bold]", "Email", password=False)
        acc_password = prompt_valid_value("[bold][?] รหัสผ่านบัญชี[/bold]", "Password", password=False)
        acc_access_key = prompt_valid_value("[bold][?] คีย์การเข้าถึง[/bold]", "Access Key", password=False)
        console.print("[bold cyan][%] กำลังพยายามเข้าสู่ระบบ[/bold cyan]: ", end=None)
        cpm = Bubcyz(acc_access_key)
        login_response = cpm.login(acc_email, acc_password)
        if login_response != 0:
            if login_response == 100:
                print(Colorate.Horizontal(Colors.rainbow, 'ไม่พบบัญชี'))
                sleep(2)
                continue
            elif login_response == 101:
                print(Colorate.Horizontal(Colors.rainbow, 'รหัสผ่านไม่ถูกต้อง'))
                sleep(2)
                continue
            elif login_response == 103:
                print(Colorate.Horizontal(Colors.rainbow, 'คีย์การเข้าถึงไม่ถูกต้อง'))
                sleep(2)
                continue
            else:
                print(Colorate.Horizontal(Colors.rainbow, 'ลองอีกครั้ง'))
                print(Colorate.Horizontal(Colors.rainbow, '- หมายเหตุ: ตรวจสอบให้แน่ใจว่าคุณได้กรอกข้อมูลครบถ้วนแล้ว !.'))
                sleep(2)
                continue
        else:
            print(Colorate.Horizontal(Colors.rainbow, 'ประสบความสำเร็จ'))
            sleep(2)
        while True:
            banner(console)
            load_player_data(cpm)
            load_key_data(cpm)
            load_client_details()
            choices = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28"]
            print(Colorate.Horizontal(Colors.rainbow, '{01}: เพิ่มเงิน                       1.5K'))
            print(Colorate.Horizontal(Colors.rainbow, '{02}: เพิ่มเหรียญ                     4.5K'))
            print(Colorate.Horizontal(Colors.rainbow, '{03}: อันดับคิง                      8K'))
            print(Colorate.Horizontal(Colors.rainbow, '{04}: เปลี่ยนไอดี                    4.5K'))
            print(Colorate.Horizontal(Colors.rainbow, '{05}: เปลี่ยนชื่อ                      100'))
            print(Colorate.Horizontal(Colors.rainbow, '{06}: เปลี่ยนชื่อ (เรนโบว์)             100'))
            print(Colorate.Horizontal(Colors.rainbow, '{07}: ป้ายทะเบียน                    2K'))
            print(Colorate.Horizontal(Colors.rainbow, '{08}: ลบบัญชี                       FREE'))
            print(Colorate.Horizontal(Colors.rainbow, '{09}: ลงทะเบียนบัญชี                 FREE'))
            print(Colorate.Horizontal(Colors.rainbow, '{10}: ลบเพื่อน                      500'))
            print(Colorate.Horizontal(Colors.rainbow, '{11}: ปลดล็อครถยนต์ที่ต้องชำระเงิน      5k'))
            print(Colorate.Horizontal(Colors.rainbow, '{12}: ปลดล็อครถยนต์ทั้งหมด           6K'))
            print(Colorate.Horizontal(Colors.rainbow, '{13}: ปลดล็อครถไซเรนทั้งหมด          3.5K'))
            print(Colorate.Horizontal(Colors.rainbow, '{14}: ปลดล็อคเครื่องยนต์ w16          4K'))
            print(Colorate.Horizontal(Colors.rainbow, '{15}: ปลดล็อคแตรทั้งหมด             3K'))
            print(Colorate.Horizontal(Colors.rainbow, '{16}: ปลดล็อคปิดการใช้งานความเสียหาย  3K'))
            print(Colorate.Horizontal(Colors.rainbow, '{17}: ปลดล็อกเชื้อเพลิงไม่จำกัด         3K'))
            print(Colorate.Horizontal(Colors.rainbow, '{18}: ปลดล็อคบ้าน 3                 4K'))
            print(Colorate.Horizontal(Colors.rainbow, '{19}: ปลดล็อคควัน                   4K'))
            print(Colorate.Horizontal(Colors.rainbow, '{20}: ปลดล็อคล้อ                    4K'))
            print(Colorate.Horizontal(Colors.rainbow, '{21}: ปลดล็อคแอนิเมชั่น               2K'))
            print(Colorate.Horizontal(Colors.rainbow, '{22}: ปลดล็อคอุปกรณ์ M              3K'))
            print(Colorate.Horizontal(Colors.rainbow, '{23}: ปลดล็อคอุปกรณ์ F              3K'))
            print(Colorate.Horizontal(Colors.rainbow, '{24}: เปลี่ยนการแข่งขันชนะ            1K'))
            print(Colorate.Horizontal(Colors.rainbow, '{25}: เปลี่ยนการแข่งขันแพ้             1K'))
            print(Colorate.Horizontal(Colors.rainbow, '{26}: บัญชีโคลน                    7K'))
            print(Colorate.Horizontal(Colors.rainbow, '{27}: ออโต้อินเนอร์ 414hp            2.5k'))
            print(Colorate.Horizontal(Colors.rainbow, '{28}: มุมที่กำหนดเอง                1.5k'))
            print(Colorate.Horizontal(Colors.rainbow, '{0} : ออก'))
            
            print(Colorate.Horizontal(Colors.rainbow, '===============[ ต่อนาที ]==============='))
            
            service = IntPrompt.ask(f"[bold][?] เลือกบริการ [red][1-{choices[-1]} or 0][/red][/bold]", choices=choices, show_choices=False)
            
            print(Colorate.Horizontal(Colors.rainbow, '===============[ ต่อนาที ]==============='))
            
            if service == 0: # Exit
                print(Colorate.Horizontal(Colors.rainbow, f'ขอขอบคุณที่ใช้เครื่องมือของเรา โปรดเข้าร่วมช่องทางโทรเลขของเรา: @{__CHANNEL_USERNAME__}.'))
            elif service == 1: # Increase Money
                print(Colorate.Horizontal(Colors.rainbow, '[?] ใส่จำนวนเงินที่ต้องการ'))
                amount = IntPrompt.ask("[?] จำนวน")
                console.print("[%] การบันทึกข้อมูลของคุณ: ", end=None)
                if amount > 0 and amount <= 500000000:
                    if cpm.set_player_money(amount):
                        print(Colorate.Horizontal(Colors.rainbow, 'ประสบความสำเร็จ'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] คุณต้องการที่จะออก ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'ขอขอบคุณที่ใช้เครื่องมือของเรา โปรดเข้าร่วมช่องทางโทรเลขของเรา: @{__CHANNEL_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'ล้มเหลว'))
                        print(Colorate.Horizontal(Colors.rainbow, 'โปรดลองอีกครั้ง'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'ล้มเหลว.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'กรุณาใช้ค่าที่ถูกต้อง'))
                    sleep(2)
                    continue
            elif service == 2: # Increase Coins
                print(Colorate.Horizontal(Colors.rainbow, '[?] ใส่จำนวนเหรียญที่คุณต้องการ'))
                amount = IntPrompt.ask("[?] จำนวน")
                console.print("[%] การบันทึกข้อมูลของคุณ: ", end=None)
                if amount > 0 and amount <= 500000:
                    if cpm.set_player_coins(amount):
                        print(Colorate.Horizontal(Colors.rainbow, 'ประสบความสำเร็จ'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] คุณต้องการออกหรือไม่?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'ขอขอบคุณที่ใช้เครื่องมือของเรา โปรดเข้าร่วมช่องทางโทรเลขของเรา: @{__CHANNEL_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'ล้มเหลว.'))
                        print(Colorate.Horizontal(Colors.rainbow, 'โปรดลองอีกครั้ง'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'ล้มเหลว.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'กรุณาใช้ค่าที่ถูกต้อง'))
                    sleep(2)
                    continue
            elif service == 3: # King Rank
                console.print("[bold red][!] Note:[/bold red]: หากอันดับราชาไม่ปรากฏในเกม ให้ปิดแล้วเปิดสองสามครั้ง", end=None)
                console.print("[bold red][!] Note:[/bold red]: โปรดอย่าทำ King Rank ในบัญชีเดียวกันสองครั้ง", end=None)
                sleep(2)
                console.print("[%] มอบตำแหน่งกษัตริย์ให้กับคุณ: ", end=None)
                if cpm.set_player_rank():
                    print(Colorate.Horizontal(Colors.rainbow, 'ประสบความสำเร็จ'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] คุณต้องการออกหรือไม่?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'ขอขอบคุณที่ใช้เครื่องมือของเรา โปรดเข้าร่วมช่องทางโทรเลขของเรา: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'ล้มเหลว.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'โปรดลองอีกครั้ง'))
                    sleep(2)
                    continue
            elif service == 4: # Change ID
                print(Colorate.Horizontal(Colors.rainbow, '[?] ป้อนรหัสใหม่ของคุณ'))
                new_id = Prompt.ask("[?] บัตรประจำตัวประชาชน")
                console.print("[%] การบันทึกข้อมูลของคุณ: ", end=None)
                if len(new_id) >= 0 and len(new_id) <= 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999 and (' ' in new_id) == False:
                    if cpm.set_player_localid(new_id.upper()):
                        print(Colorate.Horizontal(Colors.rainbow, 'ประสบความสำเร็จ'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] คุณต้องการออกหรือไม่?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'ขอขอบคุณที่ใช้เครื่องมือของเรา โปรดเข้าร่วมช่องทางโทรเลขของเรา: @{__CHANNEL_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'ล้มเหลว.'))
                        print(Colorate.Horizontal(Colors.rainbow, 'โปรดลองอีกครั้ง'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'ล้มเหลว.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'กรุณาใช้บัตรประจำตัวที่ถูกต้อง'))
                    sleep(2)
                    continue
            elif service == 5: # Change Name
                print(Colorate.Horizontal(Colors.rainbow, '[?] ป้อนชื่อใหม่ของคุณ'))
                new_name = Prompt.ask("[?] ชื่อ")
                console.print("[%] การบันทึกข้อมูลของคุณ: ", end=None)
                if len(new_name) >= 0 and len(new_name) <= 999999999:
                    if cpm.set_player_name(new_name):
                        print(Colorate.Horizontal(Colors.rainbow, 'ประสบความสำเร็จ'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] คุณต้องการออกหรือไม่?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'ขอขอบคุณที่ใช้เครื่องมือของเรา โปรดเข้าร่วมช่องทางโทรเลขของเรา: @{__CHANNEL_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'ล้มเหลว.'))
                        print(Colorate.Horizontal(Colors.rainbow, 'โปรดลองอีกครั้ง'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'ล้มเหลว.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'กรุณาใช้ค่าที่ถูกต้อง'))
                    sleep(2)
                    continue
            elif service == 6: # Change Name Rainbow
                print(Colorate.Horizontal(Colors.rainbow, '[?] ป้อนชื่อ Rainbow ใหม่ของคุณ'))
                new_name = Prompt.ask("[?] ชื่อ")
                console.print("[%] การบันทึกข้อมูลของคุณ: ", end=None)
                if len(new_name) >= 0 and len(new_name) <= 999999999:
                    if cpm.set_player_name(rainbow_gradient_string(new_name)):
                        print(Colorate.Horizontal(Colors.rainbow, 'ประสบความสำเร็จ'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] คุณต้องการออกหรือไม่?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'ขอขอบคุณที่ใช้เครื่องมือของเรา โปรดเข้าร่วมช่องทางโทรเลขของเรา: @{__CHANNEL_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'ล้มเหลว.'))
                        print(Colorate.Horizontal(Colors.rainbow, 'โปรดลองอีกครั้ง'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'ล้มเหลว.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'กรุณาใช้ค่าที่ถูกต้อง'))
                    sleep(2)
                    continue
            elif service == 7: # Number Plates
                console.print("[%] มอบป้ายทะเบียนให้คุณ: ", end=None)
                if cpm.set_player_plates():
                    print(Colorate.Horizontal(Colors.rainbow, 'ประสบความสำเร็จ'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] คุณต้องการออกหรือไม่?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'ขอขอบคุณที่ใช้เครื่องมือของเรา โปรดเข้าร่วมช่องทางโทรเลขของเรา: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'ล้มเหลว.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'โปรดลองอีกครั้ง'))
                    sleep(2)
                    continue
            elif service == 8: # Account Delete
                print(Colorate.Horizontal(Colors.rainbow, '[!] หลังจากลบบัญชีของคุณแล้วจะไม่มีการย้อนกลับ !!.'))
                answ = Prompt.ask("[?] คุณต้องการลบบัญชีนี้หรือไม่!", choices=["y", "n"], default="n")
                if answ == "y":
                    cpm.delete()
                    print(Colorate.Horizontal(Colors.rainbow, 'ประสบความสำเร็จ'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    print(Colorate.Horizontal(Colors.rainbow, f'ขอขอบคุณที่ใช้เครื่องมือของเรา โปรดเข้าร่วมช่องทางโทรเลขของเรา: @{__CHANNEL_USERNAME__}.'))
                else: continue
            elif service == 9: # Account Register
                print(Colorate.Horizontal(Colors.rainbow, '[!] การลงทะเบียนบัญชีใหม่'))
                acc2_email = prompt_valid_value("[?] อีเมลบัญชี", "Email", password=False)
                acc2_password = prompt_valid_value("[?] รหัสผ่านบัญชี", "Password", password=False)
                console.print("[%] การสร้างบัญชีใหม่: ", end=None)
                status = cpm.register(acc2_email, acc2_password)
                if status == 0:
                    print(Colorate.Horizontal(Colors.rainbow, 'ประสบความสำเร็จ'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    print(Colorate.Horizontal(Colors.rainbow, f'ข้อมูล: เพื่อปรับแต่งบัญชีนี้ด้วย Cylo Plays'))
                    print(Colorate.Horizontal(Colors.rainbow, 'คุณลงชื่อเข้าใช้เกมมากที่สุดโดยใช้บัญชีนี้'))
                    sleep(2)
                    continue
                elif status == 105:
                    print(Colorate.Horizontal(Colors.rainbow, 'ล้มเหลว.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'อีเมลนี้มีอยู่แล้ว'))
                    sleep(2)
                    continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'ล้มเหลว.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'โปรดลองอีกครั้ง'))
                    sleep(2)
                    continue
            elif service == 10: # Delete Friends
                console.print("[%] กำลังลบเพื่อนของคุณ: ", end=None)
                if cpm.delete_player_friends():
                    print(Colorate.Horizontal(Colors.rainbow, 'ประสบความสำเร็จ'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] คุณต้องการออกหรือไม่?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'ขอขอบคุณที่ใช้เครื่องมือของเรา โปรดเข้าร่วมช่องทางโทรเลขของเรา: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'ล้มเหลว.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'โปรดลองอีกครั้ง'))
                    sleep(2)
                    continue
            elif service == 11: # Unlock All Paid Cars
                console.print("[!] หมายเหตุ: ฟังก์ชั่นนี้ใช้เวลาสักครู่จึงจะเสร็จสมบูรณ์ โปรดอย่ายกเลิก", end=None)
                console.print("[%] ปลดล็อครถยนต์ที่ต้องชำระเงินทั้งหมด: ", end=None)
                if cpm.unlock_paid_cars():
                    print(Colorate.Horizontal(Colors.rainbow, 'ประสบความสำเร็จ'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] คุณต้องการออกหรือไม่?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'ขอขอบคุณที่ใช้เครื่องมือของเรา โปรดเข้าร่วมช่องทางโทรเลขของเรา: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'ล้มเหลว.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'โปรดลองอีกครั้ง'))
                    sleep(2)
                    continue
            elif service == 12: # Unlock All Cars
                console.print("[%] ปลดล็อครถยนต์ทุกคัน: ", end=None)
                if cpm.unlock_all_cars():
                    print(Colorate.Horizontal(Colors.rainbow, 'ประสบความสำเร็จ'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] คุณต้องการออกหรือไม่?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'ขอขอบคุณที่ใช้เครื่องมือของเรา โปรดเข้าร่วมช่องทางโทรเลขของเรา: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'ล้มเหลว.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'โปรดลองอีกครั้ง'))
                    sleep(2)
                    continue
            elif service == 13: # Unlock All Cars Siren
                console.print("[%] ปลดล็อครถทุกคันไซเรน: ", end=None)
                if cpm.unlock_all_cars_siren():
                    print(Colorate.Horizontal(Colors.rainbow, 'ประสบความสำเร็จ'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] คุณต้องการออกหรือไม่?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'ขอขอบคุณที่ใช้เครื่องมือของเรา โปรดเข้าร่วมช่องทางโทรเลขของเรา: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'ล้มเหลว.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'โปรดลองอีกครั้ง'))
                    sleep(2)
                    continue
            elif service == 14: # Unlock w16 Engine
                console.print("[%] ปลดล็อคเครื่อง w16: ", end=None)
                if cpm.unlock_w16():
                    print(Colorate.Horizontal(Colors.rainbow, 'ประสบความสำเร็จ'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] คุณต้องการออกหรือไม่?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'ขอขอบคุณที่ใช้เครื่องมือของเรา โปรดเข้าร่วมช่องทางโทรเลขของเรา: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'ล้มเหลว.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'โปรดลองอีกครั้ง'))
                    sleep(2)
                    continue
            elif service == 15: # Unlock All Horns
                console.print("[%] ปลดล็อคแตรทั้งหมด: ", end=None)
                if cpm.unlock_horns():
                    print(Colorate.Horizontal(Colors.rainbow, 'ประสบความสำเร็จ'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] คุณต้องการออกหรือไม่?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'ขอขอบคุณที่ใช้เครื่องมือของเรา โปรดเข้าร่วมช่องทางโทรเลขของเรา: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'ล้มเหลว.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'โปรดลองอีกครั้ง'))
                    sleep(2)
                    continue
            elif service == 16: # Disable Engine Damage
                console.print("[%] การปลดล็อคปิดการใช้งานความเสียหาย: ", end=None)
                if cpm.disable_engine_damage():
                    print(Colorate.Horizontal(Colors.rainbow, 'ประสบความสำเร็จ'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] คุณต้องการออกหรือไม่?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'ขอขอบคุณที่ใช้เครื่องมือของเรา โปรดเข้าร่วมช่องทางโทรเลขของเรา: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'ล้มเหลว.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'โปรดลองอีกครั้ง'))
                    sleep(2)
                    continue
            elif service == 17: # Unlimited Fuel
                console.print("[%] ปลดล็อกเชื้อเพลิงไม่จำกัด: ", end=None)
                if cpm.unlimited_fuel():
                    print(Colorate.Horizontal(Colors.rainbow, 'ประสบความสำเร็จ'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] คุณต้องการออกหรือไม่?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'ขอขอบคุณที่ใช้เครื่องมือของเรา โปรดเข้าร่วมช่องทางโทรเลขของเรา: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'ล้มเหลว.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'โปรดลองอีกครั้ง'))
                    sleep(2)
                    continue
            elif service == 18: # Unlock House 3
                console.print("[%] ปลดล็อคบ้าน 3: ", end=None)
                if cpm.unlock_houses():
                    print(Colorate.Horizontal(Colors.rainbow, 'ประสบความสำเร็จ'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] คุณต้องการออกหรือไม่?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'ขอขอบคุณที่ใช้เครื่องมือของเรา โปรดเข้าร่วมช่องทางโทรเลขของเรา: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'ล้มเหลว.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'โปรดลองอีกครั้ง'))
                    sleep(2)
                    continue
            elif service == 19: # Unlock Smoke
                console.print("[%] ปลดล็อคควัน: ", end=None)
                if cpm.unlock_smoke():
                    print(Colorate.Horizontal(Colors.rainbow, 'ประสบความสำเร็จ'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] คุณต้องการออกหรือไม่?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'ขอขอบคุณที่ใช้เครื่องมือของเรา โปรดเข้าร่วมช่องทางโทรเลขของเรา: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'ล้มเหลว.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'โปรดลองอีกครั้ง'))
                    sleep(2)
                    continue
            elif service == 20: # Unlock Smoke
                console.print("[%] ปลดล็อคล้อ: ", end=None)
                if cpm.unlock_wheels():
                    print(Colorate.Horizontal(Colors.rainbow, 'ประสบความสำเร็จ'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] คุณต้องการออกหรือไม่?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'ขอขอบคุณที่ใช้เครื่องมือของเรา โปรดเข้าร่วมช่องทางโทรเลขของเรา: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'ล้มเหลว.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'โปรดลองอีกครั้ง'))
                    sleep(2)
                    continue
            elif service == 21: # Unlock Smoke
                console.print("[%] การปลดล็อกภาพเคลื่อนไหว: ", end=None)
                if cpm.unlock_animations():
                    print(Colorate.Horizontal(Colors.rainbow, 'ประสบความสำเร็จ'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] คุณต้องการออกหรือไม่?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'ขอขอบคุณที่ใช้เครื่องมือของเรา โปรดเข้าร่วมช่องทางโทรเลขของเรา: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'ล้มเหลว.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'โปรดลองอีกครั้ง'))
                    sleep(2)
                    continue
            elif service == 22: # Unlock Smoke
                console.print("[%] ปลดล็อคอุปกรณ์ชาย: ", end=None)
                if cpm.unlock_equipments_male():
                    print(Colorate.Horizontal(Colors.rainbow, 'ประสบความสำเร็จ'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] คุณต้องการออกหรือไม่?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'ขอขอบคุณที่ใช้เครื่องมือของเรา โปรดเข้าร่วมช่องทางโทรเลขของเรา: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'ล้มเหลว.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'โปรดลองอีกครั้ง'))
                    sleep(2)
                    continue
            elif service == 23: # Unlock Smoke
                console.print("[%] ปลดล็อคอุปกรณ์หญิง: ", end=None)
                if cpm.unlock_equipments_female():
                    print(Colorate.Horizontal(Colors.rainbow, 'ประสบความสำเร็จ'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] คุณต้องการออกหรือไม่?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'ขอขอบคุณที่ใช้เครื่องมือของเรา โปรดเข้าร่วมช่องทางโทรเลขของเรา: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'ล้มเหลว.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'โปรดลองอีกครั้ง'))
                    sleep(2)
                    continue
            elif service == 24: # Change Races Wins
                print(Colorate.Horizontal(Colors.rainbow, '[!] ใส่จำนวนการแข่งขันที่คุณชนะ'))
                amount = IntPrompt.ask("[?] จำนวน")
                console.print("[%] การเปลี่ยนแปลงข้อมูลของคุณ: ", end=None)
                if amount > 0 and amount <= 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999:
                    if cpm.set_player_wins(amount):
                        print(Colorate.Horizontal(Colors.rainbow, 'ประสบความสำเร็จ'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] คุณต้องการออกหรือไม่?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'ขอขอบคุณที่ใช้เครื่องมือของเรา โปรดเข้าร่วมช่องทางโทรเลขของเรา: @{__CHANNEL_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'ล้มเหลว.'))
                        print(Colorate.Horizontal(Colors.rainbow, 'โปรดลองอีกครั้ง'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'ล้มเหลว.'))
                    print(Colorate.Horizontal(Colors.rainbow, '[!] กรุณาใช้ค่าที่ถูกต้อง'))
                    sleep(2)
                    continue
            elif service == 25: # Change Races Loses
                print(Colorate.Horizontal(Colors.rainbow, '[!] ใส่จำนวนการแข่งขันที่คุณแพ้'))
                amount = IntPrompt.ask("[?] จำนวน")
                console.print("[%] การเปลี่ยนแปลงข้อมูลของคุณ: ", end=None)
                if amount > 0 and amount <= 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999:
                    if cpm.set_player_loses(amount):
                        print(Colorate.Horizontal(Colors.rainbow, 'ประสบความสำเร็จ'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] คุณต้องการออกหรือไม่?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'ขอขอบคุณที่ใช้เครื่องมือของเรา โปรดเข้าร่วมช่องทางโทรเลขของเรา: @{__CHANNEL_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'ล้มเหลว.'))
                        print(Colorate.Horizontal(Colors.rainbow, '[!] กรุณาใช้ค่าที่ถูกต้อง'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'ล้มเหลว.'))
                    print(Colorate.Horizontal(Colors.rainbow, '[!] กรุณาใช้ค่าที่ถูกต้อง'))
                    sleep(2)
                    continue
            elif service == 26: # Clone Account
                print(Colorate.Horizontal(Colors.rainbow, '[!] กรุณากรอกรายละเอียดบัญชี'))
                to_email = prompt_valid_value("[?] อีเมลบัญชี", "Email", password=False)
                to_password = prompt_valid_value("[?] รหัสผ่านบัญชี", "Password", password=False)
                console.print("[%] การโคลนบัญชีของคุณ: ", end=None)
                if cpm.account_clone(to_email, to_password):
                    print(Colorate.Horizontal(Colors.rainbow, 'ประสบความสำเร็จ'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] คุณต้องการออกหรือไม่?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'ขอขอบคุณที่ใช้เครื่องมือของเรา โปรดเข้าร่วมช่องทางโทรเลขของเรา: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                        
                    print(Colorate.Horizontal(Colors.rainbow, 'ล้มเหลว.'))
                    print(Colorate.Horizontal(Colors.rainbow, '[!] กรุณาใช้ค่าที่ถูกต้อง'))
                    sleep(2)
                    continue
            elif service == 27:
                console.print("[bold yellow][!] Note[/bold yellow]: ความเร็วเดิมไม่สามารถกู้คืนได้!.")
                console.print("[bold cyan][!] กรอกรายละเอียดรถ[/bold cyan]")
                car_id = IntPrompt.ask("[bold][?] รหัสรถ[/bold]")
                console.print("[bold cyan][%] แฮ็คความเร็วรถ[/bold cyan]:",end=None)
                if cpm.hack_car_speed(car_id):
                    console.print("[bold green]สำเร็จ (✔)[/bold green]")
                    console.print("================================")
                    answ = Prompt.ask("[?] คุณต้องการออกหรือไม่?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'ขอขอบคุณที่ใช้เครื่องมือของเรา โปรดเข้าร่วมช่องทางโทรเลขของเรา: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'ล้มเหลว.'))
                    print(Colorate.Horizontal(Colors.rainbow, '[!] กรุณาใช้ค่าที่ถูกต้อง'))
                    sleep(2)
                    continue
            elif service == 28: # ANGLE
                print(Colorate.Horizontal(Colors.rainbow, '[!] ป้อนรายละเอียดรถยนต์'))
                car_id = IntPrompt.ask("[red][?] รหัสประจำตัวรถ[/red]")
                print(Colorate.Horizontal(Colors.rainbow, '[!] เข้ามุมบังคับเลี้ยว'))
                custom = IntPrompt.ask("[red][?] กรอกจำนวนมุมที่คุณต้องการ[/red]")                
                console.print("[red][%] แฮ็กมุมรถ[/red]: ", end=None)
                if cpm.max_max1(car_id, custom):
                    print(Colorate.Horizontal(Colors.rainbow, 'ประสบความสำเร็จ'))
                    answ = Prompt.ask("[red][?] คุณต้องการที่จะออก[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print("ขอขอบคุณที่ใช้เครื่องมือของเรา")
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'ล้มเหลว'))
                    print(Colorate.Horizontal(Colors.rainbow, 'โปรดลองอีกครั้ง'))
                    sleep(2)
                    continue                                        
            else: continue
            break
        break
            
        
            
              
