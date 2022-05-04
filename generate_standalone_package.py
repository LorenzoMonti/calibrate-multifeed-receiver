import os
import platform
import shutil
import subprocess

HERE = os.path.dirname(os.path.realpath(__file__))

if __name__ == '__main__':
    operating_system = platform.system()
    if operating_system.lower() == 'darwin':
        operating_system = 'macOS'
    machine_type = platform.machine()

    subprocess.run(
        [
            "pyinstaller",
            "--noconfirm",
            "--clean",
            "--name", "calibrate_receiver",
            "--onefile",
            "--paths", "C:\\Users\\loren\\AppData\\Local\\Programs\\Python\\Python38\\Lib\\site-packages\\",
            "--hidden-import", "pyvisa",
            "--windowed", #"--console",
            "src/gui_support.py"
        ],
        check=True)