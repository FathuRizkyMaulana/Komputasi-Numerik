import numpy as np

# Diberikan nilai
F = 60  # gaya dalam Newton
theta = 40  # sudut dalam derajat

# Mengonversi sudut ke radian
theta_rad = np.radians(theta)

# Menghitung komponen horizontal dan vertikal
F_x = F * np.cos(theta_rad)
F_y = F * np.sin(theta_rad)

print("Komponen horizontal (F_x):", F_x, "N")
print("Komponen vertikal (F_y):", F_y, "N")
