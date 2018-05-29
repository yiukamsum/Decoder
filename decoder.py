#!/usr/bin/env python
# -*- coding: utf-8 -*-

class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False
    
    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration
    
    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args: # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False

def caesar_cipher():
    import sys
    contents = ""
    print("Please Enter The Text (Leave a line and click Ctrl+D when you finish your input")
    for line in sys.stdin:
        contents += line
    print("-------------------Caesar Cipher--------------------")
    new = [""] * 25
    print("+0\t" + contents.replace("\n", "\n\t"))
    for num in range(0, 25):
        for i in range(0, len(contents)):
            if ord(contents[i]) >= 97 and ord(contents[i]) <= 122:
                if ord(contents[i])+num +1 >  122:
                    new[num] += chr(ord(contents[i])+num +1 -26)
                else:
                    new[num] += chr(ord(contents[i])+num +1)
            elif ord(contents[i]) >= 65 and ord(contents[i]) <= 90:
                if ord(contents[i])+num +1 >  90:
                    new[num] += chr(ord(contents[i])+num +1 -26)
                else:
                    new[num] += chr(ord(contents[i])+num +1)
            else:
                new[num] += contents[i]
                continue


    for abc in range(0, 25):
        print("+" + str(abc + 1) + "\t" + new[abc].replace("\n", "\n\t"))
    main()

def base64():
    import base64
    print("Result:\n"+base64.b64decode(input("Please Enter The Text:\n")).decode("utf-8"))
    main()

def main():
    print("\n---------------------------Decoder---------------------------\n")
    for case in switch(input('''(1)Base64\t(2)Caesar Cipher \nCtrl+C to Stop This\n''')):
        if case('1'):
            base64()
            break
        if case('2'):
            caesar_cipher()
            break
        if case('3'):
            import hashlib
            import sys
            import time
            def timing(f):
                def wrap(*args):
                    time1 = time.time()
                    ret = f(*args)
                    time2 = time.time()
                    print("%s Time: %0.3f s" % (f.func_name, float(time2 - time1)))
                    return ret
                return wrap
            @timing
            def decryptMD5(testHash):
                s = []
                while True:
                    m = hashlib.md5()
                    for c in s:
                        m.update(chr(c).encode("utf-8"))
                    hash = m.hexdigest()
                    if hash == testHash:
                        return ''.join([chr(c) for c in s])
                    wrapped = True
                    for i in range(0, len(s)):
                        s[i] = (s[i] + 1) % 256
                        if s[i] != 0:
                            wrapped = False
                            break
                    if wrapped:
                        s.append(0)
            print(decryptMD5("9743a66f914cc249efca164485a19c5c".encode("utf-8")))
            break
        if case(): # default, could also just omit condition or 'if True'
            print("Error!")
            main()
# No need to break here, it'll stop anyway

main()

