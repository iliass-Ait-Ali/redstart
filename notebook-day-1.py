import marimo

__generated_with = "0.20.4"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Redstart: A Lightweight Reusable Booster
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.image(src="public/images/redstart.png")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Project Redstart is an attempt to design the control systems of a reusable booster during landing.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In principle, it is similar to SpaceX's Falcon Heavy Booster.

    >The Falcon Heavy booster is the first stage of SpaceX's powerful Falcon Heavy rocket, which consists of three modified Falcon 9 boosters strapped together. These boosters provide the massive thrust needed to lift heavy payloads—like satellites or spacecraft—into orbit. After launch, the two side boosters separate and land back on Earth for reuse, while the center booster either lands on a droneship or is discarded in high-energy missions.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.center(
        mo.Html("""
    <iframe width="560" height="315" src="https://www.youtube.com/embed/RYUr-5PYA7s?si=EXPnjNVnqmJSsIjc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>""")
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Dependencies
    """)
    return


@app.cell
def _():
    import scipy
    import scipy.integrate as sci

    import matplotlib as mpl
    import matplotlib.pyplot as plt

    import numpy as np
    import numpy.linalg as la

    return np, plt, sci


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## The Model

    The Redstart booster in model as a rigid tube of length $\ell$ and negligible diameter whose mass $M$ is uniformly spread along its length. It may be located in 2D space by the coordinates $(x, y)$ of its center of mass and the angle $\theta$ it makes with respect to the vertical (with the convention that $\theta > 0$ for a left tilt, i.e. the angle is measured counterclockwise)

    This booster has an orientable reactor at its base ; the force that it generates is of amplitude $f \geq 0$ and the angle of the force with respect to the booster axis is $\phi$ (with a counterclockwise convention).

    We assume that the booster is subject to gravity, the reactor force and that the friction of the air is negligible.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.center(mo.image(src="public/images/geometry.svg"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Constants

    For the sake of simplicity (this is merely a toy model!) in the sequel we assume that:

    - the total length $\ell$ of the booster is 2 meters,
    - its mass $M$ is 1 kg,
    - the gravity constant $g$ is 10 m/s^2.

    This set of values is completely unrealistic, but very simple! It will simplify our computations and will not fundamentally impact the structure of the booster dynamics.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Getting Started
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Constants

    Define the Python constants `g`, `M` and `l` that correspond to the gravity constant, the mass and half-length of the booster.
    """)
    return


@app.cell
def _():
    # Constants
    g = 10.0
    M = 1.0
    l = 2.0
    return M, g, l


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Forces

    Compute the cartesian coordinates $f_x$ and $f_y$ of the force applied to the booster by the reactor, functions of $f$, $\theta$ and $\phi$.
    """)
    return


@app.cell
def _(np):
    def force_coordinates(f, theta, phi):
        fx = -f * np.sin(theta + phi)
        fy =  f * np.cos(theta + phi)
        return fx, fy

    return (force_coordinates,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Center of Mass

    Give the ordinary differential equation that governs the evolution of the position $(x, y)$ of the center of mass of the booster.
    """)
    return


@app.cell
def _(M, force_coordinates, g):
    def center_of_mass_acceleration(f, theta, phi):
        fx, fy = force_coordinates(f, theta, phi)
        ax = fx / M
        ay = fy / M - g
        return ax, ay

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Moment of inertia

    Compute the [moment of inertia](https://en.wikipedia.org/wiki/Moment_of_inertia) $J$ of the booster and define the corresponding Python variable `J`.
    """)
    return


@app.cell
def _(M, l):
    J = (1/12) * M * l**2 
    return (J,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Tilt

    Give the ordinary differential equation that governs the evolution of the tilt angle $\theta$.
    """)
    return


