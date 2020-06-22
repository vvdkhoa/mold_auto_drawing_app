TESTING

PLASTIC ỊNECTION MOLD DRAWING APP

Input:  Mold dimensiton
Output: CAD data (IGES, Parasolid, STEP, FCMat)

################################
Install for Windows;
1. Dowload [mold_draw_v.01_windows_app] and save to PC (The directory must be writable).
2. Unzip the file.
3. Install free cad and setting FreeCAD path in FreeCAD_path.json file (\database\FreeCAD_path.json)
################################

########## Note for me ###########
Delete content of file __init__ before using

Can built with below
pyinstaller mold_draw.py --debug all
pyinstaller mold_ui.py --debug all
pyinstaller mold_draw.py --noconsole
pyinstaller mold_ui.py --noconsole

File main.ui > main.py
C:\Users\DELL\AppData\Local\Programs\Python\Python36\Scripts\pyside2-uic.exe main.ui -o main.py

File icons.qrc convert to icons_rc.py
C:\Users\DELL\AppData\Local\Programs\Python\Python36\Scripts\pyside2-rcc.exe icons.qrc -o icons_rc.py

Reference

Can not use
--debug all --noconsole

======
