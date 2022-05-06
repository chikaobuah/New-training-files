filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = []
newfilenames = filenames.copy()

for index, filename in enumerate(newfilenames) :
    if filename.endswith('hpp'):
        newfilenames[index] = filename.replace('hpp', 'h')
    


print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]
