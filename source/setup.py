from cx_Freeze import setup, Executable
packages = ['matplotlib.backends.backend_qt4agg']

target = Executable(
	script="calculator.py",
	icon="icon.ico")

setup(name='Plancials',
	version='1.1',
	description='A simple break-even calulcator',
	options={'build_exe': {'packages':packages}},
	executables=[target])

# python setup.py build
# make sure the 'icon.ico' file is in the same subdirectory 