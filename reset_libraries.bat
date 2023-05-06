pip freeze > installed_libs.txt
pip uninstall -r installed_libs.txt -y
del installed_libs.txt