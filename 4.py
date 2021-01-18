from googletrans import Translator
translator = Translator()

ru = ["Один", "Два", "Три", "Четыре", "Пять", "Шесть", "Семь"]
en = ["One", "Two", "Three", "Four", "Five", "Six", "Seven"]

def trans(word):
    return ru[en.index(word)] if word in en else ''

f1 = open("4.txt", 'r')
f2 = open("A.txt", 'w')

for line in f1:
#    f2.write(translator.translate(line, dest='ru').text)
     pars = line.split('-')
     f2.write(trans(pars[0])+'-'+pars[1])

f2.close()
f1.close()
