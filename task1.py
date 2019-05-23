
# source - https://www.sanfoundry.com/python-program-copy-contents-file-another/#

with open("test.txt") as f:
    with open("out.txt", "w") as f1:
        for line in f:
            f1.write(line)
