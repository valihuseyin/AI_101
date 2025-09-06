#tr in a text
def is_text_contains_word(text,word):
    if word in text:
        return True
    return False

text =input("Bir ifade giriniz:")
if is_text_contains_word(text,"tr"):
    print("Kelime \"tr\" ifadesi içermektedir.")
else:
    print("Kelime \"tr\" ifadesi içermemektedir.")

