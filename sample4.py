# Given an array, shuffle the array without duplicates
# random()
# reset()

import random

class RandomArray:
    def __init__(self, original_array):
        self.length = len(original_array)
        self.original_array = original_array

        # self.length = len(original_array)
        # self.loc_map = dict()
        # for i in range(len(original_array)):
        #     item = original_array[i]
        #     self.loc_map[item] = i

    def random(self):
        new_arr = [0] * self.length
        already_used_index = set()
        for i in range(self.length):
            orig_index = i
            key = self.original_array[i]
            while True:
                random_index = random.randint(0, self.length-1)
                # print (random_index, orig_index)

                if random_index == orig_index and len(already_used_index) == self.length - 1:
                    break

                if random_index != orig_index and random_index not in already_used_index:
                    new_arr[random_index] = key
                    already_used_index.add(random_index)
                    break
                else:
                    pass
                    #print(already_used_index)

        return new_arr

    def reset(self):
        # new_arr = [0] * len(self.loc_map)
        # for key, orig_index in self.loc_map.items():
        #     new_arr[orig_index] = key

        return self.original_array

if __name__ == "__main__":
    inp_arr = [1, 3, 9, 5, 8]
    random_array = RandomArray(inp_arr)
    print(random_array.random())
    print(random_array.random())
    print(random_array.reset())

####################
# interface Sample{
#     default
# }

class Sandeep{
    public static void print(String n){
        System.out.println("name " + n);
    }

    public static void main(){
        ArrayList < Integer > Numbers = new ArrayList <Integer>();
        Numbers.forEach((n) -> {System.out.println(n)});
        Numbers.forEach((n) -> print(n));
    }
}

################