@app.cell
def _(J, l, np):
    def angular_acceleration(f, phi):
        return -(l / 2) * f * np.sin(phi) / J

    return (angular_acceleration,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Vector Field

    Denote

    - $v_x =\dot{x}$, $v_y = \dot{y}$ the components of the booster center of mass velocity,
    - $\omega = \dot{\theta}$ the angular velocity of the booster.


    What is is dimension $n$ of the state space?
    What is the state $s \in \R^n$ of the booster dynamics?
    Provide the definition of the function $F : \mathbb{R}^{n + 2} \to \mathbb{R}^n$ such that the system evolves
    according to

    $$
    \dot{s} = F(s, f, \phi).
    $$
    """)
    return


@app.cell
def _(M, angular_acceleration, force_coordinates, g, np):
    def F(s, f, phi):
        x, vx, y, vy, theta, omega = s

        fx, fy = force_coordinates(f, theta, phi)

        dx = vx
        dvx = fx / M

        dy = vy
        dvy = fy / M - g

        dtheta = omega
        domega = angular_acceleration(f, phi)  


        return np.array([dx, dvx, dy, dvy, dtheta, domega])

    return (F,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Simulation

    Define a function `redstart_solve` that, given the input parameters:

    - `t_span`: a pair of initial time `t_0` and final time `t_f`,
    - `y0`: the value of `[x, vx, y, vy, theta, omega]` at `t_0`,
    - `f_phi`: a function that given the current time `t` and current state value `y`
         returns the values of the inputs `f` and `phi` in an array.

    returns:

    - `sol`: a function that given a time `t` returns the value of `[x, vx, y, vy, theta, omega]` at time `t` (and that also accepts 1d-arrays of times for multiple state evaluations).

    A typical usage would be:

    ```python
    def free_fall_example():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0] # [x, vx, y, vy, theta, omega]
        def f_phi(t, y):
            return np.array([0.0, 0.0]) # [f, phi]
        sol = redstart_solve(t_span, y0, f_phi)
        t = np.linspace(t_span[0], t_span[1], 1000)
        y_t = sol(t)[2]
        plt.plot(t, y_t, label=r"$y(t)$ (height in meters)")
        plt.plot(t, l * np.ones_like(t), color="grey", ls="--", label=r"$y=\ell$")
        plt.title("Free Fall")
        plt.xlabel("time $t$")
        plt.grid(True)
        plt.legend()
        return plt.gcf()
    free_fall_example()
    ```
    """)
    return


@app.cell
def _(F, sci):
    def redstart_solve(t_span, y0, f_phi):
        def rhs(t, y):
            f, phi = f_phi(t, y)
            return F(y, f, phi)

        result = sci.solve_ivp(
            rhs,
            t_span,
            y0,
            dense_output=True,
        )

        return result.sol

    return (redstart_solve,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Freefall test


    In the `free_fall` example scenario. scenario, at what moment should the center of mass of the booster theoretically cross the
    height of $y = \ell$?

    Check your `redstart_solve` function in this scenario and produce a graph that allows us to check the above answer numerically/visually.
    """)
    return


@app.cell
def _(g, l, np, plt, redstart_solve):
    def free_fall_test():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]

        def f_phi(t, y):
            return np.array([0.0, 0.0])

        sol = redstart_solve(t_span, y0, f_phi)

        t = np.linspace(t_span[0], t_span[1], 1000)
        y_t = sol(t)[2]

        plt.figure()
        plt.plot(t, y_t, label=r"$y(t)$")
        plt.axhline(l, color="grey", linestyle="--", label=r"$y=\ell$")
        t_crossing = np.sqrt(2 * (10 - l) / g)
        plt.axvline(t_crossing, color="grey", linestyle=":")
        plt.xlabel("time $t$")
        plt.ylabel("height $y(t)$")
    
        t_crossing = np.sqrt(2 * (10 - l) / g)  # déjà calculé
        print(f"t* = {t_crossing:.4f} s")        # ← réponse explicite à la question


        plt.title("Free fall test")
        plt.grid(True)
        plt.legend()
        return plt.gcf()

    free_fall_test()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controlled Landing

    Assume that $x$, $\dot{x}$, $\theta$ and $\dot{\theta}$ are null at $t=0$ and that $y(0)= 10$ and $\dot{y}(0) = - 2$.

    Find a time-varying force $f(t)$ which, when applied in the booster axis ($\theta=0$), yields $y(5)=\ell / 2 = 1$ (the booster is at ground level) and $\dot{y}(5)=0$ (the booster is at rest).

    Simulate the corresponding scenario, display graphically the results and check that your solution works as expected.
    """)
    return


