import math
import matplotlib.pyplot as plt

G = 6.674e-11

def orbital_velocity(M, r):
    return math.sqrt(G * M / r)

def centripetal_acceleration(v, r):

    return v ** 2 / r

def orbital_period(v, r):
    return (2 * math.pi * r) / v

def plot_orbit(r):
    theta = [i * math.pi / 180 for i in range(360)]
    x = [r * math.cos(t) for t in theta]
    y = [r * math.sin(t) for t in theta]

    plt.figure(figsize=(6, 6))
    plt.plot(x, y, label="Orbital Path")
    plt.scatter(0, 0, color="orange", label="Central Body")
    plt.title("Orbital Path Visualization")
    plt.xlabel("x (m)")
    plt.ylabel("y (m)")
    plt.axis("equal")
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    print("Orbital Motion Calculator")


    try:
        M = float(input("Enter mass of the central body (kg): "))
        r = float(input("Enter orbital radius (m): "))

        v = orbital_velocity(M, r)
        a = centripetal_acceleration(v, r)
        T = orbital_period(v, r)

        print("\nResults:")
        print(f"Orbital Velocity: {v:.2f} m/s")
        print(f"Centripetal Acceleration: {a:.2f} m/s²")
        print(f"Orbital Period: {T:.2f} s")

        show_plot = input("\nDo you want to visualize the orbit? (y/n): ").strip().lower()
        if show_plot == "y":
            plot_orbit(r)

    except ValueError:
        print("Invalid input! Please enter numeric values.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
