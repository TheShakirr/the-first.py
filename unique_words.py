words = ["python", "javascript", "python", "c#", "javascript", "go"]
unique_words = set (words)

print("unique_words:", unique_words)

if "python" in unique_words:
    print("python is in the set")
else:
    print("python is NOT in the set")