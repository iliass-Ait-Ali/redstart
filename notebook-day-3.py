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

    return la, np, plt, sci, scipy


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
    - the gravity constant $g$ is 1 m/s^2.

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

    Define the Python constants `g`, `M` and `l` that correspond to the gravity constant, the mass and length of the booster.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _():
    g = 1.0
    M = 1.0
    l = 2
    return M, g, l


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Forces

    Compute the cartesian coordinates $f_x$ and $f_y$ of the force applied to the booster by the reactor, as functions of $f$, $\theta$ and $\phi$.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Given the geometric setting, the cartesian coordinates of the unit vector $\vec{u}=(u_x, u_y)$ aligned with the reactor (or flame) axis and pointing from the reactor towards the flame satisfy:

    \begin{align*}
    u_x & = +\sin (\theta + \phi) \\
    u_y & = -\cos(\theta +\phi)
    \end{align*}

    Assuming that $f \geq 0$, the force applied to the booster is in the opposite direction and has amplitude $f$:

    $$
    \vec{f} = -f \vec{u}
    $$

    Therefore,

    \begin{align*}
    f_x & = -f \sin (\theta + \phi) \\
    f_y & = +f \cos(\theta +\phi)
    \end{align*}
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Center of Mass

    Give the ordinary differential equation that governs the evolution of the position $(x, y)$ of the center of mass of the booster.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The force exerted by the gravity on the booster is

    $$
    \vec{f}_g =
    \begin{bmatrix}
    0 \\ - M g
    \end{bmatrix}
    $$

    By Newton's second law of motion, the acceleration $\vec{a} = (\ddot{x}, \ddot{y})$
    satisfies $M \vec{a} = \vec{f} + \vec{f}_g$ and thus

    \begin{align*}
    M \ddot{x} & = -f \sin (\theta + \phi) \\
    M \ddot{y} & = +f \cos(\theta +\phi) - Mg
    \end{align*}
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Moment of inertia

    Compute the [moment of inertia](https://en.wikipedia.org/wiki/Moment_of_inertia) $J$ of the booster and define the corresponding Python variable `J`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    The moment of inertia of a thin rod with uniformly distributed mass about its center is of mass is

    $$
    J = \frac{1}{12} M \ell^2
    $$
    """)
    return


@app.cell
def _(M, l):
    J = M * l ** 2 / 12
    J
    return (J,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Tilt

    Give the ordinary differential equation that governs the evolution of the tilt angle $\theta$.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    Newton's Second Law for Rotation is $J \ddot{\theta} = \tau$ where $\tau$ is the torque applied to the booster. Here the torque applied by the gravity to the booster is $0$ by symmetry and only the booster reactor induces a torque. The torque can be
    first computed as a vector in 3D as the cross-product of the vector between the center of the booster and the reactor location and the force applied by the reactor.
    Afterwards, we can be project it on the 3rd axis to get $\tau$.

    Thus, we have

    $$
    \tau =
    \left(
    \ell / 2
    \begin{bmatrix}
    {} +\sin \theta \\ - \cos \theta \\ 0
    \end{bmatrix}
    \wedge \begin{bmatrix} -f \sin (\theta + \phi) \\ +f \cos (\theta + \phi) \\ 0
    \end{bmatrix}
    \right)
    \cdot \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}
    =
    \ell/2 (f\sin \theta \cos (\theta + \phi) - f\sin (\theta + \phi) \cos \theta).
    $$

    Since $\sin \alpha \cos \beta - \sin \beta \cos \alpha = \sin (\alpha - \beta)$,
    we obtain

    $$
    \tau = - f (\ell/2) \sin \phi,
    $$

    thus the angular acceleration is governed by

    $$
    J \ddot{\theta} = - f (\ell / 2)  \sin \phi.
    $$
    """)
    return


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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    Given that

    \begin{align*}
    M \ddot{x} & = -f \sin (\theta + \phi) \\
    M \ddot{y} & = +f \cos(\theta +\phi) - Mg \\
    J \ddot{\theta} & = - f (\ell/2) \sin \phi
    \end{align*}

    and $\dot{x} = v_x$, $\dot{y} = v_y$ and $\dot{\theta} = \omega$, we
    can use as a state vector $s = (x, v_x, y, v_y, \theta, \omega) \in \mathbb{R}^6$
    and the corresponding function $F$ is given by

    $$
    F(s, f, \phi) = \begin{bmatrix}
    v_x \\ -(f / M) \sin (\theta + \phi) \\
    v_y \\ +(f / M) \cos(\theta +\phi) - g \\
    \omega \\ - (f / J) (\ell/2) \sin \phi
    \end{bmatrix}
    $$
    """)
    return


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


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(J, M, g, l, np, scipy):
    def redstart_solve(t_span, y0, f_phi):
        def fun(t, state):
            x, vx, y, vy, theta, omega = state
            f, phi = f_phi(t, state)
            d2x = (-f * np.sin(theta + phi)) / M
            d2y = (+ f * np.cos(theta + phi)) / M - g
            d2theta = - (f / J) * (l / 2) * np.sin(phi)
            return np.array([vx, d2x, vy, d2y, omega, d2theta])
        r = scipy.integrate.solve_ivp(fun, t_span, y0, dense_output=True)
        return r.sol

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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    In the free fall scenario, the solution satisfies $x(t)=0$, $y(t) = y(0) - g/2 t^2$ and $\theta(t) = 0$. Since numerically $y(0)=10.0$, $g=1$ and $\ell=2$, the threshold
    is crossed when $10 - 1/2 t^2 = 2$, that is $t=4$.
    """)
    return


