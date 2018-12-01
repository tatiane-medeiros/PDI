dic = {'A': '.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.','G':'--.','H':'....',
       'I':'..','J':'.---','K':'-.-','L':'.-..','M':'--	','N':'-.','O':'---',
        'P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-','U':'..-',
        'V':'...-','W':'.--', 'X':'-..-','Y':'-.--','Z':'--..',
       '0':'-----', '1':'.----','2':'..---','3':'...--','4':'....-','5':'.....',
       '6':'-....','7':'--...','8':'---..','9':'----.', ' ': '/'}

print(" 1- texto p/ morse\n 2- morse p/ texto\nDigite a opção:")
op = input()

if op == '1':    
    sentence = input().upper()
    print(sentence)
    tr = ""
    for i in sentence:
        #print(dic[i])
        tr+= dic[i] + ' '
    print(tr)
    
elif op == '2':
    cod = input().split()
    s = ""
    for i in cod:
        s += list(dic.keys())[list(dic.values()).index(i)]
    print(s)

else:
    print("opção invalida!")
