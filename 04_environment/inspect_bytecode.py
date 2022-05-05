import dis

with open("sum_function.py") as f:
    code_string = f.read()

bytecode = dis.Bytecode(code_string)
bytecode_string = bytecode.dis()
print(bytecode_string)
