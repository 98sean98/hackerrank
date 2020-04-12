import sys

var = []
for value in sys.stdin:
    var.append(int(value.strip()))

# sys.stdout(var[0] + var[1])
result = var[0] + var[1]
sys.stdout.write(str(result))
