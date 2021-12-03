from matplotlib.pyplot import *


x, y1, y2, y3 = [], [], [], []
for i in range(11):
    x.append(i)
    y1.append(i)
    y2.append(i ** 2)
    y3.append(i ** 3)
plot(x, y1, "r--", label="x")
plot(x, y2, "go", label="x^2")
plot(x, y3, "bs", label="x^3")
axis([0, 10, 0, 100])
title("my diagram")
xlabel("x")
ylabel("y")
grid(True)
legend()
show()