@app.cell(hide_code=True)
def _(l, np, plt, redstart_solve):
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


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can search for a cubic polynomial

    $$
    y(t) = a_3 t^3 + a_2 t^2 + a_1 t + a_0
    $$

    that solves the four given constraints,
    then deduce $f(t)$ from the equation $M \ddot{y} = f + Mg$.

    The time derivative of $y$ satisfies
    $$
    \dot{y}(t) = 3 a_3 t^2 + 2 a_2 t + a_1,
    $$
    thus the constraints are:

    \begin{align*}
    y(0) = a_0 &= 10, \\
    \dot{y}(0) = a_1 &= -2,\\
    y(5) = 125 a_3 + 25 a_2 + 5 a_1 + a_0 &= 1, \\
    \dot{y}(5) = 75 a_3 + 10 a_2 + a_1 &= 0. \\
    \end{align*}

    The solution of this linear system provides:

    $$
    y(t)
    =\frac{8}{125}t^3 - \frac{7}{25} t^2 - 2t + 10,
    $$
    which yields
    $$
    \ddot{y}(t)
    =
    \frac{48}{125}t - \frac{14}{25}
    $$
    and therefore since $M=1$ and $g=1$,
    $$
    f(t) = \frac{\ddot{y}(t)}{M} + g = \frac{48}{125}t + \frac{11}{25}.
    $$
    """)
    return


@app.cell(hide_code=True)
def _(l, np, plt, redstart_solve):
    def controlled_landing_example():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, -2.0, 0.0, 0.0]
        def f_phi_smooth_landing(t, state):
            return np.array([48 / 125 * t + 11 / 25, 0])
        sol = redstart_solve(t_span, y0, f_phi=f_phi_smooth_landing)
        t = np.linspace(t_span[0], t_span[1], 1000)
        y_t = sol(t)[2]
        plt.plot(t, y_t, label=r"$y(t)$ (height in meters)")
        plt.plot(t, (l / 2) * np.ones_like(t), color="grey", ls="--", label=r"$y=\ell/2$")
        plt.title("Controlled Landing")
        plt.xlabel("time $t$")
        plt.grid(True)
        plt.legend()
        return plt.gcf()
    controlled_landing_example()
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

    return animate_transform, svg, transform


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


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(svg, transform):
    def world(view_box, *objects):
        x_min, x_max, y_min, y_max = view_box    
        width, height = x_max - x_min, y_max - y_min

        return svg.svg(
          xmlns="http://www.w3.org/2000/svg",
          viewBox=f"0 0 {width} {height}",
          style="max-height:80vh")(
              transform.translate(x=-x_min, y=y_max)(
                  transform.scale(y=-1.0)(
                      # Sky
                      svg.rect(x=-1e3, y=0, width=2e3, height=1e3, fill="lightskyblue"),
                      # Ground
                      svg.rect(x=-1e3, y=-2e3, width=2e3, height=2e3, fill="sandybrown"),
                      # Target 
                      svg.rect(x=-1, y =-1, width=2, height=1, fill="lightgreen"),
                      *objects,
                )
            )
        )

    return (world,)


@app.cell
def _(mo, svg, world):
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


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(M, g, l, np, svg, transform):
    def booster(x, y, theta, f, phi):
        flame_length = (l / 2) * (f / M / g)
        return transform.translate(x, y)(
            transform.rotate(theta / np.pi * 180.0)(
                svg.rect(x=-l/20, y=-l/2, width=l/10, height=l, fill="black"),
                transform.translate(0, -l / 2)(
                    transform.rotate(phi / np.pi * 180)(
                        svg.rect(
                            x=-l/20,
                            y=-flame_length,
                            width=l/10,
                            height=flame_length,
                            fill="red",
                        )
                    )
                )
            )
        )

    return (booster,)


@app.cell(hide_code=True)
def _(M, booster, g, l, mo, np, world):
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


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(M, animate_transform, g, l, np, svg):
    def booster_anim(x, y, theta, f, phi, T):
        if not callable(theta):
            theta_cst = theta
            theta = lambda t: theta_cst
        if not callable(phi):
            phi_cst = phi
            phi = lambda t: phi_cst

        def theta_deg(t):
            return theta(t) / np.pi * 180.0

        def phi_deg(t):
            return phi(t) / np.pi * 180.0

        return animate_transform.translate(x, y, T=T)(
            animate_transform.rotate(theta_deg, T=T)(
                svg.rect(
                    x=-l / 20,
                    y=-l/2,
                    width=l / 10,
                    height=l,
                    fill="black",
                ),
                animate_transform.translate(y=-l/2, T=T)(
                    animate_transform.rotate(phi_deg, T=T)(
                        animate_transform.scale(y=f, T=T)(
                            svg.rect(
                                x=-l/20,
                                y=-1/M/g,
                                width=l / 10,
                                height=1/M/g,
                                fill="red",
                            )
                        )
                    )
                ),
            )
        )

    return (booster_anim,)


@app.cell
def _(M, booster_anim, g, l, np):
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

    return (booster_anim_0,)


@app.cell
def _(booster_anim_0, mo, world):
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


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(booster_anim, mo, np, redstart_solve, world):
    def anim_1():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0] 
        def f_phi(t, state):
            return np.array([0, 0])
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[0]
        return mo.Html(
            world(
                [-3, 3, -2, 12], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    anim_1()
    return


@app.cell
def _(M, booster_anim, g, mo, np, redstart_solve, world):
    def anim_2():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]
        def f_phi(t, state):
            return np.array([M * g, 0])
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[1]
        return mo.Html(
            world(
                [-3, 3, -2, 12], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    anim_2()
    return


@app.cell
def _(M, booster_anim, g, mo, np, redstart_solve, world):
    def anim_3():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]
        def f_phi(t, state):
            return np.array([M * g, np.pi / 8])
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[1]
        return mo.Html(
            world(
                [-3, 3, -2, 12], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    anim_3()
    return


@app.cell
def _(booster_anim, mo, np, redstart_solve, world):
    def anim_4():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, -2.0, 0.0, 0.0]
        def f_phi(t, state):
            return np.array([48 / 125 * t + 11 / 25, 0])
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[1]
        return mo.Html(
            world(
                [-3, 3, -2, 12], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    anim_4()
    return


@app.cell
def _(mo):
    mo.md(r"""
    # Linearized Dynamics
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Equilibria

    We assume that

    - $|\theta| < \pi/2$,
    - $|\phi| < \pi/2$, and
    - $f > 0$.

    What are the possible equilibria of the system for constant inputs $f$ and $\phi$ and what are the corresponding values of these inputs?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Our state is $s = (x, v_x, y, v_y,\theta, \omega)$ and the system is governed by
    $\dot{s} = F(s, f, \phi)$ with
    $$
    F(s, f, \phi) = \begin{bmatrix}
    v_x \\ -(f / M) \sin (\theta + \phi) \\
    v_y \\ +(f / M) \cos(\theta +\phi) - g \\
    \omega \\ - (f / J) (\ell/2) \sin \phi
    \end{bmatrix}
    $$
    The equilibria are characterized by $F(s, f, \phi) = 0$. We obtain directly that
    $v_x = v_y = 0$ and $\omega = 0$. We also extract the two equations

    $$
    \begin{bmatrix}
    -(f / M) \sin (\theta + \phi) \\
    +(f / M) \cos(\theta +\phi)
    \end{bmatrix}
    =
    \begin{bmatrix}
    0 \\
    g
    \end{bmatrix}
    $$
    which holds if when $|\theta| < \pi/2$ and $|\phi| < \pi/2$ and only if
    $\theta = \phi = 0$ and $f = M g$. The final equation is then satisfied if and only if
    $\omega = 0$. Finally, we obtain the equilibria as:
    $$
    \begin{bmatrix}
    x \\
    v_x \\
    y \\
    v_y \\
    \theta \\
    \omega \\
    f \\
    \phi
    \end{bmatrix}
    =
    \begin{bmatrix}
    ? \\
    0 \\
    ? \\
    0 \\
    0 \\
    0 \\
    M g \\
    0
    \end{bmatrix}
    $$
    where $?$ stands for "any possible value".
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Linearized Model

    Introduce the error variables $\Delta x$, $\Delta y$, $\Delta \theta$, and $\Delta f$ and $\Delta \phi$ of the state and input values with respect to the generic equilibrium configuration.
    What are the linear ordinary differential equations that govern (approximately) these variables in a neighbourhood of the equilibrium?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We have $\Delta \theta = \theta$, $\Delta \phi = \phi$ and $\Delta f = f - M g$. Given that

    \begin{align*}
    M \ddot{x} & = -f \sin (\theta + \phi) \\
    M \ddot{y} & = +f \cos(\theta +\phi) - Mg \\
    J \ddot{\theta} & = - f (\ell/2) \sin \phi
    \end{align*}

    and that for small values of $\alpha$, $\sin \alpha \approx \alpha$ and $\cos \alpha \approx 1$, we obtain:

    \begin{align*}
    M (d/dt)^2 \Delta x &= - Mg (\Delta \theta + \Delta \phi)  \\
    M (d/dt)^2 \Delta y &= \Delta f \\
    J (d/dt)^2 \Delta \theta &= - (Mg \ell /2) \Delta \phi \\
    \end{align*}
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Standard Form

    1. What are the matrices $A$ and $B$ associated to this linear model in standard form?
    2. Define the corresponding NumPy arrays `A` and `B`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Note: remember that $J = (1/12) M \ell^2$.

    $$
    A =
    \begin{bmatrix}
    0 & 1 & 0 & 0 & 0  & 0 \\
    0 & 0 & 0 & 0 & -g & 0 \\
    0 & 0 & 0 & 1 & 0  & 0 \\
    0 & 0 & 0 & 0 & 0  & 0 \\
    0 & 0 & 0 & 0 & 0  & 1 \\
    0 & 0 & 0 & 0 & 0  & 0
    \end{bmatrix}
    \;\;\;
    B =
    \begin{bmatrix}
    0 & 0\\
    0 & -g\\
    0 & 0\\
    1/M & 0\\
    0 & 0 \\
    0 & -M g \ell/(2J)\\
    \end{bmatrix}
    =
    \begin{bmatrix}
    0 & 0\\
    0 & -g\\
    0 & 0\\
    1/M & 0\\
    0 & 0 \\
    0 & - 6 g / \ell\\
    \end{bmatrix}
    $$
    """)
    return


@app.cell(hide_code=True)
def _(g, np):
    A = np.zeros((6, 6))
    A[0, 1] = 1.0
    A[1, 4] = -g
    A[2, 3] = 1.0
    A[4, -1] = 1.0
    A
    return (A,)


@app.cell(hide_code=True)
def _(M, g, l, np):
    B = np.zeros((6, 2))
    B[ 1, 1]  = -g 
    B[ 3, 0]  = 1/M
    B[-1, 1] = -6 * g / l
    B
    return (B,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Stability

    Is the generic equilibrium asymptotically stable?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    No, since $0$ is the only eigenvalue of $A$ and $0$ doesn't have a negative real part.
    """)
    return


