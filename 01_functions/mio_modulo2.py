# when the file is run as a python script: 
# $ python mio_modulo2.py
# the interpreter assigns 
# __main__ to the variable __name__
def print_module_name()->None:
    print(__name__)

if __name__=="__main__":
    print("testing")
    print_module_name() # prints __main__