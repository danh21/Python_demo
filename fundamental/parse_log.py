log_file = open('assets/googletest-output-test-golden-lin.txt', 'r')
Lines = log_file.readlines()
 


print("Number of")

# Strips the newline character
for line in Lines:
    if line.find("[==========] [mRunning ") != -1:
        startIndex = line.find("[==========] [mRunning ") + len("[==========] [mRunning ")
        print("\tTest Ran:", line[startIndex : startIndex + 2])

    if line.find("[  PASSED  ] [m") != -1:
        startIndex = line.find("[  PASSED  ] [m") + len("[  PASSED  ] [m")
        print("\tTest Passed:", line[startIndex : startIndex + 2])

    if line.find("[  SKIPPED ] [m") != -1:
        startIndex = line.find("[  SKIPPED ] [m") + len("[  SKIPPED ] [m")
        if line[startIndex].isnumeric():
            print("\tTest Disabled:", line[startIndex : startIndex + 2])

    if line.find("[  FAILED  ] [m") != -1:
        startIndex = line.find("[  FAILED  ] [m") + len("[  FAILED  ] [m")
        if line[startIndex].isnumeric():
            print("\tTest Disabled:", line[startIndex : startIndex + 2])