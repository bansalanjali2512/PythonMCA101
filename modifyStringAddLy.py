def modifyString(string):
    length = len(string)
    if(length < 3):
        return string
    else:
        last3chars = string[length-3:length]
        if(last3chars == 'ing'):
            return string+'ly'
        else:
            return string+'ing'

def main():
    string = input('Enter String: ')
    print('Modified String Is: ',modifyString(string))

if __name__ == '__main__':
    main()