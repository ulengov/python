def func(*args, name, faml, year, toun, emal, phon):
    print(name+' '+faml+' '+year+' '+toun+' '+emal+' '+phon)

name = input("Имя: ")
faml = input("Фамилия: ")
year = input("Год рождения: ")
toun = input("Город: ")
emal = input("E-mail: ")
phon = input("Телефон: ")

func(name=name, faml=faml, year=year, toun=toun, emal=emal, phon=phon)



