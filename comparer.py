import base64 

def comparerTxt(input_file,input_file2,):

    

    with open(input_file, "r") as arr1: 
        first =arr1.read()

    with open(input_file2, "rb") as arr2: 
        secondBase64 = base64.b64encode(arr2.read())

    #decoded1 = base64.decodebytes(firstBase64)
    decoded2 = base64.decodebytes(secondBase64)


    #y1=''.join([bin(i)[2:].zfill(8) for i in decoded1])
    y2=''.join([bin(i)[2:].zfill(8) for i in decoded2])
    first = first.replace('[', '').replace(']', '').replace(' ', '').replace(',', '')
    
    num_differences = 0
    for i in range(len(first)):
        if first[i] != y2[i]:
            num_differences += 1
    
    

    if num_differences != 0:
        BER = num_differences/len(first)
    else:
        BER = 0
    print("\n   ---> BER = " + str(BER))
    input("\n\nCarregue em qualquer tecla para voltar ao menu.")
    




