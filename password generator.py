import os
from datetime import datetime

PASSWORD_FILE = "passwords.txt"

# Evaluate password strength
def check_strength(password):
    length = len(password) >= 8
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()-_=+[{]};:<>|./?" for c in password)
    
    strength = sum([length, has_upper, has_lower, has_digit, has_special])
    
    if strength == 5:
        return "Very Strong"
    elif strength == 4:
        return "Strong"
    elif strength == 3:
        return "Medium"
    else:
        return "Weak"

# Load existing passwords
def load_passwords():
    passwords = {}
    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, 'r') as f:
            for line in f:
                parts = line.strip().split('|')
                if len(parts) == 3:
                    service, masked_pw, timestamp = parts
                    if service not in passwords:
                        passwords[service] = []
                    passwords[service].append((masked_pw, timestamp))
    return passwords

# Save a new password
def save_password(service, password):
    masked_pw = '*' * len(password)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(PASSWORD_FILE, 'a') as f:
        f.write(f"{service}|{masked_pw}|{timestamp}\n")

# Check if password was reused
def is_reused(service, password, passwords):
    masked_pw = '*' * len(password)
    if service in passwords:
        return any(pw == masked_pw for pw, _ in passwords[service])
    return False

# View password history
def view_history(passwords):
    for service, entries in passwords.items():
        print(f"\nService: {service}")
        for pw, time in entries:
            print(f"  {pw} (added on {time})")

# Main program
def main():
    passwords = load_passwords()

    while True:
        print("\nPassword Manager")
        print("1. Add Password")
        print("2. View Password History")
        print("3. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            service = input("Enter service name (e.g., Gmail): ").strip().lower()
            password = input("Enter new password: ").strip()
            
            strength = check_strength(password)
            print(f"Password Strength: {strength}")
            
            if is_reused(service, password, passwords):
                print("⚠️ Warning: This password was used before for this service!")
            else:
                save_password(service, password)
                print("✅ Password saved.")
                if service not in passwords:
                    passwords[service] = []
                passwords[service].append(('*' * len(password), datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        
        elif choice == '2':
            view_history(passwords)
        
        elif choice == '3':
            print("Exiting Password Manager...")
            break
        
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

