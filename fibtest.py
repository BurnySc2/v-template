from ctypes import CDLL
import platform

filename = ""
if platform.system() == "Linux":
    filename = "fibrec.so"
elif platform.system() == "Darwin":
    filename = "fibrec.dylib"
elif platform.system() == "Windows":
    filename = "fibrec.dll"
assert filename, "Unknown platform"

libfibrec = CDLL(f"./{filename}")

result = libfibrec.fib(40)
print(result)

assert result == 102334155
