##########################
# dice_probability.py
# Noah Ansel
# 2016-01-01
# --------------
# A program for finding probabilities of rolling arbitrary dice.
# Intended for use with non-standard types of dice. More useful
# programs exist for standard or numeric-only dice.
#########################

# Formatting for input file:
# 1. Each line represents a new die. 
# 2. Faces of a die will be separated by spaces or tabs.
# 3. To indicate multiple instances of a face on a die, use "<face name>*<number of occurences>"
# 4. To indicated multiple instances of a die, put "*<number of occurences" at the beginning of the line
# 5. Anything past a character '#' on a line will be ignored.
# 6. Empty lines will be ignored.

class Die:

  ###############
  # __init__
  #   Initializes a die from a string.
  def __init__(self, initString):
    self.sides = self.parse_string(initString)

  ###############
  # parseString
  #   Creates a list of sides from a string.
  #   Raises errors if string is formatted incorrectly.
  def parse_string(self, string):
    sidelist = string.replace("\t"," ").split(" ")

    sides = {}
    for item in sidelist:
      if item == '':
        continue
      elif item[0] == "#":
        break
      elif item not in sides.keys(): # new face
        splitItem = item.split("*")
        if len(splitItem) == 1:
          sides[item] = 1
        elif len(splitItem) == 2:
          if splitItem[0] not in sides.keys():
            try:
              sides[splitItem[0]] = int(splitItem[1])
            except Exception:
              raise IOError("File is formatted incorrectly.")
          else:
            try:
              sides[splitItem[0]] += int(splitItem[1])
            except Exception:
              raise IOError("File is formatted incorrectly.")
        else:
          raise IOError("File is formatted incorrectly.")
      else: # more of an existing face
        splitItem = item.split("*")
        if len(splitItem) == 1:
          sides[item] += 1
        elif len(splitItem) == 2:
          if splitItem[0] not in sides.keys():
            try:
              sides[splitItem[0]] = int(splitItem[1])
            except Exception:
              raise IOError("File is formatted incorrectly.")
          else:
            try:
              sides[splitItem[0]] += int(splitItem[1])
            except Exception:
              raise IOError("File is formatted incorrectly.")
        else:
          raise IOError("File is formatted incorrectly.")
    return sides


###############
# find_multiplicity
#   Finds the number of times this die should
#   be entered in the list, and returns string
#   with this data removed.
def find_multiplicity(string):
  if string[0] != "*":
    return 1, string
  else:
    if len(string) > 1:
      for i in range(1,len(string)):
        if string[i] == ' ' or string[i] == '\t':
          break
      try:
        multiplicity = int(string[1:i])
        return multiplicity, string[i:]
      except Exception:
        raise IOError("File is formatted incorrectly.")


###############
# get_combinations
#   Recursively finds all combinations of dice
#   in a list of dice, as well as how common they are.
def get_combinations(dice, index = 0, preceding_sides = [], occurences = 1):
  retList = []

  for key in dice[index].sides.keys():
    sides = preceding_sides + [key]
    new_occ = occurences * dice[index].sides[key]

    if index == len(dice) - 1: # base case
      retList.append((sides, new_occ)) # stored in tuples
    else: # recursive call
      retList += get_combinations(dice, index + 1, sides, new_occ)

  return (retList) 

def generate_output_file(filename, dice, combinations):
  f = open(filename + "_statistics.csv","w")

  # column headers
  for i in range(len(dice)):
    f.write("die " + str(i + 1) + ",")
  f.write("possibilities count,percentage chance\n")

  totalRolls = 0
  for combination in combinations:
    totalRolls += combination[1]

  for combination in combinations:
    f.write(",".join(combination[0]))
    f.write("," + str(combination[1]))
    f.write("," + "{:.2f}".format(100 * combination[1] / totalRolls) + "\n")

  f.write(","*(len(dice)-1) + "Total Rolls," + str(totalRolls) + "\n")

  f.close()

  print("[Dice Probability] Statistics written to " + filename + "_statistics.csv")

###############
# main
#   Overall program flow.
def main():

  filename = input("[Dice Probability] Please enter the file containing your dice (without '.txt'): ")
  try:
    f = open(filename + ".txt","r")
    lines = f.readlines()
    f.close()
  except Exception:
    print("[Dice Probability] Invalid file provided.")
    return

  dice = []
  for line in lines: # populate dice list
    if len(line.rstrip("\n")) > 0: # non-empty line
      multiplicity, retLine = find_multiplicity(line)
      for i in range(multiplicity):
        dice.append(Die(retLine.rstrip("\n")))
        if dice[-1].sides == {}: # empty die, so delete
          del dice[-1]

  for i in range(len(dice)): # print dice list
    print("Die {} :".format(i + 1), dice[i].sides)

  combinations = get_combinations(dice)

  generate_output_file(filename, dice, combinations)

main()