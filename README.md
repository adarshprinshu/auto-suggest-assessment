The auto_suggest function takes two arguments: words (a list of words) and prefix (the prefix to search for).
Inside the function, we create a regular expression pattern pattern using the fr"^{prefix}" syntax. The ^ symbol matches the start of the string, and the r prefix denotes a raw string literal, which is useful for handling backslashes in regular expressions. The f prefix is for formatted string literals, allowing us to insert the prefix variable directly into the pattern string.
We then use a list comprehension to filter the words list, keeping only those words that match the pattern regex. The re.search function searches for the pattern in each word, and the re.IGNORECASE flag makes the search case- insensitive.
The filtered list of suggestions is returned by the function.
In the example usage, we define the input lists input1 and input2, and call the auto_suggest function with different prefixes ("ke" and "*k").
The suggestions are printed for each input.
