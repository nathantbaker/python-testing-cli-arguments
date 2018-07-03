import sys

# Print arguments in CLI if they are passed

def main(args):
  print("Arguments:", args)

if __name__ == "__main__":
  main(sys.argv[1:])

# Setup a Lootbag as a definition to store temporary data



class loot():

    def add_toys(name, toys):

        bag = {}
        bag['name'] = name
        bag['toys'] = toys

        #print key and values
        for key in bag:
            if key == 'name':
                print('Name: %s' % bag[key])
            elif key == 'toys':
                print('Toys: %s' % bag[key])

loot.add_toys('Frank', ['Meth', 'Spiders', 'Hot Liquids'])


  # working with files

  # class Cars:

  # def __init__(self):
  #   pass


  # def read_car_makes(self):

  #   with open("data/car-makes", "r") as make_file:
  #     car_makes = { make[:-1] for make in make_file }

  #   return car_makes


  # def read_car_models(self):

  #   with open("data/car-models", "r") as model_file:
  #     car_models = { model[:-1] for model in model_file }

  #   return car_models


  # def create_collection(self):

  #   makes = self.read_car_makes()
  #   models = self.read_car_models()

  # from datetime import datetime
  # from time import time

  # def log(message):
  #   with open('messages.log', 'a+') as logger:
  #       timestamp = time()
  #       logger.write("{0}: {1}\n".format(
  #           datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S'),
  #           str(message)
  #       ))


# f = open('messages.log', 'w')
# f.write('This is a test\n')

# def log(message):
#   with open('messages.log', 'a+') as logger:
#     logger.write("hi")



