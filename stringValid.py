if __name__ == '__main__':
    s = input()
  #The any() method returns True if any element of an iterable is true. If not, this method returns False.
    print (any(c.isalnum() for c in s ));
    print (any(c.isalpha() for c in s));
    print (any(c.isdigit() for c in s));
    print (any(c.islower() for c in s));
    print (any(c.isupper() for c in s));