@app.cell
def _(M, g):
    def controlled_landing_force(t):
        y_ddot = 0.384 * t - 0.56
        return M * (g + y_ddot)

    return (controlled_landing_force,)


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _(controlled_landing_force, l, np, plt, redstart_solve):
    def controlled_landing():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, -2.0, 0.0, 0.0]

        def f_phi(t, y):
            f = controlled_landing_force(t)
            phi = 0.0
            return np.array([f, phi])

        sol = redstart_solve(t_span, y0, f_phi)

        t = np.linspace(0.0, 5.0, 1000)
        s = sol(t)

        plt.figure()
        plt.plot(t, s[2], label=r"$y(t)$")
        plt.plot(t, s[3], label=r"$\dot{y}(t)$")
        plt.axhline(l / 2, color="grey", linestyle="--", label=r"$y=\ell/2$")
        plt.xlabel("time $t$")
        plt.title("Controlled landing")
        plt.grid(True)
        plt.legend()
    


    

        print("y(5) =", sol(5.0)[2])
        print("vy(5) =", sol(5.0)[3])

        y5 = sol(5.0)[2]
        vy5 = sol(5.0)[3]

        print("y(5) =", round(y5, 10))
        print("vy(5) =", round(vy5, 10))

        return plt.gcf()

    controlled_landing()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Animations

    It's very handy to visualize the evolution of our booster "as a movie"!

    Have a look at the [animations tutorial] to understand the basics of animated SVG documents.

    [animations tutorial]: http://localhost:2718/?file=animations.py
    """)
    return


@app.cell
def _():
    from svg import svg, transform, animate_transform

    return (svg,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Environment

    Create a function `world` whose arguments are:

    - `view_box`: a view box in cartesian coordinates `[x_min, x_max, y_min, y_max]`,

    - `*objects`: (optional) list of extra svg elements (default : `[]`).

    and that returns a SVG string which

    - has the appropriate cartesian view box and frame ($y$-axis upwards),

    - depicts the sky and the ground,

    - depicts a 2 meter wide green ground target centered on $(0, 0)$,

    - displays the objects (if any) inserted on top of the world.

    Test your function with the following scenes:

    ```python
    mo.hstack(
        [
            # Display an empty world
            mo.Html(
                world([-3, 3, -2, 4])
            ),
            # Display a world with a black square on top of the landing pad
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    svg.rect(x=-1, y=0, width=2, height=2, fill="black"),
                )
            ),
            # Display a world with a red square in the top-left corner of the view box
            # and a blue square on the top-right corner of the view box.
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    svg.rect(x=-3, y=2, width=2, height=2, fill="red"),
                    svg.rect(x=1, y=2, width=2, height=2, fill="blue"),
                )
            )
        ],
        justify="space-around"
    )
    ```
    """)
    return


@app.function
def world(view_box, *objects):
    x_min, x_max, y_min, y_max = view_box
    width = x_max - x_min
    height = y_max - y_min

    objects_str = "\n".join(str(obj) for obj in objects)

    return f"""
    <svg viewBox="{x_min} {-y_max} {width} {height}"
         xmlns="http://www.w3.org/2000/svg"
         width="500">

      <g transform="scale(1,-1)">

        <!-- sky -->
        <rect x="{x_min}" y="0"
              width="{width}" height="{y_max}"
              fill="#dceeff"/>

        <!-- ground -->
        <rect x="{x_min}" y="{y_min}"
              width="{width}" height="{-y_min}"
              fill="#b68b59"/>

        <!-- landing pad: 2 meters wide, centered on (0,0) -->
        <rect x="-1" y="-0.08"
              width="2" height="0.16"
              fill="green"/>

        <!-- axes / horizon -->
        <line x1="{x_min}" y1="0" x2="{x_max}" y2="0"
              stroke="black" stroke-width="0.02"/>

        {objects_str}

      </g>
    </svg>
    """


