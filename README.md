import re

def auto_suggest(words, prefix):
    pattern = fr"^{prefix}"  # regex pattern for prefix matching
    suggestions = [word for word in words if re.search(pattern, word, re.IGNORECASE)]
    return suggestions
