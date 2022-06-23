def CtoFconverter():
    while True:
        Ctemp = input("please enter C degrees : ")
        if Ctemp:
            Ctemp = float(Ctemp)
            Ftemp = round(9*Ctemp/5 + 32)

            print(f"{Ctemp}*C is convert to {Ftemp}*F ")
            break

        else:
            print("Have no input degrees")
            continue









def main():
    #print("Starting")
    CtoFconverter()
if __name__ == '__main__':
    main()