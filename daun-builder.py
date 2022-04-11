import shutil
import sys
import os
import modules.require  # install required modules
from modules.thread import threaded
from modules.scrape import prep, parsers, functions
import ui.main as uimain
from PyQt5 import QtCore, QtWidgets
from ui.gui import popup, cls
import tempfile

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = uimain.Ui_MainWindow()
ui.setupUi(MainWindow)

icon_path = 'ui/logo.ico'

for name in list(parsers):
    item = QtWidgets.QListWidgetItem(name)
    item.setCheckState(QtCore.Qt.Checked)
    ui.modules_list.addItem(item)

MainWindow.show()


def choose_icon():
    global icon_path
    icon_path = QtWidgets.QFileDialog.getOpenFileName(
        None,
        'Choose custom icon for daun',
        os.getenv('USERPROFILE') + '/Pictures',
        '*.ico'
    )[0]
    if icon_path == '':
        icon_path = 'ui/logo.ico'
    print(icon_path)


@threaded
def build(*args):
    tempdir = tempfile.TemporaryDirectory()
    temp = os.path.join(tempdir.name)
    ui.build_button.setEnabled(False)
    modules_to_add = list()
    for i in range(ui.modules_list.count()):
        if ui.modules_list.item(i).checkState():
            modules_to_add.append(ui.modules_list.item(i).text())
    with open('daun-to-build.py', 'w+') as f:
        f.writelines(prep['Before'])
        for module in list(parsers):
            if module in modules_to_add:
                f.writelines(parsers[module])
        f.writelines(prep['Parse args'])
        for module in list(functions):
            if module in modules_to_add:
                f.writelines(functions[module][1])

    if ui.path_box.text() == '':
        ui.path_box.setText(os.getenv('USERPROFILE') + '/Desktop/daun.exe')

    popup('Build', 'File is generated, press OK to build exe.\n'
                   'Logs will appear in terminal.')
    cls()
    if ui.is_pyinstaller.isChecked():
        os.system(f'pyinstaller --onefile --{"console" if not ui.enable_console_button.isChecked() else "windowed"} '
                  f'--noconfirm --icon {icon_path} --workpath {temp} daun-to-build.py')
        try:
            shutil.move(f'{os.getcwd()}/dist/daun-to-build.exe', ui.path_box.text())
            os.remove(f'daun-to-build.py')
        except FileNotFoundError:
            pass

    if ui.is_nuitka.isChecked():
        os.system(f'nuitka --standalone --assume-yes-for-downloads --remove-output --disable-dll-dependency-cache '
                  f'--onefile --windows-icon-from-ico={icon_path} '
                  f'{"" if not ui.enable_console_button.isChecked() else "--windows-disable-console"} daun-to-build.py')
        try:
            shutil.move(f'{os.getcwd()}/daun-to-build.dist/daun-to-build.exe', ui.path_box.text())
            os.remove(f'daun-to-build.py')
        except FileNotFoundError:
            pass

    ui.build_button.setEnabled(True)
    popup('Build', 'Builder process exited.\n'
                   'You will find the executable\n'
                   'in the path you specified\n'
                   'if the build was successful.')


show_desc = lambda: ui.desc_list.setText(functions[ui.modules_list.currentItem().text()][0])
ui.modules_list.setCurrentItem(ui.modules_list.item(0))
ui.modules_list.itemClicked.connect(show_desc)
ui.modules_list.currentItemChanged.connect(show_desc)
ui.modules_list.itemDoubleClicked.connect(lambda:
                                          ui.modules_list.currentItem().setCheckState(
                                              QtCore.Qt.Unchecked if ui.modules_list.currentItem().checkState()
                                              else QtCore.Qt.Checked
                                          )
                                          )
ui.choose_folder_button.clicked.connect(lambda:
                                        ui.path_box.setText(
                                            QtWidgets.QFileDialog.getSaveFileName(
                                                None,
                                                'Choose where to save daun',
                                                os.getenv('USERPROFILE') + '/Desktop/daun.exe',
                                                '*.exe'
                                            )[0]
                                        )
                                        )
ui.choose_icon_button.clicked.connect(choose_icon)
ui.build_button.clicked.connect(build)

sys.exit(app.exec_())
