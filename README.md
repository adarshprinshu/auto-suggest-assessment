import re

def auto_suggest(words, prefix):
    pattern = fr"^{prefix}"  # regex pattern for prefix matching
    suggestions = [word for word in words if re.search(pattern, word, re.IGNORECASE)]
    return suggestions

# Example usage
input1 = ["take", "make", "check", "ack", "rake"]
input2 = "ke"
suggestions = auto_suggest(input1, input2)
print(f"Input1: {', '.join(input1)}")
print(f"Input2: {input2}")
print(f"Suggestions: {', '.join(suggestions)}")

input2 = "*k"
suggestions = auto_suggest(input1, input2)
print(f"Input1: {', '.join(input1)}")
print(f"Input2: {input2}")
print(f"Suggestions: {', '.join(suggestions)}")