@app.cell(hide_code=True)
def _(A, la):
    eigenvalues, eigenvectors = la.eig(A)
    print(f"Eigenvalues of A: {eigenvalues}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controllability

    Is the linearized model controllable?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    The controllability matrix of the system is:
    """)
    return


@app.cell(hide_code=True)
def _(A, B, np):
    # Controllability
    cs = np.column_stack
    mp = np.linalg.matrix_power
    KC = cs([mp(A, k) @ B for k in range(6)])
    KC
    return (KC,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    and its rank is
    """)
    return


@app.cell(hide_code=True)
def _(KC, np):
    int(np.linalg.matrix_rank(KC))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    which is equal to the state dimension, so the answer is yes, it's controllable.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Lateral Dynamics

    We limit our interest in the lateral position $x$, the tilt $\theta$ and their derivatives (we are for the moment fine with letting $y$ and $\dot{y}$ be uncontrolled). We also set $f = M g$ and control the system only with $\phi$.

    - What are the new (reduced) matrices $A$ and $B$ for this reduced system?

    - Check the controllability of this new system.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(g, l, np):
    A_lat = np.array([
        [0, 1, 0, 0], 
        [0, 0, -g, 0], 
        [0, 0, 0, 1], 
        [0, 0, 0, 0]], dtype=np.float64)
    B_lat = np.array([[0, -g, 0, - 6 * g / l]]).T

    print("A_lat:")
    print(A_lat)
    print("B_lat:")
    print(B_lat)
    return A_lat, B_lat


