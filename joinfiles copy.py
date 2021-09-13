import json

with open('master.json', 'r') as f:
    lista = json.load(f)

#filenames = ['2095303.json', '2169202.json'] 
  
# Open file3 in write mode 

with open('tryall.json', 'w') as outfile: 
  #all.json
    # Iterate through list 
    contador = 0
    helper = 0
    update =  True
    for names in lista: 
  
        # Open each file in read mode 
        
        with open(f'{names}.json') as infile:
            infile.readline()
            infile.readline()
            infile.readline()
            #outfile.write(infile.read()) 
            #outfile.write(infile.read(50))
            temp = infile.readline()
            #print((helper==temp))
            if helper != temp:
                update = True
                helper = temp
                #print(helper, temp)

            else:
                update = False

        with open(f'{names}.json') as infile: 
  
            # read the data from file1 and 
            # file2 and write it in file3 
            
            if update == True:
                #infile.readline()
                #infile.readline()
                #infile.readline()
                #outfile.write(infile.read()) 
                #outfile.write(infile.read(50))
                #outfile.write(infile.readline())
                outfile.write(infile.read()) 
    
        contador+=1
        print(contador, names)
        # Add '\n' to enter data of file2 
        # from next line 
        outfile.write("\n") 