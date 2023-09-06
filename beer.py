def main():
    i = 99
    while i != 0:
        if i != 1:
            print(f"""{i} bottles of beer on the wall {i} bottles of beer
take one down pass it around {i-1} bottles of beer on the wall""")
        else:
            print(f"""{i} bottle of beer on the wall {i} bottle of beer
take one down pass it around {i-1} bottles of beer on the wall""")
        i -= 1

if __name__ == "__main__":
    main()
