from hashing_tool import compare_hash

file_path = "example.txt"
expected_hash = "expectedhashvalue"
print(f"File hash matches: {compare_hash(file_path, expected_hash)}")
