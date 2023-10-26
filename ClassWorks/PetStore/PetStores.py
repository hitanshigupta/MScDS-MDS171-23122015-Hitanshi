# Create a petstore class where you have the details of pets available and their details,
# The class will have the methods for:
# Store a new pet details
# Search for a pet
# Sell a pet
# List all pets

# Importing your petstore class, create a petstoremain file, where you will implement a menu driven
# program for Admin - who will manage the store and user who will see the pets and buy pets.


class PetStore:

    def __init__(self):
            
            self.pets = []
            self.search = []

    def store_details(self,type,name,breed,age,bp,pp):
        details = { 
            'Type' : type.strip().title(),
            'Name' : name.strip().title(),
            'Breed' : breed.strip().title(),
            'Age' : age.strip().lower(),
            'Birthplace' : bp.strip().title(),
            'Price' : pp
        }
        self.pets.append(details)

    def display_pets(self):
        print('The store has the following pets:')
        for i in self.pets:
            print(i)

    def search_pets(self,typ):
        typ = typ.strip().title()
        found = False

        for i in self.pets:
            if i['Type'] == typ:
                found = True
                self.search.append(i)

        if found == False:    
            print('Sorry!!',typ,'NOT found!')
        else:
            print('The search is successful with the following details:')
            for i in self.search:
                print(i)

    def sell_pet(self,name,type,breed):
        name = name.strip().title()
        type = type.strip().title()
        breed = breed.strip().title()
        found = False

        for i in self.pets:
            if i['Name'] == name and i['Type'] == type and i['Breed'] == breed:
                found = True
                self.pets.remove(i)
                print(name,'A',type,'of breed:',breed,',has been sold!!')
        
        if found == False:
            print('Pet not available to be sold!!')
                
         

