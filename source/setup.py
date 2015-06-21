from cx_Freeze import setup, Executable
packages = ['matplotlib.backends.backend_tkagg']

target = Executable(
	script="calculator.py",
	icon="icon.ico")

setup(name='Plancials',
	version='1.0',
	description='A simple break-even calulcator',
	options={'build_exe': {'packages':packages}},
	executables=[target])