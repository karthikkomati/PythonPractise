def wordCount(name,length):
    with open(name) as file:
        count = [word for line in file for word in line.split()]
        print ("Total words:",len(count))
        v = 0
        l = 0
        vowel = ["a","e","i","o","u"]
        for w in count:
            if set('aeiou').intersection(w.lower()):
                v += 1
            if(len(w)==length):
                l += 1
        print("Words with vowels:",v)
        print("Words with lenght {}:".format(length),l)
    return len(count),v,l
        

    
a,b,c = wordCount("test.txt",1)


