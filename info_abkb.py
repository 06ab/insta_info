import requests
import json
import random
from cfonts import render, say
k = render('{info_insta}', colors=['red', 'blue'], align='center')
print(f'''\n
  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
     
                      {k}
    ~ devlomper : @06ab| tele: @abkb6~
 
   ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛    
''')                
def date(hy):
    try:
        ranges = [
            (1279000, 2010),
            (17750000, 2011),
            (279760000, 2012),
            (900990000, 2013),
            (1629010000, 2014),
            (2500000000, 2015),
            (3713668786, 2016),
            (5699785217, 2017),
            (8597939245, 2018),
            (21254029834, 2019)
        ]

        for upper, year in ranges:
            if hy <= upper:
                return year
        return 2023

    except Exception:
        pass

def InfoAcc(username, gg):
    global total, ID

    rr = infoinsta.get(username,{})

    Id = rr.get('pk',)
    full_name = rr.get('full_name', )
    fows = rr.get('follower_count', )
    fowg = rr.get('following_count', )
    pp = rr.get('media_count', )
    isPraise = rr.get('is_private', )
    bio = rr.get('biography', )
    is_verified = rr.get('is_verified', )
    headers = {
    'X-Pigeon-Session-Id': '50cc6861-7036-43b4-802e-fb4282799c60',
    'X-Pigeon-Rawclienttime': '1700251574.982',
    'X-IG-Connection-Speed': '-1kbps',
    'X-IG-Bandwidth-Speed-KBPS': '-1.000',
    'X-IG-Bandwidth-TotalBytes-B': '0',
    'X-IG-Bandwidth-TotalTime-MS': '0',
    'X-Bloks-Version-Id': 'c80c5fb30dfae9e273e4009f03b18280bb343b0862d663f31a3c63f13a9f31c0',
    'X-IG-Connection-Type': 'WIFI',
    'X-IG-Capabilities': '3brTvw==',
    'X-IG-App-ID': '567067343352427',
    'User-Agent': 'Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)',
    'Accept-Language': 'en-GB, en-US',
     'Cookie': 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept-Encoding': 'gzip, deflate',
    'Host': 'i.instagram.com',
    'X-FB-HTTP-Engine': 'Liger',
    'Connection': 'keep-alive',
    'Content-Length': '356',
}
    data = {
    'signed_body': '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj","adid":"0dfaf820-2748-4634-9365-c3d8c8011256","guid":"1f784431-2663-4db9-b624-86bd9ce1d084","device_id":"android-b93ddb37e983481c","query":"'+username+'"}',
    'ig_sig_key_version': '4',
  }
    response = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/',headers=headers,data=data,).json()
    r=response['email']
    try:
        hy = int(Id) if Id != 'none' else None
        datte = date(hy) if hy else 'none'
    except:
        datte = 'none'
    total += 1
    urlk = "https://i.instagram.com/api/v1/users/lookup/"

    payloadk = {
  "q":username,
  }
    headersk = {
    'User-Agent': f"Instagram {random.randint(100,999)}.0.0.{random.randint(10,99)}.{random.randint(100,999)} Android (20/12; 320dpi; 720x1456; mt6765; ar_IQ; {random.randint(100000,999999)})",
  }
    responsek = requests.post(urlk, data=payloadk, headers=headersk).json()
    try:
        can_email_reset=responsek['can_email_reset']
    except:
        can_email_reset=False
    try:
        obfuscated_phone=responsek['obfuscated_phone']
    except:
        obfuscated_phone=False
    try:
        pk_id=responsek['user']['fbid_v2']
    except:
        pk_id=None
    try:
        profile_pic_url=responsek['user']['profile_pic_url']
    except:
        profile_pic_url= False

    ss = f"""
          𓊆 INSTAGRAM info  𓊇
╭───────────────────────╮
│ 🌟 nav     : {username}
│ 👥 yars      : {fows}
│ 👣 yaryen          : {fowg}
│ 📝 chehrag post       : {pp}
│ 💬 byane    : {bio}
│ 📅 tarekh jortehn     : {datte}
╰───────────────────────╯
╭───────────────────────╮
│ 📧 email      : {username}@{gg}
│ 🔒 numbar     : {obfuscated_phone}
│ 🔄 h         : {r}
╰───────────────────────╯
╭───────────────────────╮
│ 🔗 <a href="https://www.facebook.com/{pk_id}">Facebook Link</a>
│ 📸 <a href="https://www.instagram.com/{username}/">Insta Link</a>
╰───────────────────────╯
╭                        ──                                      ╮
  💌 TELEGRAM : @abkb6 github @06ab
╰                        ──                                      ╯
"""
    return ss


def main():
    global total, ID, infoinsta
    
    
    username = input("Instagram user: ").strip()
    
  
    email_domain = input("emails types ?!(for example: gmail.com, hotmail.com): ").strip()
    
    
    total = 0
    ID = None
    infoinsta = {}
    
    
    result = InfoAcc(username, email_domain)
    
    
    print(result)


if __name__ == "__main__":
    main()
