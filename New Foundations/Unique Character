# Given an input string (inline variable string, file, networkrequest)...

# Return the count of how many times each unique character was present in the input

# e.g. 'abcda'
# a: 2, b: 1, ...

def input_str(string):
    outputs = {}
    for input in string:
        if outputs.get(input) is None:
            outputs[input] = 1
        else:
            outputs[input] += 1
