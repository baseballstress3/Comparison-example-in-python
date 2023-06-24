from math import sqrt
m = 2; n = 4
if m * m == n :
print("2 times 2 is four.")
x = sqrt(2);y = 2.0
if x * x == y :
print("sqrt(2) times sqrt(2) is 2")
else :
print("sqrt(2) times sqrt(2) is not two but %.18f" % (x * x))
EPSILON = 1E-14
if abs(x * x - y) < EPSILON :
print("sqrt(2) times sqrt(2) is approximately 2")
s = "120"
t = "20"
if s == t :
comparisun = "is the same as"
else :
comparisun = "is not the same as"
print("The string '%s' %s the string '%s'." % (s, comparisun, t))
u = "1" + t
if s != u :
comparisun = "not "
else :
comparisun = ""
print("The strings '%s' and '%s' are %sidentical." % (s, u, comparisun))
