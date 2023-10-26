import PetStores

pets = PetStores.PetStore()
# pets.store_details('Dog','Rocky','pitbull','5','MP',45000)
# pets.store_details('dog','Nawab','husky','8','Delhi',50000)
# pets.store_details('cat','Kitty','wild','3','Mizoram',20000)
# pets.store_details('parrot','Rhio','indian','3','Mumbai',10000)
# pets.store_details('dog','Sheebu','golden retriever','8','UP',55000)
# pets.display_pets()
# pets.search_pets('dog') 
# pets.search_pets('hamster') 
# pets.sell_pet('rhio','parrot','Indian')
# pets.sell_pet('Charlie','dog','pug')

while True:
    print('MENU:')
    print('1. Add a  pet')
    print('2. List the pets') 
    print('3. Search a pet')
    print('4. Sell a pet')
    print('5. Quit')

    choice = int(input('Enter your choice:'))
    print('Your entered choice is',choice)

    if choice == 1:
        type = input('Enter the type of pet:')
        name = input('Enter the name for the pet:')
        breed = input('Enter the breed of the pet:')
        age = input('Enter the age of the pet:')
        bp = input('Enter the birthplace of the pet:')  
        pp = int(input('Enter the price of the pet:'))
        pets.store_details(type,name,breed,age,bp,pp)
        print('Details has been entered!!')
    elif choice == 2:
        pets.display_pets()
    elif choice == 3:
        typ = input('Enter the type of pet to be searched:')
        pets.search_pets(typ)
    elif choice == 4:
        name = input('Enter the name of the pet:')
        type = input('Enter the type of the pet:')
        breed = input('Enter the breed of the pet:')
        pets.sell_pet(name,type,breed)
    elif choice == 5:
        break
    else:
        print('Invalid choice. Please try again!')