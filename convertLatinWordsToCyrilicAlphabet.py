global badLetters
global latinToCyrilic


def latin_to_cyrilic(word, skip_warning = False):
  if not skip_warning:
    if any([(letter in word) for letter in badLetters]):
      raise Exception(f"{word} cannot be written in the cyrilic alphabet")

  for translation in latinToCyrilic:
    word = word.replace(translation[0],translation[1])
  return word

# Initializing variables

allWordsInRussian = [] # This will store all the writable words

listOfWordsFilePath = "/words.txt" # "/content/gdrive/MyDrive/MISCS/miscTXTs/words.txt"
outputFilePath = "/wordsInCyrilic.txt" # '/content/allWordsThatYouCanWriteWithCyrilicAlphabet.txt'

badLetters = ['d','f','g','i','j','q','s','v','z'] # These are all of the letters that cannot be written using the cyrilic alphabet
latinToCyrilic = [['y','у'],["k","к"],['e','е'],['r','г'],['x','х'],["p","р"],['o','o'],['t','т'],["b","в"],['h','н'],['n','п'],['w','ш'],['u', "ц"]] # Convert the latin characters to their cyrilic counterparts

if __name__ == "main":
  # Getting the data and then making it all lowercase (so that we don't have to check for the upper AND lower case version of each letter) 
  words = open(listOfWordsFilePath, "r").read()
  words = [z.lower() for z in words.split('\n')]

  # Getting rid of anything that has numbers, as well as any word that contains any of the forbidden letters
  for i in range(len(words)):
    if not any([z in words[i] for z in badLetters]) and words[i].isalpha():
      allWordsInRussian.append(words[i])

  # Loops through the array and then converts the latin characters to cyrilic ones
  allWordsInRussian = [latin_to_cyrilic(word) for word in allWordsInRussian]
  with open(outputFilePath,'w') as f:
    f.write("\n".join(allWordsInRussian))