@app.cell(hide_code=True)
def _(A_lat, B_lat, np):
    # Controllability
    _cs = np.column_stack
    _mp = np.linalg.matrix_power
    KC_lat = _cs([_mp(A_lat, k) @ B_lat for k in range(6)])
    KC_lat
    return (KC_lat,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This reduced system of dimension 4 is controllable since the rank of its controllability matrix is 4:
    """)
    return


@app.cell(hide_code=True)
def _(KC_lat, np):
    np.linalg.matrix_rank(KC_lat)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Linear Model in Free Fall

    Make graphs of $x(t)$ and $\theta(t)$ for the linearized model when
    - $x(0)=0$, $\dot{x}(0)=0$, $\theta(0) = \pi/4$, $\dot{\theta}(0) =0$, and
    - $\phi(t)=0$ at all times.

    What do you see? How do you explain it?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(g, l, np):
    def make_fun_lat(phi):
        def fun_lat(t, state):
            x, dx, theta, dtheta = state
            phi_ = phi(t, state)
            d2x = -g * (theta + phi_)
            d2theta = - 6 * g / l * phi_
            return np.array([dx, d2x, dtheta, d2theta])

        return fun_lat

    return (make_fun_lat,)


@app.cell(hide_code=True)
def _(make_fun_lat, mo, np, plt, sci):
    def lin_sim_1():
        def phi(t, state):
            return 0.0

        f_lat = make_fun_lat(phi)
        t_span = [0, 10]
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]
        r = sci.solve_ivp(
            fun=f_lat, y0=state_0, t_span=t_span, dense_output=True
        )
        t = np.linspace(t_span[0], t_span[1], 1000)
        sol_t = r.sol(t)
        fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
        ax1.plot(t, sol_t[0], label=r"$x(t)$")
        ax1.grid(True)
        ax1.legend()
        ax2.plot(t, sol_t[2], label=r"$\theta(t)$")
        ax2.grid(True)
        ax2.set_xlabel(r"time $t$")
        ax2.legend()
        return mo.center(fig)


    lin_sim_1()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    - Since the reactor pushes (with a constant force) in the axis of the booster ($\phi=0$) and the initial title velocity $\omega = \dot{\theta}$ is zero, it's sensible that the title $\theta$ stays constant. That explains the second graph.
    - On the other hand, the constant projected force on the $x$-axis drives a constant acceleration which is towards the left since the initial tilt is positive. That explain the first graph.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Manually Tuned Controller

    Try to find the two missing coefficients of the matrix

    $$
    K =
    \begin{bmatrix}
    0 & 0 & ? & ?
    \end{bmatrix}
    \in \mathbb{R}^{4\times 1}
    $$

    such that the control law

    $$
    \Delta \phi(t) = - K \cdot
    \begin{bmatrix}
    \Delta x(t) \\
    \Delta \dot{x}(t) \\
    \Delta \theta(t) \\
    \Delta \dot{\theta}(t)
    \end{bmatrix} \in \mathbb{R}
    $$

    manages  when
    $\Delta x(0)=0$, $\Delta \dot{x}(0)=0$, $\Delta \theta(0) = 45 / 180  \times \pi$  and $\Delta \dot{\theta}(0) =0$ to:

    - make $\Delta \theta(t) \to 0$ in approximately $20$ sec (or less),
    - $|\Delta \theta(t)| < \pi/2$ and $|\Delta \phi(t)| < \pi/2$ at all times,
    - (but we don't care about a possible drift of $\Delta x(t)$).

    Explain your thought process, show your iterative guesses and simulations!

    Is your final closed-loop model asymptotically stable?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We try first a controller that corrects using only $\Delta \theta$ since it it's the simples think we can think of (a controller based only on the derivative would not achieve $\Delta \theta(t) \to 0$ since it would only knows $\Delta \theta(t)$ up to a constant). When $\Delta \theta > 0$, we want the reactor to be oriented on the right ($\Delta \phi > 0$) to compensate for this trend.

    Hence it makes sens to start for something simple such as
    $\Delta \phi =  \Delta \theta$, which corresponds to

    $$
    K =
    \begin{bmatrix}
    0 & 0 & -1 & 0
    \end{bmatrix}
    \in \mathbb{R}^{4\times 1}
    $$

    and

    $$
    \Delta \phi(t) = - K \cdot
    \begin{bmatrix}
    \Delta x(t) \\
    \Delta \dot{x}(t) \\
    \Delta \theta(t) \\
    \Delta \dot{\theta}(t)
    \end{bmatrix} \in \mathbb{R}
    $$

    Let's make a simulation out of this!
    """)
    return


@app.cell
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci):
    def lin_sim_k1():

        K = np.array([0.0, 0.0, -1.0, 0.0])

        print(
            "eigenvalues:",
            np.linalg.eig(
                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))
            ).eigenvalues,
        )

        t_span = [0, 20.0]
        t = np.linspace(t_span[0], t_span[1], 1000)
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]

        def phi(t, state):
            return -K.dot(state)

        f_lat = make_fun_lat(phi)
        r = sci.solve_ivp(fun=f_lat, y0=state_0, t_span=t_span, dense_output=True)
        sol_lin_t = r.sol(t)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))
        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")
        ax1.grid(True)
        ax1.legend(loc="lower right")
        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")
        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax2.grid(True)
        ax2.legend(loc="lower right")
        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")
        ax3.grid(True)
        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax3.set_xlabel(r"time $t$")
        ax3.legend(loc="lower right")
        return mo.center(fig)


    lin_sim_k1()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Unfortunately that doesn't work, we have introduced an oscillatory dynamics.

    To correct that, we may introduce some additionial "friction" that prevents our compensation to kick in too fast and end up the control
    $\Delta \phi = \Delta \theta + \beta (d \Delta \theta /dt)$, for some $\beta > 0$, which corresponds to

    $$
    K =
    \begin{bmatrix}
    0 & 0 & -1 & -\beta
    \end{bmatrix}
    \in \mathbb{R}^{4\times 1}
    $$

    Experimentally (see below), anything between $\beta = 0.1$ and $\beta = 5.0$ seems to satisfy the specification. The closed-loop dynamics is slower need $0.1$ and faster near $5.0$.

    In any case, there is a permament drift which is induced on $\Delta x$, which does not converge to $0$. This is corroborated by a double eigenvalue at $0$, which proves that our closed-loop dynamics is **not** asymptotically stable.
    """)
    return


@app.cell(hide_code=True)
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci):
    def lin_sim_k2():

        K = np.array([0.0, 0.0, -1.0, -0.1])

        print(
            "eigenvalues:",
            np.linalg.eig(
                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))
            ).eigenvalues,
        )

        t_span = [0, 20.0]
        t = np.linspace(t_span[0], t_span[1], 1000)
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]

        def phi(t, state):
            return -K.dot(state)

        f_lat = make_fun_lat(phi)
        r = sci.solve_ivp(fun=f_lat, y0=state_0, t_span=t_span, dense_output=True)
        sol_lin_t = r.sol(t)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))
        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")
        ax1.grid(True)
        ax1.legend(loc="lower right")
        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")
        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax2.grid(True)
        ax2.legend(loc="lower right")
        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")
        ax3.grid(True)
        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax3.set_xlabel(r"time $t$")
        ax3.legend(loc="lower right")
        return mo.center(fig)


    lin_sim_k2()
    return


@app.cell
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci):
    def lin_sim_k3():

        K = np.array([0.0, 0.0, -1.0, -5.0])

        print(
            "eigenvalues:",
            np.linalg.eig(
                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))
            ).eigenvalues,
        )

        t_span = [0, 20.0]
        t = np.linspace(t_span[0], t_span[1], 1000)
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]

        def phi(t, state):
            return -K.dot(state)

        f_lat = make_fun_lat(phi)
        r = sci.solve_ivp(fun=f_lat, y0=state_0, t_span=t_span, dense_output=True)
        sol_lin_t = r.sol(t)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))
        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")
        ax1.grid(True)
        ax1.legend(loc="lower right")
        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")
        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax2.grid(True)
        ax2.legend(loc="lower right")
        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")
        ax3.grid(True)
        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax3.set_xlabel(r"time $t$")
        ax3.legend(loc="lower right")
        return mo.center(fig)


    lin_sim_k3()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controller Tuned with Pole Assignment

    Using pole assignement, find a matrix

    $$
    K_{pp} =
    \begin{bmatrix}
    ? & ? & ? & ?
    \end{bmatrix}
    \in \mathbb{R}^{4\times 1}
    $$

    such that the control law

    $$
    \Delta \phi(t)
    = - K_{pp} \cdot
    \begin{bmatrix}
    \Delta x(t) \\
    \Delta \dot{x}(t) \\
    \Delta \theta(t) \\
    \Delta \dot{\theta}(t)
    \end{bmatrix} \in \mathbb{R}
    $$

    satisfies the conditions defined for the manually tuned controller and additionally:

    - result in an asymptotically stable closed-loop dynamics,

    - make $\Delta x(t) \to 0$ in approximately $20$ sec (or less).

    Explain how you find the proper design parameters!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We decide to try to cluster all our eigenvalue near a single real (negative) value
    $s$. If we want a convergence at 5% in 20 seconds at most, we know that $|\lambda|$
    should be at least $3 / 20 = 0.15$.

    Experimentally however this is a bit slow to converge (see below), the setup is better if we pick a faster dynamics, to have our eigenvalues clustered around $-0.5$ for example.

    There is actually quite a range of locations that work, but around $-0.1$, we start compensating too fast and to violate the constraint on the maximal value of $\phi$.
    """)
    return


