#### Description:

The **Orbital Motion Calculator** is a Python program that models the motion of an object orbiting around a central body, such as a planet around a star or a satellite around Earth. The program uses basic principles of physics — Newton’s law of universal gravitation and circular motion — to calculate key orbital parameters such as orbital velocity, centripetal acceleration, and orbital period. It can also visualize the orbit using a 2D plot.

This project was created as part of the final requirement for **CS50’s Introduction to Programming with Python (CS50P)**. It represents my understanding of functions, mathematical operations, exception handling, modular design, user interaction, and data visualization.

---

### Features and Functionality

The program begins by prompting the user to enter:
- The mass of the central body (in kilograms).
- The orbital radius (in meters).

From these two inputs, the program performs several computations:
1. **Orbital Velocity** – calculated using the formula
   \[
   v = \sqrt{\frac{GM}{r}}
   \]
   where \( G = 6.674 \times 10^{-11} \) is the gravitational constant.

2. **Centripetal Acceleration** – calculated using
   \[
   a = \frac{v^2}{r}
   \]

3. **Orbital Period** – calculated using
   \[
   T = \frac{2 \pi r}{v}
   \]

Once the calculations are complete, the results are displayed with two decimal points of precision.
The user is then given an option to visualize the orbit. If the user enters “y”, the program generates a circular orbit using **matplotlib**, showing the path of the orbiting object and the position of the central body.

---

### Project Structure

- **project.py**
  Contains the main program logic and all function definitions.
  It includes the following top-level functions:
  - `orbital_velocity(M, r)` – calculates the orbital velocity.
  - `centripetal_acceleration(v, r)` – calculates centripetal acceleration.
  - `orbital_period(v, r)` – computes the time it takes for one complete orbit.
  - `plot_orbit(r)` – uses matplotlib to visualize the orbital path.
  - `main()` – handles user interaction, input validation, and calls other functions.

- **test_project.py**
  Contains automated tests written using `pytest`.
  Each major function (`orbital_velocity`, `centripetal_acceleration`, and `orbital_period`) has its own corresponding test function to verify correctness using known values and physical relationships.

- **requirements.txt**
  Lists the dependencies required to run the project. In this case, the only external library is `matplotlib`.

---

### Design Choices

I chose to design the project in a modular way — every physical formula is implemented as a separate function. This makes the code easier to test, maintain, and extend. For example, additional features such as elliptical orbits or multi-body simulations could be added in the future.

I also used exception handling (`try/except`) to manage invalid user input gracefully.
The visualization part (`plot_orbit`) adds an interactive element and makes the program more engaging and educational.

---

### How to Run

1. Make sure Python 3 and pip are installed.
2. Install dependencies by running:
