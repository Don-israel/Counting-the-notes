# Taking total amount as input from user
Amount=int(input("Please Enter Amount For withdraw :"))

#Calculating the number of notes of different denomination
note_1 = Amount//100
note_2 = (Amount%100)//50
note_3 = ((Amount%100)%50)//10
print("note of 100 naira", note_1)
print("note of 50 naira",note_2)
print("note of 10 naira",note_3)