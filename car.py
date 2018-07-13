# # permissions: r: read only, w: write only, a: appending, r+: read and write

# # with open(filename, permissions) as

# with open("test.txt", 'w') as testfile:
#     testfile.write("Hello, c25. Hope you're good. yep yep yep.")

# with open("test.txt", 'a') as testfile:
#     testfile.write("Hello, c25. Hope you're awake")

# nick_names = {"The Cracker", "Ole Red", "Bubba", "Cat Lady"}

# names = {"Matt kelly", "John Smith", "Em Coo"}

# with open("data/nicknames.txt", "w") as nicknames:
#     for nick in nick_names:
#       nicknames.write(nick + '\n')


# with open("data/nicknames.txt", "r") as nicks:
#     nicklist = nicks.readlines()
#     print(nicklist)

# with open("data/namelist.txt", "r") as nicks:
#     namelist = names.readlines()
#     print(namelist)

# mob_names = [f"{name.strip().split(' ')[0]} \"{nick_names[i].strip()}\" {names.strip().split(' ')[1]}"
#     for i, name in enumerate(namelist)]

# # print(mob_names)

class Car():

    # def __init__(self):

    def read_makes(self):
        with open("car_makes.txt", "r") as makes:
            car_makes = makes.readlines()
            return car_makes

    def read_models(self):
        with open("car_models.txt", "r") as models:
            car_models = models.readlines()
            return car_models

    def make_and_model(self):
        make = self.read_makes()
        model = self.read_models()
        mod = []
        cars = dict.fromkeys(make, mod)
        # print(cars)

        for c in cars:
            # print(cars[c]) prints value of c
            # print(c[0]) prints first letter
            # print("first loop")
            for mo in model:
                # print("second loop")
                # print(mo[0])
                if (mo[0] == c[0]):
                    # print("if statement")
                    # cars[c].append(mo)
                    mod.append(mo)

                # print(cars)
                    # print(mo)
                    print(cars )
                #     mod.append(mo)
        # print(cars)





        # print(cars)

        # print(make[0][0])
        # print(model[0])

car = Car()

car.make_and_model()


        # vowels keys
        # keys = {'a', 'e', 'i', 'o', 'u' }
        # value = [1]

        # vowels = dict.fromkeys(keys, value)
        # print(vowels)

        # # updating the value
        # value.append(2)
        # print(vowels)

        # for m in make:
        #     for mo in model:
        #         if (m in make and m[0] == mo[0]):
        #             car_dict[m] = mo
        #         else:
        #             car_dict[m] = mo
        #         print(car_dict)



# rocky_planets = planet_list[0:4]
# del(planet_list[7])

# planet_launches = {}

# for launch in launches:
#      if launch[0] in planet_launches:
#          planet_launches[launch[0]]+= launch[1],
#      else:
#          planet_launches[launch[0]] = launch[1],


# for planet, launch in planet_launches.items():
#     print(f'{planet}: {launch}')



# print(car.read_makes())

# print(car.read_models())

