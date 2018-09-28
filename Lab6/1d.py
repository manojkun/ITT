with open("mail1.txt",'r') as name:
         with open("mail2.txt",'r') as name2:
                 mail = name.read()
                 mail += name2.read()
                 with open("mail3.txt",'w') as nm3:
                         nm3.write(mail)

