import os
import secrets
import time

def generate_random_string(length):
    return secrets.token_hex(length).upper()

def generate_formatted_key():
    parts = [generate_random_string(4) for _ in range(4)]
    return '-'.join(parts)

def generate_and_save_keys(number_of_keys, log_file_path, output_file_path):
    existing_keys = []
    try:
        with open('keys.txt', 'r') as f:
            existing_keys = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        pass

    keys = []
    while len(keys) < number_of_keys:
        new_key = generate_formatted_key()
        if new_key not in existing_keys and new_key not in keys:
            keys.append(new_key)

    with open(log_file_path, 'a') as f:
        f.write('\n'.join(keys) + '\n')
    with open(output_file_path, 'w') as f:
        f.write('\n'.join(keys))

    print(f"Generated and saved {len(keys)} unique keys to {output_file_path}")

current_time = time.strftime('%d-%m-%Y_%H%M%S')
current_directory = os.getcwd()
log_file_name = 'keys.txt'
output_file_name = f'keys_{current_time}.txt'
log_file_path = os.path.join(current_directory, log_file_name)
output_file_path = os.path.join(current_directory, output_file_name)

generate_and_save_keys(1000, log_file_path, output_file_path)