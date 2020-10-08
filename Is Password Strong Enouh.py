def is_password_strong(password):

    symbols = ["!","@","#","$","%","^","&","*","(",")",'_','-','=','+','|','\\','/','?','.','>',',','<',';',':']

    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u''v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    number = ['0','1','2','3','4','5','6','7','8','9']
    hasnumber = False
    hassymbol = False
    islongenough = False
    hasletter = False

    if (len(password)>=8):
        for i in range(len(symbols)):
            if (symbols[i] in password):

                hassymbol = True
                break
            else:

                hassymbol = False

        for i in range(len(letters)):
            if (letters[i] in password):

                hasletter = True
                break
            else:

                hasletter = False


        for i in range(len(number)):
            if (number[i] in password):

                hasnumber = True
                break

            else:

                hasnumber = False

        islongenough = True
    else:
        islongenough = False


    return hasletter and hasnumber and hassymbol and islongenough


