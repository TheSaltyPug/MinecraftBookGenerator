import math

# Parts of the generate function are loosely based on TheWii's function that works similarly.
"""Generates the book's pages"""
def generate(list, max_chars):
    count = 0
    page_count = 1

    rv = '''\"{\\"text\\":\\"'''

    for line in list:
        words = line.split()
        if len(words) > 0:
            for i in range(0,len(words)):
                # check for " and '
                words[i] = words[i].replace('\"','\\\\\\\"')
    
                if len(words[i]) + count <= max_chars:
                    rv = rv + words[i]
                    count += len(words[i])
                    if i != len(words)-1:
                        rv = rv + ' '
                        count += 1
                else:
                    rv = rv + '''\\"}\",\"{\\"text\\":\\"''' + words[i] + ' '
                    count = len(words[i]) + 1
                    page_count += 1
        else:
            rv = rv + '\\\\n'
            count += 2
    else:
        rv = rv + '''\\"}\"'''

    return rv, page_count


"""The main function; called when the program is run."""
def main():
  
    max_chars = 250

    # get the input filename
    input_file = input(">> Enter the name of the input file: ")

    # open file
    with open(input_file, 'r') as rf, open("output.txt", 'w') as of:
        print(">> Reading file " + input_file)
        all_lines = rf.readlines()

        # error checking, statistics
        total_characters = 0
        for line in all_lines:
            total_characters += len(line)
        predicated_pages = math.ceil(total_characters/max_chars)
        print(">> Total character is " + str(total_characters) + " for a page length of " + str(predicated_pages) + ".")

        if predicated_pages > 100:
            print(">> Predicated page length is above the maximum for Minecraft. Aborting.")
            return

        print(">> Predicated page length is below the maximum for Minecraft. Continuing.")

        # generate
        print(">> Generating...")
        # define some variables
        title, subtitle, author = all_lines[0], all_lines[1], all_lines[2]
        output,total_pages = generate(all_lines, max_chars)
        
        print("Generating complete.")

        # recompile generated string data into give command
        final_output = "/give @p written_book{pages:[" + output +"],title:\"" + title +"\",author:" + author + "}" 

        # write to output file
        of.write(final_output)
        print(">> Give command written to output.txt in this directory")
        
        # print statistics
        print(">> Predicated pages: " + str(predicated_pages))
        print(">> Actual pages: " + str(total_pages))

    return

if __name__ == "__main__":
    main()
