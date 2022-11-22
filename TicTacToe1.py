size = 10
varLigne = "# # # # # # # # # # # # #"
varCase = "#       #       #       #"

for i in range(size):
    if ((i%3)==0):
        print(varLigne)
    else:
        print(varCase)
