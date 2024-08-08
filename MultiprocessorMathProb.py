def singleprocessor():
    ns = int((120 - 20) / 0.1)
    return ns
single_de = singleprocessor()

nu = 0
pc = 70
de = 1
def multiprocessor(nu, pc, de):
    nu = input("What is the data entry?: ")
    try:
        number = int(nu)
        if number == 2*de and number %  2 == 0:
            pc += 5
            de *= 2
            if pc == 120:
                print("Congrats! Your multiprocessor has reached the limit of 120ms." "\n" "Your multiprocessor can prepare and copy: " + str(de) + " data entries")
                print()
                total = de - single_de
                print("Know we know that both your MULTIPROCESSOR data entries and SINGLE PROCESSOR data entry are " + str(de)+ " and " + str(single_de))
                print("So its obviously that the MULTIPROCESSOR can prepare and copy " + str(total) + " more data entries.")
                print("That is all, thank you for using my program")
                print("Signing off, Benn.")           
            else:
                print("Great, but there is not enough data entry to reach the limit of 120ms. Continue!\n" "Your current speed of preparing and copying data entry: " + str(pc)+"ms")
                multiprocessor(nu, pc ,de)
            
        #check for odd number
        else:
            print("This is not double the number of your current data entry\n" "Your current data entry: " + str(de))
            multiprocessor(nu, pc, de)
    except ValueError:
        print("Sorry, your input must be an Integer. Please try again!")
        multiprocessor(nu, pc, de)

def intro(single_de):
    print("Question: A single processor takes 20 milliseconds (ms) to prepare data entries and 0.1n ms to copy the entries, where n is the number of entries. A multiprocessor takes 70 ms to prepare and copy one data entry, and whenever the number of entries is doubled, the amount of time to prepare and copy them increases by 5 ms. Given 120 ms to prepare and copy data entries, which processor type can prepare and copy more entries and how many more entries can it prepare and copy?\n")
    step1 = input("Now, I have written this code to help you solve this question! Type in 'Next' to continue! ")
    step1_low = step1.lower().strip()
    if step1_low == "next":
        print("Awesome! After some calculations, I think we need to figure out the numbers of data entries in both the single processor and multiprocessor.\n")
        print("Your single processor with the limits of 120ms has can prepare and copy the total of " + str(single_de) + " data entries")
        step2 = input("Knowing that your SINGLE PRCOESSOR can produce 1000 data entries, then whats about your MULTIPROCESSOR? Type 'Next' to continue. ")
        step2_low = step2.lower().strip()
        if step2_low == "next":
            print("Now I need your help on this! By typing in the INTEGERS for how many data entries you think will be needed in order for your MULTIPROCESSOR to reach its limited of 120ms, this program will help you to know the total number of data entries it needed")
            print("Start with 2")
            print()
            multiprocessor(nu, pc, de)
        else:
            print("Oh no, you typed the wrong word, please start again!\n")
            intro()
    else:
        print("Oh no, you typed the wrong word, please start again!\n")
        intro()

intro(single_de)
