def edit_distance(s,t):
    dist = 0
    a = list(s)
    b = list(t)
    while len(a) != len(b):
        if len(a) > len(b):
            if a[0] == b[0]:
                del a[-1]
                dist += 1
            else:
                del a[0]
                dist += 1
        elif a[0] == b[0]:
            del b[-1]
            
            dist += 1
        else:
            del b[0]
            dist += 1
    for i in range(len(a)):
        if a[i] != b[i]:
            a[i] = b[i]
            dist += 1
    return dist





def spell_check():
    x=raw_input("Enter the wrong apelling: ")
    file_words = open("words.txt", 'r')
    dictionary = (file_words.read()).split()
    count=min(edit_distance(x,dictionary[i]) for i in range(len(dictionary)))
    for i in range(len(dictionary)):
        if(edit_distance(x,dictionary[i])==count):
           print dictionary[i]
           break
    file_words.close()

def add_word():
    add = raw_input("Enter the word you want to add : ")
    file_words = open("words.txt", 'a')
    file_words.write("\n"+add)
    print "The word is added!"
    file_words.close()
    return

while True:
    inp = input("Press 1 to check the spelling \nPress 2 to add a new word and \nPress 3 to exit:")
    if inp == 1:
        spell_check()
    elif inp == 2:
        add_word()
    elif inp == 3:
        break
    else:
        print "Wrong Choice!!!"

    




 
