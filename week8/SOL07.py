# Function to return all anagrams together
def allAnagram(input):
    # empty dictionary which holds subsets
    # of all anagrams together
    dict = {}

    # traverse list of strings
    for strVal in input:

        # sorted(iterable) method accepts any
        # iterable and returns list of items
        # in ascending order
        key = str(sorted(strVal))

        # now check if key exist in dictionary
        # or not. If yes then simply append the
        # strVal into the list of it's corresponding
        # key. If not then map empty list onto
        # key and then start appending values
        if key in dict.keys():
            dict[key].append(strVal)
        else:
            dict[key] = []
            dict[key].append(strVal)

        # traverse dictionary and concatenate values
    # of keys together
    output = ""
    for key, value in sorted(dict.items(), key=lambda kv: (len(kv[1]), kv[0])):
        output = output + ' '.join(value) + ":" + str(len(value)) + '\n'

    return output


# create an empty set
input = set()
# read all the data from the file and put them in a set
f = open('data.txt')
for word in f.read().split():
    input.add(word)
f.close()

print(allAnagram(input))
