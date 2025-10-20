while (word := input("Enter a sentence: ")).lower() != "stop" :
    count = 0
    for w in word.split():
        if len(w) >= 5:
            count += 1
        else:
            pass
    print(f"There are {count} long words!")
    

