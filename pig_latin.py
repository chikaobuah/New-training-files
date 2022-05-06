def pig_latin(text):
  say = ""
  # Separate the text into words
  
  words = text.split()
  for index, word in enumerate(words):
    # Create the pig latin word and add it to the list
    l = len(word)
    word = word[1:l] + word[0] + 'ay'
    words[index] = word
    
    # Turn the list back into a phrase
  return " ".join(words)
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"
