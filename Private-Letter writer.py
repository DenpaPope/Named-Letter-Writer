print('hello this is the private letter writer, please follow the instructions')

names = []
occupations = []
counter = 0
more = ''

letter_text = input('please write the text of the letter, while labeling the name of the worker as name and job occupation as occupation - ')

while more != 'n':
    name = input('please input the names of the officials that need to recieve the personal letter. Name "," and position: ')
    info = list(name.split(','))
    names.append(info[0])
    occupations.append(info[1])
    more = input('do you want to add another one? Y or N - ')
    if more == 'n':
        break
    if more != 'n' or more != 'y':
        print('please provide correct input')


while True:
    words = letter_text.split(' ')
    for i, n in enumerate(words):
        if n == 'name' or n == 'name,' or n == ',name':
            words[i] = names[counter]
    for g, k in enumerate(words):
        if k == 'occupation' or k == 'occupation,' or k == ',occupation':
            words[g] = occupations[counter]
    final_text = ' '.join(words)
    print(final_text)
    counter += 1


