import os
import sys

width = 1280
height = 720
additonal_flags = "/EXIT"
folder = './'

def main():    
    if len(sys.argv) != 2:
        files = [each for each in os.listdir(folder) if each.endswith('.pov')]
        for file in files:
            print(f'Rendering {file} at {width}x{height}')
            os.system(f'pvengine /RENDER {file} +W{width} +H{height} +A {additonal_flags}')
    elif str(sys.argv[1]) == 'clean':
        if sys.platform == 'linux' or sys.platform == 'linux2':
            os.system('rm -rf *.png')
        elif sys.platform == 'win32':
            os.system('del /S *.png')
        elif sys.platform == 'darwin':
            print('Dont know the mac command')
        else:
            print('Invalid os')
    else:
        print(f'{str(sys.argv[1])} is invalid')
        

if __name__ == '__main__':
    main()