@app.cell
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci, scipy):
    def lin_sim_3():
        K = scipy.signal.place_poles(
            A=A_lat,
            B=B_lat,
            poles=-0.15 * np.array([1.0, 1.01, 1.02, 1.03]),
        ).gain_matrix.squeeze()

        print(f"K = {K}")

        print(
            "eigenvalues:",
            np.linalg.eig(
                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))
            ).eigenvalues,
        )

        t_span = [0, 20.0]
        t = np.linspace(t_span[0], t_span[1], 1000)
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]

        def phi(t, state):
            return -K.dot(state)

        f_lat = make_fun_lat(phi)
        r = sci.solve_ivp(fun=f_lat, y0=state_0, t_span=t_span, dense_output=True)
        sol_lin_t = r.sol(t)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))
        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")
        ax1.grid(True)
        ax1.legend(loc="lower right")
        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")
        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax2.grid(True)
        ax2.legend(loc="lower right")
        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")
        ax3.grid(True)
        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax3.set_xlabel(r"time $t$")
        ax3.legend(loc="lower right")
        return mo.center(fig)


    lin_sim_3()
    return


@app.cell
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci, scipy):
    Kpp = scipy.signal.place_poles(
        A=A_lat,
        B=B_lat,
        poles=-0.5 * np.array([1.0, 1.01, 1.02, 1.03]),
    ).gain_matrix.squeeze()


    def lin_sim_32():
        K = Kpp
        print(f"K = {K}")

        print(
            "eigenvalues:",
            np.linalg.eig(
                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))
            ).eigenvalues,
        )

        t_span = [0, 20.0]
        t = np.linspace(t_span[0], t_span[1], 1000)
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]

        def phi(t, state):
            return -K.dot(state)

        f_lat = make_fun_lat(phi)
        r = sci.solve_ivp(fun=f_lat, y0=state_0, t_span=t_span, dense_output=True)
        sol_lin_t = r.sol(t)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))
        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")
        ax1.grid(True)
        ax1.legend(loc="lower right")
        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")
        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax2.grid(True)
        ax2.legend(loc="lower right")
        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")
        ax3.grid(True)
        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax3.set_xlabel(r"time $t$")
        ax3.legend(loc="lower right")
        return mo.center(fig)


    lin_sim_32()
    return (Kpp,)


@app.cell
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci, scipy):
    def lin_sim_33():
        K = scipy.signal.place_poles(
            A=A_lat,
            B=B_lat,
            poles=-1.0 * np.array([1.0, 1.01, 1.02, 1.03]),
        ).gain_matrix.squeeze()

        print(f"K = {K}")

        print(
            "eigenvalues:",
            np.linalg.eig(
                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))
            ).eigenvalues,
        )

        t_span = [0, 20.0]
        t = np.linspace(t_span[0], t_span[1], 1000)
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]

        def phi(t, state):
            return -K.dot(state)

        f_lat = make_fun_lat(phi)
        r = sci.solve_ivp(fun=f_lat, y0=state_0, t_span=t_span, dense_output=True)
        sol_lin_t = r.sol(t)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))
        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")
        ax1.grid(True)
        ax1.legend(loc="lower right")
        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")
        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax2.grid(True)
        ax2.legend(loc="lower right")
        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")
        ax3.grid(True)
        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax3.set_xlabel(r"time $t$")
        ax3.legend(loc="lower right")
        return mo.center(fig)


    lin_sim_33()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Controller Tuned with Optimal Control

    Using optimal control, find a gain matrix $K_{oc}$ that satisfies the same set of requirements that the one defined using pole placement.

    Explain how you find the proper design parameters!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The basic optimal control design, with

    $$
    Q = \begin{bmatrix}
    1 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 \\
    0 & 0 & 1 & 0 \\
    0 & 0 & 0 & 1
    \end{bmatrix},
    $$

    and

    $$
    R = \begin{bmatrix}
    1
    \end{bmatrix},
    $$
    almost makes the job, except that it is a bit too fast and that results initially in large values of the angle $\phi$.
    """)
    return


@app.cell
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci, scipy):
    def lin_sim_4():
        Q = np.eye(4,4)
        print("Q:", Q)
        R = np.eye(1) #10*l**2 * np.eye(1)
        print("R:", R)
        Pi = scipy.linalg.solve_continuous_are(
            a=A_lat, 
            b=B_lat, 
            q=Q, 
            r=R
        )
        Koc = (np.linalg.inv(R) @ B_lat.T @ Pi).squeeze()

        K = Koc
        print(f"K = {K}")

        print(
            "eigenvalues:",
            np.linalg.eig(
                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))
            ).eigenvalues,
        )

        t_span = [0, 20.0]
        t = np.linspace(t_span[0], t_span[1], 1000)
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]

        def phi(t, state):
            return -K.dot(state)

        f_lat = make_fun_lat(phi)
        r = sci.solve_ivp(fun=f_lat, y0=state_0, t_span=t_span, dense_output=True)
        sol_lin_t = r.sol(t)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))
        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")
        ax1.grid(True)
        ax1.legend(loc="lower right")
        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")
        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax2.grid(True)
        ax2.legend(loc="lower right")
        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")
        ax3.grid(True)
        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax3.set_xlabel(r"time $t$")
        ax3.legend(loc="lower right")
        return mo.center(fig)


    lin_sim_4()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A second design with the same $Q$ but $R$ increased by $100$ (to reduce the activation of the input at the price of some convergence speed) performs adequately!
    """)
    return


