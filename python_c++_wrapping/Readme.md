# Compilet with :

'''bash
gcc -Iscr -fPIC $(pig-config --cflags --libs python3) -c src/hw.c hw_wrap.c
gcc -shared -fPIC -o hw.so hw.o hw_wrap.o -framework Python
'''


# Test with :
'''bash
python test.py
'''
