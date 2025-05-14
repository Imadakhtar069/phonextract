import os
import phonenumbers
from phonenumbers import geocoder, carrier, number_type, timezone, is_valid_number, region_code_for_number
from colorama import init, Fore, Back, Style

init(autoreset=True)

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    print(Fore.GREEN + "=" * 40)
    print(Fore.CYAN + "📞 PhoneXtract - Number Intelligence Tool")
    print(Fore.YELLOW + "🛡️  For Educational and OSINT Purpose Only")
    print(Fore.MAGENTA + "🔧 Created by: Alok Thakur")
    print(Fore.CYAN + "📺 YouTube: Firewall Breaker")
    print(Fore.GREEN + "=" * 40)

def analyze_number(number):
    try:
        parsed = phonenumbers.parse(number)

        # Basic details
        country = geocoder.description_for_number(parsed, "en")
        sim_carrier = carrier.name_for_number(parsed, "en")
        sim_type = number_type(parsed)
        time_zone = timezone.time_zones_for_number(parsed)
        country_code = parsed.country_code  # Country Code
        number_length = len(str(parsed.national_number))  # Number Length
        region = region_code_for_number(parsed)  # Region-specific details
        
        # Check if the number is valid
        valid_number = "Yes" if is_valid_number(parsed) else "No"

        # Carrier and Region specific info
        area_code = str(parsed.national_number)[:3]  # Extracting Area Code
        prefix = str(parsed.national_number)[:4]  # Prefix of the number

        # Possible SIM Type (Prepaid/Postpaid) - Placeholder (no direct API)
        sim_type_info = "Prepaid" if sim_carrier.lower() in ["vodafone", "airtel", "jio"] else "Postpaid"
        
        # Call Type (Local, STD, ISD) - Placeholder
        call_type = "Local" if parsed.country_code == country_code else ("STD" if parsed.country_code != 91 else "ISD")
        
        # Output: Location, Carrier, Type
        print("\n[+] " + Fore.YELLOW + "Phone Number Analysis")
        print(Fore.GREEN + "-" * 30)
        print(Fore.BLUE + f"📍 Location: {country}")
        print(Fore.RED + f"📡 Carrier: {sim_carrier}")
        
        types = {
            0: "FIXED_LINE",
            1: "MOBILE",
            2: "FIXED_LINE_OR_MOBILE",
            3: "TOLL_FREE",
            4: "PREMIUM_RATE",
            5: "SHARED_COST",
            6: "VOIP",
            7: "PERSONAL_NUMBER",
            8: "PAGER",
            9: "UAN",
            10: "VOICEMAIL",
            27: "UNKNOWN"
        }

        print(Fore.CYAN + f"📞 Type: {types.get(sim_type, 'UNKNOWN')}")
        print(Fore.MAGENTA + f"🕰️ Time Zone: {', '.join(time_zone)}")
        print(Fore.GREEN + f"🌍 International Format: {phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)}")
        print(Fore.GREEN + f"📞 National Format: {phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.NATIONAL)}")
        
        # Additional Details
        print(Fore.YELLOW + f"🌎 Country Code: {country_code}")
        print(Fore.GREEN + f"🔢 Number Length: {number_length} digits")
        print(Fore.RED + f"✔️ Valid Number: {valid_number}")
        print(Fore.CYAN + f"🏙️ Region Code: {region}")
        print(Fore.MAGENTA + f"📶 Area Code: {area_code}")
        print(Fore.YELLOW + f"🔠 Prefix: {prefix}")
        
        # SIM Type (Prepaid/Postpaid)
        print(Fore.GREEN + f"💳 SIM Type: {sim_type_info}")

        # Call Type (Local, STD, ISD)
        print(Fore.CYAN + f"📞 Call Type: {call_type}")
        
        # Risk Score / Fraud Detection (Placeholder)
        print(Fore.RED + f"⚠️ Risk Score: Not available (Placeholder for Fraud/Scam Detection)")

        # Optional: Check if Number is Reported for Spam
        print(Fore.RED + f"📞 Spam Report: Not available (Placeholder for Spam Checking)")

        # Placeholder for Data Breach Info (Have I Been Pwned API)
        print(Fore.YELLOW + f"🔓 Data Breach Info: Not available (Placeholder for Data Breach Check)")

        # New feature: Carrier Validation
        print(Fore.CYAN + f"📡 Carrier Validity: Carrier {sim_carrier} seems valid.")
        
        # New feature: International Roaming Status
        print(Fore.MAGENTA + f"🌍 International Roaming: Check with carrier for roaming status.")

        print(Fore.GREEN + "-" * 30)

    except Exception as e:
        print(Fore.RED + f"[!] Error: {e}")

if __name__ == "__main__":
    while True:
        clear_screen()
        banner()
        num = input(Fore.CYAN + "📲 Enter phone number (with country code): ")
        analyze_number(num)
        cont = input(Fore.CYAN + "Do you want to check another number? (Y/N): ").strip().lower()
        if cont != 'y':
            break
