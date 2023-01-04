def binary_search(lista):
    number = int(input("Enter a number: ")) #Ta emot en siffra att hitta från användaren
    first_row = 0
    last_row = len(lista)-1 #Sätt last_row till sista raden genom att ta antal rader minus 1 (ger rätt index)
    first_col = 0
    last_col = len(lista[first_row]) - 1 #Sätt last_col till sista kolumnen genom att ta antal kolumner minus 1 (ger rätt index)

    while (first_row <= last_row and first_col <= last_col): 
        mid_row = (first_row + last_row) // 2 #Beräkna mitten av alla rader, avrunda uppåt till heltal (en ny mitt beräknas beroende på rad 16 o 19)
        mid_col = (first_col + last_col) // 2 #Beräkna mitten av alla kolumner, avrunda uppåt till heltal (en ny mitt beräknas beroende på rad 24 o 28)

        if (lista[mid_row][mid_col] == number): #Starta genom att kolla i middle row och i middle of columns
            return [mid_row, mid_col] #Returnera platsen, index för rad och kolumn, ifall vi prickar rätt siffra

        # Number must be in further row if:
        elif (lista[mid_row][last_col] < number): #Kolla mittersta raden som räknades ut i rad 9 och sista kolumnen, ifall vår siffra < användarens siffra.
            first_row = mid_row + 1 #Om den är mindre så sätt/flytta first_row till mid_row (som vi kollat) och hoppa upp en rad(+1)

        # Number must be in previous row if:
        elif (lista[mid_row][first_col] > number): #Kolla mittersta raden som räknades ut i rad 9 och första kolumnen, ifall vår siffra > användarens siffra.
            last_row = mid_row -1 #Om den är större så sätt/flytta last_row till mid_row (som vi kollat) och hoppa ner en rad(-1)
# Number must be in previous column if:
        elif (lista[mid_row][mid_col] < number): #Kolla mittersta a raden som räknas ut i rad 9 samt mittersta kolumnen (se rad 10), ifall vår siffra < användarens siffra.
            first_col = mid_col + 1 #Om den är mindre så sätt/flytta first_col till mid_col (som vi kollat) och hoppa upp en kolumn (+1).

        # Number must be in next column if:
        elif (lista[mid_row][mid_col] > number): #Kolla mittersta a raden som räknas ut i rad 9 samt mittersta kolumnen (se rad 10), ifall vår siffra > användarens siffra.
            last_col = mid_col -1 #Om den är större så sätt/flytta last_col till mid_col (som vi kollat) och hoppa ner en kolumn (-1).

    #Number is not in the arrays, ex "2":
    return False 

test_list = [
    [3, 5, 7, 8, 11, 14, 19, 20, 21],
    [22, 25, 35, 36, 47, 50, 53, 55, 56],
    [76, 86, 94, 96, 100, 102, 108, 109, 111],
    [119, 120, 140, 145, 150, 161, 171, 178, 179],
    [201, 204, 209, 250, 256, 267, 289, 290, 291],
    [299, 302, 308, 311, 321, 323, 327, 329, 330]
]

print(binary_search(test_list))


#PSEUDO
# Create a function that accepts a list.
# Take a target number to find as input from the User.
# Declare first and last column, and first and last row.
# Create a while loop which lasts until first row > last row and first column > last column
#     Calculate the middle row and middle column
#     Start from the middle row and middle column and chech if equals number from input.else
#         if so, return the position
#     Check if on right row
#         if not jump up/down until positioned in right row.
#     Check if on right column
#         if not, go to half of the columns in that row 
# If number from user does not exist in the list, return false.