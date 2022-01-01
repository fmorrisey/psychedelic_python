G = 6.67 * (10 ** -11)
M = 6.0 * (10 ** 24)  # Mass of Earth
m = 7.34 * (10 ** 22)  # Mass of the moon
r = 3.84 * (10 ** 8)

grav_force = (G * M * m) / (r ** 2)
print(grav_force)

grav_Const = 1.9920979817708333e+20

if (grav_force == grav_Const):
    print("The Universe Exist!")

else :
    print("check your reality")