@app.cell
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci, scipy):
    Q = np.eye(4,4)
    print("Q:", Q)
    R = 100 * np.eye(1)
    print("R:", R)
    Pi = scipy.linalg.solve_continuous_are(
        a=A_lat, 
        b=B_lat, 
        q=Q, 
        r=R
    )
    Koc = (np.linalg.inv(R) @ B_lat.T @ Pi).squeeze()

    def lin_sim_42():
        K = Koc
        print(f"K = {K}")

        print(
            "eigenvalues:",
            np.linalg.eig(
                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))
            ).eigenvalues,
        )

        t_span = [0, 20.0]
        t = np.linspace(t_span[0], t_span[1], 1000)
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]

        def phi(t, state):
            return -K.dot(state)

        f_lat = make_fun_lat(phi)
        r = sci.solve_ivp(fun=f_lat, y0=state_0, t_span=t_span, dense_output=True)
        sol_lin_t = r.sol(t)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))
        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")
        ax1.grid(True)
        ax1.legend(loc="lower right")
        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")
        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax2.grid(True)
        ax2.legend(loc="lower right")
        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")
        ax3.grid(True)
        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax3.set_xlabel(r"time $t$")
        ax3.legend(loc="lower right")
        return mo.center(fig)


    lin_sim_42()
    return (Koc,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Validation

    Test the two control strategies (pole placement and optimal control) on the "true" (nonlinear) model with an animation. Check that both controllers achieve their goal; otherwise, go back to the drawing board and tweak the design parameters until they do!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(Kpp, M, booster_anim, g, mo, np, redstart_solve, world):
    def _anim():
        t_span = [0.0, 20.0]
        y0 = [0.0, 0.0, 20.0, 0.0, 45 * np.pi/180.0, 0.0]
        def f_phi(t, state):
            x, dx, y, dy, theta, dtheta = state  
            return np.array(
                [M*g, -Kpp.dot([x, dx, theta, dtheta])]
            )
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[1]
        return mo.Html(
            world(
                [-6, 6, -2, 22], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    _anim()
    return


@app.cell(hide_code=True)
def _(Koc, M, booster_anim, g, mo, np, redstart_solve, world):
    def _anim():
        t_span = [0.0, 20.0]
        y0 = [0.0, 0.0, 20.0, 0.0, 45 * np.pi/180.0, 0.0]
        def f_phi(t, state):
            x, dx, y, dy, theta, dtheta = state  
            return np.array(
                [M*g, -Koc.dot([x, dx, theta, dtheta])]
            )
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[1]
        return mo.Html(
            world(
                [-6, 6, -2, 22], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    _anim()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Exact Linearization

    Let
    $$
    R(\alpha) =
    \begin{bmatrix} +\cos \alpha & -\sin \alpha \\ +\sin \alpha & -\cos \alpha
    \end{bmatrix}
    $$

    Consider an auxiliary system which is meant to compute the force $(f_x, f_y)$ applied to the booster.

    The inputs of the auxiliary system are

    $$
    v = (v_1, v_2) \in \mathbb{R}^2,
    $$

    its dynamics

    $$
    \ddot{z} = v_1 \qquad \text{ where } \qquad z \in \mathbb{R}
    $$

    and its output $(f_x, f_y) \in \mathbb{R}^2$ is given by

    \[
    \begin{bmatrix}
    f_x \\
    f_y
    \end{bmatrix} = R\left(\theta - \frac{\pi}{2}\right)
    \begin{bmatrix}
    z - M\ell\dot{\theta}^2 / 6 \\
    {M\ell v_2}/{6z}
    \end{bmatrix}
    \]

    ⚠️ Note that the second component $f_y$ of the reactor force is undefined whenever $z=0$.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Geometrical Interpretation


    Consider the output $h$ of the original system

    $$
    h :=
    \begin{bmatrix}
    x - (\ell/6) \sin \theta \\
    y + (\ell/6) \cos \theta
    \end{bmatrix} \in \mathbb{R}^2
    $$

    Provide a geometrical interpretation of $h$ (for example, make a drawing).
    """)
    return
@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    The booster is a uniform rod of length $\ell$, center of mass $G$ at $(x, y)$. When it tilts by $\theta$, the unit vector pointing from base to tip along the rod is:
    $$
    \vec{u}_{axe} = \begin{pmatrix} -\sin\theta \\ \cos\theta \end{pmatrix}
    $$

    So $h$ is $G$ shifted by $\ell/6$ toward the tip:
    $$
    h = \begin{pmatrix} x \\ y \end{pmatrix} + \frac{\ell}{6}\,\vec{u}_{axe}
    = \begin{pmatrix} x - (\ell/6)\sin\theta \\ y + (\ell/6)\cos\theta \end{pmatrix}
    $$

    Measured from the base:
    1) engine at $0$
    2) center of mass $G$ at $\ell/2$
    3) point $h$ at $\ell/2 + \ell/6 = 2\ell/3$
    4) tip at $\ell$

    So $h$ is one third down from the tip. For a uniform rod, that's the center of mass of the upper third — a physically meaningful point, not some arbitrary formula.

    Why this specific point? When you differentiate $h$ twice, things cancel out nicely — $\ddot{h}$ ends up depending only on $\theta$ and $z$, with no $\dot\theta$ terms. That's the whole reason $h$ was introduced here, and we'll see it in the next question.
    """)
    return


@app.cell
def _(np, plt):
    def draw_h_point():
        fig, ax = plt.subplots(1, 2, figsize=(12, 7), facecolor="white")

        for k, theta in enumerate([0.0, -np.pi/6]):
            a = ax[k]
            a.set_facecolor("white")
            c, s = np.cos(theta), np.sin(theta)
            ux, uy = -s, c
            x_cm, y_cm = 0.0, 0.0
            L = 4.0
            engine = np.array([x_cm - (L/2)*ux, y_cm - (L/2)*uy])
            nose   = np.array([x_cm + (L/2)*ux, y_cm + (L/2)*uy])
            h_pt   = np.array([x_cm + (L/6)*ux, y_cm + (L/6)*uy])

            a.plot([engine[0], nose[0]], [engine[1], nose[1]],
                   color="steelblue", lw=10, solid_capstyle="round", zorder=2)

            a.plot(*engine, "o", color="tomato", markersize=20, zorder=4)
            a.plot(*engine, "o", color="tomato", markersize=28, alpha=0.25, zorder=3)

            a.plot(*[x_cm, y_cm], "s", color="navy", markersize=13, zorder=5)

            a.plot(*h_pt, "*", color="goldenrod", markersize=24, zorder=5)

            a.plot(*nose, "o", color="white", markersize=8,
                   markeredgecolor="steelblue", markeredgewidth=2, zorder=5)

            a.annotate("G", (x_cm, y_cm), xytext=(-35, 8),
                       textcoords="offset points", color="navy",
                       fontsize=13, fontweight="bold")
            a.annotate(r"$h$", h_pt, xytext=(12, 8),
                       textcoords="offset points", color="goldenrod",
                       fontsize=15, fontweight="bold")
            a.annotate("tip", nose, xytext=(8, 6),
                       textcoords="offset points", color="gray", fontsize=10)
            a.annotate("engine", engine, xytext=(8, -18),
                       textcoords="offset points", color="tomato",
                       fontsize=10, fontweight="bold")

            nx, ny = c, s

            d = 1.2
            def off1(p): return (p[0] + d*nx, p[1] + d*ny)
            Gd, hd = off1((x_cm, y_cm)), off1(h_pt)
            a.annotate("", xy=hd, xytext=Gd,
                       arrowprops=dict(arrowstyle="<->", color="goldenrod", lw=1.8))
            mid = ((Gd[0]+hd[0])/2 + 0.3*nx, (Gd[1]+hd[1])/2 + 0.3*ny)
            a.text(*mid, r"$\ell/6$", color="goldenrod", fontsize=12, fontweight="bold")

            d2 = 2.4
            def off2(p): return (p[0] + d2*nx, p[1] + d2*ny)
            Ed2, Gd2 = off2(engine), off2((x_cm, y_cm))
            a.annotate("", xy=Gd2, xytext=Ed2,
                       arrowprops=dict(arrowstyle="<->", color="gray", lw=1.5))
            mid2 = ((Ed2[0]+Gd2[0])/2 + 0.3*nx, (Ed2[1]+Gd2[1])/2 + 0.3*ny)
            a.text(*mid2, r"$\ell/2$", color="gray", fontsize=11)

            d3 = -1.5
            def off3(p): return (p[0] + d3*nx, p[1] + d3*ny)
            Ed3, hd3 = off3(engine), off3(h_pt)
            a.annotate("", xy=hd3, xytext=Ed3,
                       arrowprops=dict(arrowstyle="<->", color="seagreen", lw=1.8))
            mid3 = ((Ed3[0]+hd3[0])/2 + 0.3*nx - 0.5, (Ed3[1]+hd3[1])/2 + 0.3*ny)
            a.text(*mid3, r"$2\ell/3$", color="seagreen", fontsize=11, fontweight="bold")

            if abs(theta) > 1e-3:
                a.plot([x_cm, x_cm], [y_cm, y_cm + 1.5], "--",
                       color="mediumpurple", lw=1.2, alpha=0.7)
                from matplotlib.patches import Arc
                arc = Arc((x_cm, y_cm), 1.8, 1.8, angle=0,
                          theta1=90 + np.degrees(theta), theta2=90,
                          color="mediumpurple", lw=2)
                a.add_patch(arc)
                a.text(x_cm - 0.5, y_cm + 1.1, r"$\theta$",
                       color="mediumpurple", fontsize=14, fontweight="bold")

            a.set_xlim(-4.5, 4.5)
            a.set_ylim(-4, 4)
            a.set_aspect("equal")
            a.grid(True, alpha=0.2, linestyle="--", color="lightgray")
            a.spines[["top", "right"]].set_visible(False)
            a.set_title(rf"$\theta = {np.degrees(theta):.0f}^\circ$",
                        fontsize=13, pad=12)

        fig.suptitle(
            r"Position of $h$ on the booster — $h = G + (\ell/6)\,\vec{u}_{axe}$",
            fontsize=13, y=1.01
        )
        fig.tight_layout()
        return fig

    draw_h_point()
    return

@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 First and Second-Order Derivatives

    Compute $\dot{h}$ as a function of $\dot{x}$, $\dot{y}$, $\theta$ and $\dot{\theta}$ (and constants) and then $\ddot{h}$ as a function of $\theta$ and $z$ (and constants) when the auxiliary system is plugged in the booster.
    """)
    return

@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    We start from:
    $$
    h_x = x - \tfrac{\ell}{6}\sin\theta,\qquad h_y = y + \tfrac{\ell}{6}\cos\theta.
    $$

    #### First derivative

    Differentiating with respect to time:
    $$
    \dot h_x = \dot x - \tfrac{\ell}{6}\cos\theta\,\dot\theta,\qquad
    \dot h_y = \dot y - \tfrac{\ell}{6}\sin\theta\,\dot\theta.
    $$

    #### Second derivative

    One more differentiation:
    $$
    \ddot h_x = \ddot x + \tfrac{\ell}{6}\sin\theta\,\dot\theta^2 - \tfrac{\ell}{6}\cos\theta\,\ddot\theta
    $$
    $$
    \ddot h_y = \ddot y - \tfrac{\ell}{6}\cos\theta\,\dot\theta^2 - \tfrac{\ell}{6}\sin\theta\,\ddot\theta
    $$

    These still depend on $\ddot x$, $\ddot y$, $\ddot\theta$ so we plug in the booster dynamics.

    Newton and Euler give:
    $$
    M\ddot x = f_x,\qquad M\ddot y = f_y - Mg,\qquad J\ddot\theta = -\tfrac{\ell}{2}f_\perp
    $$

    The auxiliary system defines:
    $$
    \begin{pmatrix} f_x \\ f_y \end{pmatrix}
    = \begin{pmatrix} \sin\theta & \cos\theta \\ -\cos\theta & \sin\theta \end{pmatrix}
    \begin{pmatrix} z - \tfrac{M\ell\dot\theta^2}{6} \\ \tfrac{M\ell v_2}{6z} \end{pmatrix}
    $$

    With $J = M\ell^2/12$ the angular acceleration becomes:
    $$
    \ddot\theta = \frac{v_2}{z}
    $$

    Expanding $\ddot x$ and $\ddot y$:
    $$
    \ddot x = \tfrac{z}{M}\sin\theta - \tfrac{\ell\dot\theta^2}{6}\sin\theta + \tfrac{\ell v_2}{6z}\cos\theta
    $$
    $$
    \ddot y = -\tfrac{z}{M}\cos\theta + \tfrac{\ell\dot\theta^2}{6}\cos\theta + \tfrac{\ell v_2}{6z}\sin\theta - g
    $$

    Substituting into $\ddot h_x$, the $\dot\theta^2$ terms cancel:
    $$
    -\tfrac{\ell\dot\theta^2}{6}\sin\theta + \tfrac{\ell}{6}\sin\theta\,\dot\theta^2 = 0
    $$
    The $v_2$ terms cancel too:
    $$
    \tfrac{\ell v_2}{6z}\cos\theta - \tfrac{\ell}{6}\cos\theta\cdot\tfrac{v_2}{z} = 0
    $$
    What remains:
    $$
    \ddot h_x = \tfrac{z}{M}\sin\theta
    $$

    The same cancellations happen in $\ddot h_y$, leaving:
    $$
    \ddot h_y = -\tfrac{z}{M}\cos\theta - g
    $$

    So overall:
    $$
    \ddot h = \frac{z}{M}\begin{pmatrix}\sin\theta \\ -\cos\theta\end{pmatrix} - \begin{pmatrix} 0 \\ g \end{pmatrix}
    $$

    No $\dot\theta$, no $v_2$. This is exactly why $h$ was defined at $\ell/6$ above $G$ — it's the unique point where the second derivative decouples from the rotational velocity.
    """)
    return

@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Third and Fourth-Order Derivatives

    Compute the third derivative $h^{(3)}$ of $h$ as a function of $\theta$ and $z$ (and constants) and then the fourth derivative $h^{(4)}$ of $h$ with respect to time as a function of $\theta$, $\dot{\theta}$, $z$, $\dot{z}$, $v$ (and constants) when the auxiliary system is on.
    """)
    return

@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    #### Third derivative

    Differentiating $\ddot h = \tfrac{z}{M}\begin{pmatrix}\sin\theta \\ -\cos\theta\end{pmatrix} - \begin{pmatrix}0\\g\end{pmatrix}$ with respect to time, the $g$ term disappears. The product rule on $z\sin\theta$ gives $\dot z \sin\theta + z\cos\theta\,\dot\theta$, and on $z\cos\theta$ gives $\dot z\cos\theta - z\sin\theta\,\dot\theta$:

    $$
    h^{(3)} = \frac{1}{M}
    \begin{pmatrix}
    \dot z\sin\theta + z\cos\theta\,\dot\theta \\
    -\dot z\cos\theta + z\sin\theta\,\dot\theta
    \end{pmatrix}
    $$

    At this stage $h^{(3)}$ still depends only on the state — no inputs appear yet.

    #### Fourth derivative

    Differentiating once more and using $\ddot z = v_1$ and $\ddot\theta = v_2/z$:

    $$
    h^{(4)} = \frac{1}{M}
    \begin{pmatrix}
    \sin\theta & \cos\theta \\
    -\cos\theta & \sin\theta
    \end{pmatrix}
    \begin{pmatrix} v_1 \\ v_2 \end{pmatrix}
    +
    \frac{1}{M}
    \begin{pmatrix}
    2\dot z\cos\theta\,\dot\theta - z\sin\theta\,\dot\theta^2 \\
    2\dot z\sin\theta\,\dot\theta + z\cos\theta\,\dot\theta^2
    \end{pmatrix}
    $$

    The first term is linear in $(v_1, v_2)$ — that's what we steer. The second term depends only on the current state $(\theta, \dot\theta, z, \dot z)$, so it's a known quantity at each instant that can be computed and compensated for.

    The matrix in front of $(v_1, v_2)$ is $R(\theta - \pi/2)$, orthogonal and always invertible regardless of $\theta$. That's what makes exact linearization possible — we can always recover any desired $h^{(4)}$ from a suitable $(v_1, v_2)$, as long as $z \neq 0$.
    """)
    return
@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Exact Linearization

    Show that with yet another auxiliary system with input $u=(u_1, u_2)$ and output $v$ fed into the previous one, we can achieve the dynamics

    $$
    h^{(4)} = u
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 State to Derivatives of the Output

    Implement a function `Tr` of `x, dx, y, dy, theta, dtheta, z, dz` that returns `h_x, h_y, dh_x, dh_y, d2h_x, d2h_y, d3h_x, d3h_y`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Inversion


    Assume for the sake of simplicity that $z<0$ at all times. Show that given the values of $h$, $\dot{h}$, $\ddot{h}$ and $h^{(3)}$, one can uniquely compute the booster state (the values of $x$, $\dot{x}$, $y$, $\dot{y}$, $\theta$, $\dot{\theta}$) and auxiliary system state (the values of $z$ and $\dot{z}$).

    Implement the corresponding function `T_inv`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Admissible Path Computation

    Implement a function

    ```python
    def compute(
        x_0,
        dx_0,
        y_0,
        dy_0,
        theta_0,
        dtheta_0,
        z_0,
        dz_0,
        x_tf,
        dx_tf,
        y_tf,
        dy_tf,
        theta_tf,
        dtheta_tf,
        z_tf,
        dz_tf,
        tf,
    ):
        ...

    ```

    that returns a function `fun` such that `fun(t)` is a value of `x, dx, y, dy, theta, dtheta, z, dz, f, phi` at time `t` that match the initial and final values provided as arguments to `compute`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Graphical Validation

    Test your `compute` function with

    - `(x_0, dx_0, y_0, dy_0, theta_0, dtheta_0, z_0, dz_0) = (5.0, 0.0, 20.0, -1.0, -np.pi/8, 0.0, -M*g, 0.0`),
    - `(x_tf, dx_tf, y_tf, dy_tf, theta_tf, dtheta_tf, z_tf, dz_tf) = (0.0, 0.0, 2/3*l, 0.0,     0.0, 0.0, -M*g, 0.0`),
    - `tf = 10.0`.

    Make the graph of the relevant variables as a function of time, then make an animation out of the same result. Comment and iterate if necessary!
    """)
    return


if __name__ == "__main__":
    app.run()
