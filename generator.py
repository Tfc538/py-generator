import random

Numbers = [0,1,2,3,4,5,6,7,8,9]

Letters = [
            "q","w","e","r","t","z","u","i",
            "o","p","ü","a","s","d","f","g",
            "h","j","k","l","ö","ä","y","x",
            "c","v","b","n","m",
            "Q","W","E","R","T","Z","U","I",
            "O","P","Ü","A","S","D","F","G",
            "H","J","K","L","Ö","Ä","Y","X",
            "C","V","B","N","M","0","1","2",
            "3","4","5","6","7","#","#","#",
            "#","#","#","#","#","#","#","#",
            "#","#","#","#","#","#","#","#",
            "#","#","#","#","#","#","#","#"
]

random.shuffle(Letters)
random.shuffle(Numbers)

print(''.join(Letters))
