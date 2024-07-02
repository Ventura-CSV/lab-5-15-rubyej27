
def consonant(strval):
    for char in strval:
        if char.lower() not in 'aeiou' and char.isalpha():
            yield char
    
   ##################################################
   # make your code
   ##################################################


def main():
    strval = 'Python Programming'
    mygen = consonant(strval)

    rlst = list(mygen)
    print(len(rlst))
    for v in rlst:
        print(v, end=' ')
    print()


if __name__ == '__main__':
    main()
