#take tw0 words and compare them witout cae sensivitytivity
def compareWords(word1, word2):
    if word1.lower() == word2.lower():
        return True
    else:
        return False
    
word1 = input("1.Kelimeyi giriniz:")
word2 = input("2.Kelimeyi giriniz:")
if compareWords(word1,word2):
    print("Kelimeler aynıdır.") 
else:
    print("Kelimeler farklıdır.")
