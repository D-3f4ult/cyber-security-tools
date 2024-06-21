import hashlib
import logging

def hash_file(file_path, hash_type="sha256"):
    hash_func = getattr(hashlib, hash_type)()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_func.update(chunk)
        return hash_func.hexdigest()
    except Exception as e:
        logging.error(f"Error hashing file {file_path}: {e}")
        return None

def compare_hash(file_path, expected_hash, hash_type="sha256"):
    file_hash = hash_file(file_path, hash_type)
    if file_hash:
        return file_hash == expected_hash
    return False
