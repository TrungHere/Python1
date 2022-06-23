def CtoFconverter():
 
    while True:
        Ctemp = input("please enter C degree :")
        if Ctemp:
            Ctemp = int(Ctemp)
            Ftemp = 9*Ctemp/5 + 32

            print(f"{Ctemp}C is convert to {Ftemp}F")
            break
        else:
            print("have no input to convert")
            continue






def main():
    #print("hello world")
    CtoFconverter()
if __name__ == "__main__":
    main()