```python
from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get the database URI from environment variables
database_uri = os.getenv('database_uri')

def generate_encryption_key():
    """
    This function generates a new encryption key.
    """
    key = Fernet.generate_key()
    return key

def encrypt_data(data, key):
    """
    This function encrypts the provided data using the provided key.
    """
    f = Fernet(key)
    encrypted_data = f.encrypt(data)
    return encrypted_data

def decrypt_data(encrypted_data, key):
    """
    This function decrypts the provided data using the provided key.
    """
    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data)
    return decrypted_data

def secure_database_connection():
    """
    This function secures the database connection using encryption.
    """
    # Generate a new encryption key
    key = generate_encryption_key()

    # Encrypt the database URI
    encrypted_database_uri = encrypt_data(database_uri, key)

    # Decrypt the database URI (for use in connecting to the database)
    decrypted_database_uri = decrypt_data(encrypted_database_uri, key)

    return decrypted_database_uri
```