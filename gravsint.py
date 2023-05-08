import hashlib
import json
import subprocess

print('''
 ██████  ██████   █████  ██    ██ ███████ ██ ███    ██ ████████
██       ██   ██ ██   ██ ██    ██ ██      ██ ████   ██    ██
██   ███ ██████  ███████ ██    ██ ███████ ██ ██ ██  ██    ██
██    ██ ██   ██ ██   ██  ██  ██       ██ ██ ██  ██ ██    ██
 ██████  ██   ██ ██   ██   ████   ███████ ██ ██   ████    ██

                    created by Akinari
''')

def search_gravatar_by_email():
    email = input("Masukkan email : ")
    md5 = hashlib.md5(email.encode('utf-8')).hexdigest()
    url = f"https://en.gravatar.com/{md5}.json"
    return url

def search_gravatar_by_username():
    username = input("Masukkan username : ")
    url = f"https://en.gravatar.com/{username}.json"
    return url

print("Pilih cara pencarian Gravatar :")
print("1. Email")
print("2. Username")

choice = input("Pilihan (1/2): ")
if choice == "1":
    url = search_gravatar_by_email()
elif choice == "2":
    url = search_gravatar_by_username()
else:
    print("Pilihan tidak valid.")
    exit()

# Jalankan curl untuk mendapatkan hasil JSON
try:
    output = subprocess.check_output(["curl", "-s", url])

    # Parse JSON ke dalam objek Python
    result = json.loads(output)
except:
    print("Nothing!")
    exit()

print("\nHasil Pencarian : ")
if 'entry' in result and len(result['entry']) > 0:
    print(f"Id           : {result.get('entry', [{}])[0].get('id', '')}")
    print(f"Profile      : {result.get('entry', [{}])[0].get('profileUrl', '')}")
    print(f"Username     : {result.get('entry', [{}])[0].get('preferredUsername', '')}")
    print(f"Photo        : {result.get('entry', [{}])[0].get('thumbnailUrl', '')}")
    print(f"Hash         : {result.get('entry', [{}])[0].get('hash', '')}")
    print(f"First Name   : {result.get('entry', [{}])[0].get('name', {}).get('givenName', '')}")
    print(f"Second Name  : {result.get('entry', [{}])[0].get('name', {}).get('familyName', '')}")
    print(f"Fullname     : {result.get('entry', [{}])[0].get('name', {}).get('formatted', '')}")
    print(f"Display Name : {result.get('entry', [{}])[0].get('displayName', '')}")
    print(f"About        : {result.get('entry', [{}])[0].get('aboutMe', '')}")
else:
    print("Nothing!")