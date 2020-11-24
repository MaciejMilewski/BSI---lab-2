def problem_description(path):
    a_file = open(path)
    lines = a_file.readlines()
    for line in lines:
        line = line.rstrip("\n")
        print(line)
    print(" ")
    a_file.close()