@app.cell
def _(mo, svg):
    mo.hstack(
        [
            mo.Html(world([-3, 3, -2, 4])),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    svg.rect(x=-1, y=0, width=2, height=2, fill="black"),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    svg.rect(x=-3, y=2, width=2, height=2, fill="red"),
                    svg.rect(x=1, y=2, width=2, height=2, fill="blue"),
                )
            ),
        ],
        justify="space-around",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Booster Drawing

    Create a `booster` function that:

    - takes the numeric arguments `x`, `y`, `theta` (in radians), `f` and `phi` (in radians)

    and returns

    - a SVG fragment that represents the body of the booster and the flame of its reactor.
    (The booster drawing can be very simple, for example a rectangle for the body and another one of a different color for the flame will be fine.)

    **Constraint:** make sure that

    - the orientation of the flame is correct,
    - its length is proportional to the force $f$,
    - the flame length is equal to $\ell/2$ when $f=Mg$.


    Test you function in the following scenarios:

    ```python
    mo.hstack(
        [
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l/2, 0, 0, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l, 0, M * g, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(-l/2, l, np.pi / 4, 2 * M * g, np.pi / 2),
                )
            ),
        ],
        justify="space-around",
    )
    ```
    """)
    return


@app.cell
def _(M, g, l, np, svg):
    def point_to_string(p):
        return f"{p[0]},{p[1]}"


    def points_to_string(points):
        return " ".join(point_to_string(p) for p in points)


    def rotate_booster_point(x, y, theta, X, Y):
        """
        Local coordinates:
        - Y is along the booster axis.
        - X is perpendicular to the booster axis.
        theta > 0 means left tilt.
        """
        ex = np.array([np.cos(theta), np.sin(theta)])
        ey = np.array([-np.sin(theta), np.cos(theta)])
        return np.array([x, y]) + X * ex + Y * ey


    def booster(x, y, theta, f, phi):
        body_width = 0.25

        # Body rectangle in local coordinates
        body_local = [
            [-body_width / 2, -l / 2],
            [ body_width / 2, -l / 2],
            [ body_width / 2,  l / 2],
            [-body_width / 2,  l / 2],
        ]

        body_points = [
            rotate_booster_point(x, y, theta, X, Y)
            for X, Y in body_local
        ]

        # Flame length: equal to l/2 when f = M*g
        if M * g == 0:
            flame_length = 0.0
        else:
            flame_length = (l / 2) * max(f, 0) / (M * g)

        # Base of the booster
        base_center = rotate_booster_point(x, y, theta, 0.0, -l / 2)
        base_left = rotate_booster_point(x, y, theta, -body_width / 3, -l / 2)
        base_right = rotate_booster_point(x, y, theta, body_width / 3, -l / 2)

        # Flame is opposite to the reactor force
        # Force direction: (-sin(theta + phi), cos(theta + phi))
        # Flame direction: opposite
        flame_direction = np.array([
            np.sin(theta + phi),
            -np.cos(theta + phi),
        ])

        flame_tip = base_center + flame_length * flame_direction

        flame_points = [
            base_left,
            base_right,
            flame_tip,
        ]

        body_svg = svg.polygon(
            points=points_to_string(body_points),
            fill="white",
            stroke="black",
            stroke_width=0.04,
        )

        flame_svg = svg.polygon(
            points=points_to_string(flame_points),
            fill="orange",
            stroke="red",
            stroke_width=0.02,
            fill_opacity=0.8,
        )

        return svg.g()(flame_svg, body_svg)

    return booster, points_to_string, rotate_booster_point


@app.cell
def _(M, booster, g, l, mo, np):
    mo.hstack(
        [
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l / 2, 0, 0, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l, 0, M * g, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(-l / 2, l, np.pi / 4, 2 * M * g, np.pi / 2),
                )
            ),
        ],
        justify="space-around",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Booster Animation

    Create a `booster_anim` function whose arguments are:

    - `x`, `y`, `theta` (in radians), `f` and `phi` (in radians)
    **which are functions of a time `t`**.
    - an animation duration `T`,

    and returns

    - a SVG fragment that represents the animated body of the booster and the flame of its reactor during `T` seconds, then repeats.
    (The booster drawing can be very simple, for example a rectangle for the body and another one of a different color for the flame will be fine.)

    **Constraint:** make sure that

    - the orientation of the flame is correct,
    - its length is proportional to the force $f$,
    - the flame length is equal to $\ell/2$ when $f=Mg$.

    Test your function in the following scenario:

    ```python
    def booster_anim_0():
        T = 5.0
        def x(t):
            return -l/2 + l * (t / T)
        def y(t):
            return l/2 + l/2 * (t / T)
        def theta(t):
            return (t / T) * 2 * np.pi
        def f(t):
            return M * g * (t / T)
        def phi(t):
            return 2 * np.pi * (t / T)
        return booster_anim(x, y, theta, f, phi, T=T)

    mo.Html(
        world([-3, 3, -2, 4], booster_anim_0())
    ).center()
    ```
    """)
    return


