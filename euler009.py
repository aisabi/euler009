dico = {}   

for a in range(1,100):
    # argument = 99
    # recherch = argument
    target = 120
    # print('recherche',recherche)
    a > 0
    for b in range(1,100):
        b >0
        c =  a **2 + b **2
        cRacine = c ** 0.5
        
        if (cRacine.is_integer()) == True:
            cRacine = int(cRacine)
            # print('Solution : ',a**2,'+',b**2,'=',cRacine**2)
            argument = a + b + cRacine
            # print('Finale Multiplication: ',a,'x',b,'x',cRacine,'=', a * b * cRacine)
            retour = a * b * cRacine
                
            dico.setdefault(argument, []).append(retour)
            # dico.update({argument:retour}) # can append but only one key so use of setdefault method
            print(dico)

            # print('KEY',cle)
            for cle in dico.keys(): 
                if cle == target:
                    print("\nThe value for argument ",target, " is ",set(dico[cle]))
                