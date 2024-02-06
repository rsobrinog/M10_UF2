def shop(d):

    fr = []

    for x in d:
        val = d[x]

        fr.append((val / 100) * x)

    gprice = sum([x for x in fr])

    final_price = ((gprice * (int(input('iva\n')) / 100)) + gprice)
                 
    print(f"final price : {final_price}\noriginal price : {gprice}")

shop({100:10, 250:5, 1500:30})

###########################################################################################

# a = input("a\n")
# b = input("b\n")

# print(b[0:2] + a[2:-1] + a[-1] + " " + a[0:2] + b[2:-1] + b[-1])

############################################################################################

# import random

# try_ = 0
# secr = random.randint(1, 100)
# num = ""

# while int(num := input("num\n")) != secr:
#     print("the number is " + ("lower than" if int(num) < secr else "bigger than") + " the number you gave")
#     try_ += 1 #kek3

# print("secret " + str(secr) + "\n" +
#       "tries " + str(try_))