@app.cell
def _(M, g, l, np, points_to_string, rotate_booster_point):
    def booster_points(x, y, theta, f, phi):
        body_width = 0.25

        body_local = [
            [-body_width / 2, -l / 2],
            [ body_width / 2, -l / 2],
            [ body_width / 2,  l / 2],
            [-body_width / 2,  l / 2],
        ]

        body_points = [
            rotate_booster_point(x, y, theta, X, Y)
            for X, Y in body_local
        ]

        flame_length = (l / 2) * max(f, 0) / (M * g)

        base_center = rotate_booster_point(x, y, theta, 0.0, -l / 2)
        base_left = rotate_booster_point(x, y, theta, -body_width / 3, -l / 2)
        base_right = rotate_booster_point(x, y, theta, body_width / 3, -l / 2)

        flame_direction = np.array([
            np.sin(theta + phi),
            -np.cos(theta + phi),
        ])

        flame_tip = base_center + flame_length * flame_direction

        flame_points = [
            base_left,
            base_right,
            flame_tip,
        ]

        return body_points, flame_points


    def booster_anim(x, y, theta, f, phi, T=5.0, fps=20.0):
        dt = 1.0 / fps
        ts = np.arange(0.0, T + dt, dt)

        key_times = "; ".join(str(t / T) for t in ts)

        body_values = []
        flame_values = []

        for t in ts:
            body_points, flame_points = booster_points(
                x(t),
                y(t),
                theta(t),
                f(t),
                phi(t),
            )

            body_values.append(points_to_string(body_points))
            flame_values.append(points_to_string(flame_points))

        body_values = "; ".join(body_values)
        flame_values = "; ".join(flame_values)

        body_points_0, flame_points_0 = booster_points(
            x(0.0),
            y(0.0),
            theta(0.0),
            f(0.0),
            phi(0.0),
        )

        return f"""
        <g>
          <polygon points="{points_to_string(flame_points_0)}"
                   fill="orange"
                   stroke="red"
                   stroke-width="0.02"
                   fill-opacity="0.8">
            <animate attributeName="points"
                     keyTimes="{key_times}"
                     values="{flame_values}"
                     dur="{T}s"
                     repeatCount="indefinite"/>
          </polygon>

          <polygon points="{points_to_string(body_points_0)}"
                   fill="white"
                   stroke="black"
                   stroke-width="0.04">
            <animate attributeName="points"
                     keyTimes="{key_times}"
                     values="{body_values}"
                     dur="{T}s"
                     repeatCount="indefinite"/>
          </polygon>
        </g>
        """

    return (booster_anim,)


@app.cell
def _(M, booster_anim, g, l, mo, np):
    def booster_anim_0():
        T = 5.0

        def x(t):
            return -l / 2 + l * (t / T)

        def y(t):
            return l / 2 + l / 2 * (t / T)

        def theta(t):
            return (t / T) * 2 * np.pi

        def f(t):
            return M * g * (t / T)

        def phi(t):
            return 2 * np.pi * (t / T)

        return booster_anim(x, y, theta, f, phi, T=T)


    mo.Html(
        world([-3, 3, -2, 4], booster_anim_0())
    ).center()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Animated Simulation Results

    Let's go back to a booster whose evolution is governed by its system of ordinary differentential equations. Produce a animation of the booster for 5 seconds for each of the following initial value problems:

    1. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=0$ and $\phi=0$

    2. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=Mg$ and $\phi=0$

    3. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=Mg$ and $\phi=\pi/8$

    4. The "controlled landing" scenario (see above).
    """)
    return


@app.cell
def _(booster_anim, mo, redstart_solve):
    def animated_simulation(y0, f_phi, T=5.0, view_box=[-5, 5, -2, 12]):
        sol = redstart_solve([0.0, T], y0, f_phi)

        def x(t):
            return sol(t)[0]

        def y(t):
            return sol(t)[2]

        def theta(t):
            return sol(t)[4]

        def f(t):
            state = sol(t)
            return f_phi(t, state)[0]

        def phi(t):
            state = sol(t)
            return f_phi(t, state)[1]

        return mo.Html(
            world(
                view_box,
                booster_anim(x, y, theta, f, phi, T=T),
            )
        ).center()

    return (animated_simulation,)


@app.cell
def _(animated_simulation, np):
    def anim_free_fall():
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]

        def f_phi(t, y):
            return np.array([0.0, 0.0])

        return animated_simulation(y0, f_phi, T=5.0)


    anim_free_fall()
    return


@app.cell
def _(M, animated_simulation, g, np):
    def anim_hover():
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]

        def f_phi(t, y):
            return np.array([M * g, 0.0])

        return animated_simulation(y0, f_phi, T=5.0)


    anim_hover()
    return


@app.cell
def _(M, animated_simulation, g, np):
    def anim_tilted_thrust():
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]

        def f_phi(t, y):
            return np.array([M * g, np.pi / 8])

        return animated_simulation(y0, f_phi, T=5.0, view_box=[-8, 8, -2, 12])


    anim_tilted_thrust()
    return


@app.cell
def _(animated_simulation, controlled_landing_force, np):
    def anim_controlled_landing():
        y0 = [0.0, 0.0, 10.0, -2.0, 0.0, 0.0]

        def f_phi(t, y):
            f = controlled_landing_force(t)
            phi = 0.0
            return np.array([f, phi])

        return animated_simulation(y0, f_phi, T=5.0, view_box=[-3, 3, -2, 12])


    anim_controlled_landing()
    return


if __name__ == "__main__":
    app.run()
