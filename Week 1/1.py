import datetime
import sysconfig
import platform

date_time = datetime.datetime.now()
python_version = sysconfig.get_python_version()
os_name = platform.system()
os_version = platform.version()

print("Hello, World!")
print("Successful test at ")
print(date_time)
print("Python version:", python_version)
print("Operating System:", os_name)
print("Operating System Version:", os_version)