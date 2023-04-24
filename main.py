import argparse

from symmetric_encryption import generate_symmetric_key, symmetric_decrypt, symmetric_encrypt
from functions import read_bytes_sequence, save_bytes_sequence
from asymmecric_encryption import generate_pair_of_keys, asymmetric_decrypt, asymmetric_encrypt, \
    serialize_asymmetric_keys, deserialize_private_key, deserialize_public_key
from settings import read_settings

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-cus', '--custom', type=str,
                        help='Использует пользовательский файл с настройками, необходимо указать путь к файлу')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-gen', '--generation', help='Запускает режим генерации ключей')
    group.add_argument('-enc', '--encryption', help='Запускает режим шифрования')
    group.add_argument('-dec', '--decryption', help='Запускает режим дешифрования')
    args = parser.parse_args()
    settings = read_settings()
    if settings:
        if args.generation:
            symmetric_key = generate_symmetric_key(settings['key_length'])
            private_key, public_key = generate_pair_of_keys()
            serialize_asymmetric_keys(public_key, private_key, settings['public_key'], settings['private_key'])
            save_bytes_sequence(asymmetric_encrypt(public_key, symmetric_key), settings['symmetric_key'])
        elif args.encryption:
            private_key = deserialize_private_key(settings['private_key'])
            c_key = read_bytes_sequence(settings['symmetric_key'])
            symmetric_key = asymmetric_decrypt(private_key, c_key)
            text = read_bytes_sequence(settings['initial_file'])
            c_text = symmetric_encrypt(symmetric_key, text)
            save_bytes_sequence(c_text, settings['encrypted_text'])
        else:
            private_key = deserialize_private_key(settings['private_key'])
            c_key = read_bytes_sequence(settings['symmetric_key'])
            symmetric_key = asymmetric_decrypt(private_key, c_key)
            c_text = read_bytes_sequence(settings['encrypted_text'])
            text = symmetric_decrypt(symmetric_key, c_text)
            save_bytes_sequence(text, settings['decrypted_text'])
