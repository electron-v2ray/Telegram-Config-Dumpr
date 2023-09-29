import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

webpage_addresses = [


    "https://web.telegram.org/k/#?tgaddr=tg%3A%2F%2Fresolve%3Fdomain%3Dinternet_groups",
    "https://t.me/s/vpn_xw",
    "https://t.me/s/CloudCityy",
    "https://t.me/s/azadi_az_inja_migzare",
    "https://t.me/s/reality_daily",
    "https://t.me/s/zen_cloud",
    "https://t.me/s/DigiV2ray",
    "https://t.me/s/prrofile_purple",
    "https://t.me/s/V2rayCollectorDonate",
    "https://t.me/s/iP_CF",
    "https://t.me/s/TLS_v2ray",
    "https://t.me/s/v2raycollector",
    "https://t.me/s/Cov2ray",
    "https://t.me/s/v2ray_cartel",
    "https://t.me/s/speedconfig00",
    "https://t.me/s/FOXNT",
    "https://t.me/s/EspinasVPN",
    "https://t.me/s/frev2ray",
    "https://t.me/s/vpnsshocean",
    "https://t.me/s/forwardv2ray",
    "https://t.me/s/filterkoshi",
    "https://t.me/s/MsV2ray",
    "https://t.me/s/Outline_Vpn",
    "https://t.me/s/ARv2ray",
    "https://t.me/s/Eleven_vpn",
    "https://t.me/s/v2rayng_org",
    "https://t.me/s/freeownvpn",
    "https://t.me/s/msv2raynp",
    "https://t.me/s/v2rayngvpn",
    "https://t.me/s/v2ray_outlineir",
    "https://t.me/s/PrivateVPNs",
    "https://t.me/s/v2_vmess",
    "https://t.me/s/V2RAY_VMESS_free",
    "https://t.me/s/VmessProtocol",
    "https://t.me/s/FOX_VPN66",
    "https://t.me/s/Network_442",
    "https://t.me/s/Awlix_ir",
    "https://t.me/s/God_CONFIG",
    "https://t.me/s/Configforvpn01",
    "https://t.me/s/vpn_ocean",
]


def remove_duplicates(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


html_pages = []

for url in webpage_addresses:
    response = requests.get(url)
    html_pages.append(response.text)

codes = []

for page in html_pages:
    soup = BeautifulSoup(page, 'html.parser')
    code_tags = soup.find_all('code')

    for code_tag in code_tags:
        code_content = code_tag.text.strip()
        if "vless://" in code_content or "ss://" in code_content or "vmess://" in code_content or "trojan://" in code_content:
            codes.append(code_content)

codes = list(set(codes))  # Remove duplicates

processed_codes = []

# Get the current date and time
current_date_time = datetime.now()

# Print the current month in letters
current_month = current_date_time.strftime("%b")

# Get the current day as a string
current_day = current_date_time.strftime("%d")

# Increase the current hour by 4 hours
new_date_time = current_date_time + timedelta(hours=4)

# Get the updated hour as a string
updated_hour = new_date_time.strftime("%H")

# Combine the strings to form the final result
final_string = f"{current_month}-{current_day}-{updated_hour}"
config_string = "#✅ " + str(final_string) + ":00-"

for code in codes:
    vmess_parts = code.split("vmess://")
    vless_parts = code.split("vless://")

    for part in vmess_parts + vless_parts:
        if "ss://" in part or "vmess://" in part or "vless://" in part or "trojan://" in part:
            service_name = part.split("serviceName=")[-1].split("&")[0]
            processed_part = part.split("#")[0]
            processed_codes.append(processed_part)

processed_codes = remove_duplicates(processed_codes)

i = 0
with open("config.txt", "w", encoding="utf-8") as file:
    for code in processed_codes:
        if i == 0:
            config_string = "#🌐 Updated on " + final_string + ":00 | update every 12 hours"
        else:
            config_string = "#🌐electron-v2ray " + str(final_string) + ":00-" + str(i)
        config_final = code + config_string
        file.write(config_final + "\n")
        i += 1
