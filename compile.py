#Coding : utf-8
#Code by: MR.AKING
#Github : AKING110
#------------------
try:
    import os,cython
    from Cython.Build.BuildExecutable import build
except:
    os.system('pip install cython > /dev/null')
def en():
    os.system('clear')
    print(' Code By AKING \n----------------')
    print('\033[1;37m 1 -> Compile Cython \n 2 -> Compile ELF (ex: \033[1;32m./run\033[1;37m)\n 0 -> Exit ')
    x = input(' -> Opt: ')
    if x =='1':
        os.system('clear')
        file = input(' Put File: ')
        try:
            open(file,'r').read()
        except:
            exit(' File Location Not Found ')
        os.system('cythonize -i -2 '+file+'> /dev/null')
        input(' Your File Compile Done Enjoy ');en()
    elif x =='2':
        os.system('clear')
        file=input(' Put File: ')
        try:
            open(file,'r').read()
        except:
            exit(' File Location Not Found ')
        build(file)
        input(' Your File Compile Done Enjoy ');en()
    else:
        exit(' Successful exit ')
en()
