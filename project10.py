Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def censor(word):
    for i in range(len(word)):
        if word[i].isalpha():
            word=word[:i] + '*' + word [i+1:]
    return word

def main():
    f= input ("Enter the file to censor: ")
    tex= open(f, 'r')
    word.f= input ("Enter the file containing the words: ")
    cen= open(word.f, 'r')
    cen.word= cen.read().split()

    cen.t= ""
    for line in text:
        words = line.split()
        for i in range(len(words)):
            word= ""
            for letter in words [i]:
                if letter.isalpha():
                    word+= letter
            if word in cen.word:
                words[i]= cen(words[i])
        cen.t += " ".join(words) + '\n'

        tex.close()
        cen.close()

        newfile = open("censored:" + f, 'w')
        newfile.write(censored_text)
        newfile.close()
main() 
