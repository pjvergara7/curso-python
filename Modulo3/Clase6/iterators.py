words = "Esto es una cadena de texto"

word = ''
for letter in words:
    if letter!= ' ':
        word += letter
    else:
        print(word)
        word = ''

print("\n --------------------------- \n")
for letter in words:
    if letter != ' ':
        print(letter)
    else:
        break

print("\n --------------------------- \n")
animals_list = ['Gato', 'Doggo', 'Pájaro', 'Ardilla']
for animal in animals_list:
    print(animal)

print("\n --------------------------- \n")

list1 = range(2,3)
print(list1)
for number_in in range(1,10,2):
    print(number_in)


