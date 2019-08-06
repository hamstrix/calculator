#importarea meniul necesar operatiilor matematice
import math
#Bucla while pentru exevutarea programului fara intrerupere si a permite utilizatorului sa se intoarca la
#meniu si sa aleaga altaoptiune
while True:
#utilizatorul alegeoperatia matematica pe care o odreste din meniu (folosim\n pentru introducerea unui nou rand)
    print("\nSelecteaza operatia matematica dorita.\n\n0 -Adunare\n1 -Scadere\n2 -Inmultire\n3 -Impartire\n4 -Modulo\n5 -Ridicare la putere\n6 - Radical\n7 - Sinus\n8 - Cosinus\n9- Tangenta\n")
    oper= input("\nOptiunea ta: ")#Variabila care stocheaza valoarea aleasa de utilizatorul
    
    #Adunare
    if oper=="0":
        val1= float(input("\nPrima valoare: "))#Variabila care stocheaza valoare introdusa
        val2= float(input("\nA doua valoare: ")) #Variabila care stocheaza a doua valoare introdusa
        suma = val1 + val2
        print("\nREzultatul este: " + str(suma) + "\n")
        #intoarcere la meniul principal sau iesirea din program
        inapoi= input("\nMergi inapoi la meniul principal? (y/n) ")
        if inapoi=="y":
            continue
        else:
            break
    
    #Scadere
    elif oper=="1":
        val1= float(input("\nPrima valoare: "))#Variabila care stocheaza prima valoare introdusa
        val2= float(input("\nA doua valoare: ")) #Variabila care stocheaza a doua valoare introdusa
        diferenta = val1-val2
        print("\nRezultatul este: "+str(diferenta)+"\n")
        #intoarcere la meniul principal sau iesirea din program
        inapoi= input("\nMergi inapoi la meniul principal? (y/n) ")
        if inapoi=="y":
            continue
        else:
            break

    #Inmultire
    elif oper =="2":
        val1 = float(input("\nPrima valoare: "))  # Variabila care stocheaza prima valoare introdusa
        val2 = float(input("\nA doua valoare: "))  # Variabila care stocheaza a doua valoare introdusa
        inmultirea = val1 * val2
        print("\nRezultatul este: " + str(inmultirea) + "\n")
        # intoarcere la meniul principal sau iesirea din program
        inapoi = input("\nMergi inapoi la meniul principal? (y/n) ")
        if inapoi == "y":
            continue
        else:
            break

    # Inpartire
    elif oper == "3":
        val1 = float(input("\nPrima valoare: "))  # Variabila care stocheaza prima valoare introdusa
        val2 = float(input("\nA doua valoare: "))  # Variabila care stocheaza a doua valoare introdusa
        inpartirea = val1 / val2
        print("\nRezultatul este: " + str(inpartirea) + "\n")
        # intoarcere la meniul principal sau iesirea din program
        inapoi = input("\nMergi inapoi la meniul principal? (y/n) ")
        if inapoi == "y":
            continue
        else:
            break

    # Modulo
    elif oper == "4":
        val1 = float(input("\nPrima valoare: "))  # Variabila care stocheaza prima valoare introdusa
        val2 = float(input("\nA doua valoare: "))  # Variabila care stocheaza a doua valoare introdusa
        modulo = val1 % val2
        print("\nRezultatul este: " + str(modulo) + "\n")
        # intoarcere la meniul principal sau iesirea din program
        inapoi = input("\nMergi inapoi la meniul principal? (y/n) ")
        if inapoi == "y":
             continue
        else:
             break

    # Ridicare la putere
    elif oper == "5":
        val1 = float(input("\nValoarea: "))  # Variabila care stocheaza prima valoare introdusa
        val2 = float(input("\nPuterea de ridicare a valorii: "))  # Variabila care stocheaza a doua valoare (cea la care se face ridicarea la putere)
        putere = math.pow(val1,val2)
        print("\nRezultatul este: " + str(putere) + "\n")
        # intoarcere la meniul principal sau iesirea din program
        inapoi = input("\nMergi inapoi la meniul principal? (y/n) ")
        if inapoi == "y":
            continue
        else:
            break
    # Radical
    elif oper == "6":
        val1 = float(input("\nValoarea din care se extrage radicalul: "))  # Variabila care stocheaza valoarea de extractie a radicalului
        radical = math.sqrt(val1)
        print("\nRezultatul este: " + str(radical) + "\n")
        # intoarcere la meniul principal sau iesirea din program
        inapoi = input("\nMergi inapoi la meniul principal? (y/n) ")
        if inapoi == "y":
            continue
        else:
            break
            
    #Sinus
    elif oper =="7":
        val1 = float(input("\nItroduceti valoarea(in grade) pentru calcularea sinus: \n"))
        #Conversia grade -> radians
        grade= math.radians(val1)
        #Returneaza sinusul valorii in radians
        sinus= math.sin(grade)
        print("\nRezultatul este :"+str(sinus)+"\n")
        # intoarcere la meniul principal sau iesirea din program
        inapoi = input("\nMergi inapoi la meniul principal? (y/n) ")
        if inapoi == "y":
            continue
        else:
            break
            
    #Cosinus 
    elif oper == "8":
        val1 = float(input("\nIntroduceti valoarea (in grade) pentru calcularea cosinusului: \n"))
        #Conversia grade->radians
        grade= math.radians(val1)
        #Returneaza cosinusul valorii in radians
        cosinus= math.cos(grade)
        print("\nRezultatul este: "+str(cosinus)+"\n")
        # intoarcere la meniul principal sau iesirea din program
        inapoi = input("\nMergi inapoi la meniul principal? (y/n) ")
        if inapoi == "y":
            continue
        else:
            break
    #Tangenta 
    elif oper == "9":
        val1 = float(input("\nIntroduceti valoarea (in grade) pentru calcularea tangentei: \n"))
        #Conversia grade->radians
        grade= math.radians(val1)
        #Returneaza tangenta valorii in radians
        tangenta= math.tan(grade)
        print("\nRezultatul este: "+str(tangenta)+"\n")
        # intoarcere la meniul principal sau iesirea din program
        inapoi = input("\nMergi inapoi la meniul principal? (y/n) ")
        if inapoi == "y":
            continue
        else:
            break
            
    #Tratarea optiunilor invalide
    else:
        print("\nOptiune invalida!\n")
        continue
    #Final de program