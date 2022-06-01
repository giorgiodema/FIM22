import dis
import os

# python non è un linguaggio compilato ma neanche propriamente un 
# linguaggio interpretato. Il codice python infatti viene convertito 
# in bytecode, che viene eseguito direttamente dall'interprete. Per ispezionare
# il bytecode che viene generato per un programma si può usare 
# il modulo dis
with open(os.path.join("00_environment","example_program.py")) as f:
    code_string = f.read()

bytecode = dis.Bytecode(code_string)
bytecode_string = bytecode.dis()
print(bytecode_string)
