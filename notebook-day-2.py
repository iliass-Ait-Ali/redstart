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

    return np, plt, scipy


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


@app.cell(hide_code=True)
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


@app.cell(hide_code=True)
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
    mo.md(r"""
    ### 🔓 Solution

    An equilibrium is a state where nothing changes — all velocities and accelerations are zero. So we need:

    $$
    v_x = v_y = \omega = 0 \quad \text{and} \quad \ddot{x} = \ddot{y} = \ddot{\theta} = 0
    $$

    **From $\ddot{\theta} = 0$:**
    $$
    J\ddot{\theta} = -f \frac{\ell}{2} \sin\phi = 0
    $$
    Since $f > 0$, we need $\sin\phi = 0$, so $\phi = 0$.

    **From $\ddot{x} = 0$:**
    $$
    M\ddot{x} = -f\sin(\theta + \phi) = -f\sin\theta = 0
    $$
    Since $f > 0$, we need $\sin\theta = 0$, so $\theta = 0$.

    **From $\ddot{y} = 0$:**
    $$
    M\ddot{y} = f\cos(0) - Mg = f - Mg = 0
    $$
    So $f = Mg$.

    **Conclusion:** the only equilibrium is
    $$
    \boxed{\theta = 0, \quad \phi = 0, \quad f = Mg}
    $$
    with $x$, $y$ arbitrary and all velocities zero.
    """)
    return


@app.cell
def _(M, g):
    f_eq = M * g
    theta_eq = 0.0
    phi_eq = 0.0
    print(f"Equilibrium: f = {f_eq} N,  theta = {theta_eq} rad,  phi = {phi_eq} rad")
    return f_eq, phi_eq, theta_eq


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
    mo.md(r"""
    ### 🔓 Solution

    We write the state and inputs as small perturbations around the equilibrium:
    $$
    \theta = 0 + \Delta\theta, \quad \phi = 0 + \Delta\phi, \quad f = Mg + \Delta f
    $$

    For small angles:
    $$
    \sin(\Delta\theta + \Delta\phi) \approx \Delta\theta + \Delta\phi, \qquad \cos(\Delta\theta + \Delta\phi) \approx 1, \qquad \sin(\Delta\phi) \approx \Delta\phi
    $$

    **Linearizing $\ddot{x}$:**
    $$
    M\Delta\ddot{x} = -(Mg + \Delta f)(\Delta\theta + \Delta\phi) \approx -Mg(\Delta\theta + \Delta\phi)
    $$
    $$
    \implies \Delta\ddot{x} = -g(\Delta\theta + \Delta\phi)
    $$

    **Linearizing $\ddot{y}$:**
    $$
    M\Delta\ddot{y} = (Mg + \Delta f)(1) - Mg = \Delta f
    \implies \Delta\ddot{y} = \frac{\Delta f}{M}
    $$

    **Linearizing $\ddot{\theta}$:**
    $$
    J\Delta\ddot{\theta} = -Mg\frac{\ell}{2}\Delta\phi
    \implies \Delta\ddot{\theta} = -\frac{Mg\ell}{2J}\Delta\phi
    $$
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

    State vector $s = (\Delta x,\ \Delta\dot{x},\ \Delta y,\ \Delta\dot{y},\ \Delta\theta,\ \Delta\dot{\theta})$, inputs $u = (\Delta f,\ \Delta\phi)$.

    $$
    A = \begin{bmatrix}
    0 & 1 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & -g & 0 \\
    0 & 0 & 0 & 1 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 1 \\
    0 & 0 & 0 & 0 & 0 & 0
    \end{bmatrix}, \qquad
    B = \begin{bmatrix}
    0 & 0 \\
    0 & -g \\
    0 & 0 \\
    1/M & 0 \\
    0 & 0 \\
    0 & -Mg\ell/(2J)
    \end{bmatrix}
    $$

    Note: entry $A_{2,5} = -g$ captures the coupling between tilt $\Delta\theta$ and lateral acceleration $\Delta\ddot{x}$. And $B$ shows that $\Delta\phi$ affects both $\Delta\ddot{x}$ and $\Delta\ddot{\theta}$, while $\Delta f$ only affects $\Delta\ddot{y}$ — vertical and lateral dynamics are decoupled.
    """)
    return


@app.cell
def _(J, M, g, l, np):
    A = np.array([
        [0, 1, 0, 0,  0, 0],
        [0, 0, 0, 0, -g, 0],
        [0, 0, 0, 1,  0, 0],
        [0, 0, 0, 0,  0, 0],
        [0, 0, 0, 0,  0, 1],
        [0, 0, 0, 0,  0, 0],
    ], dtype=float)

    B = np.array([
        [0,            0],
        [0,           -g],
        [0,            0],
        [1/M,          0],
        [0,            0],
        [0, -M*g*l/(2*J)],
    ], dtype=float)

    print("A =\n", A)
    print("\nB =\n", B)
    return A, B
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

    #### Asymptotic Stability

    For a linear time-invariant system $\dot{s} = As$, the equilibrium $s = 0$ is **asymptotically stable** if and only if every eigenvalue $\lambda_i$ of $A$ satisfies $\text{Re}(\lambda_i) < 0$.

    The reasoning is straightforward: the general solution of $\dot{s} = As$ is a linear combination of modes of the form $e^{\lambda_i t} v_i$ where $v_i$ are the eigenvectors. If $\text{Re}(\lambda_i) < 0$, the corresponding mode decays exponentially to zero. If $\text{Re}(\lambda_i) = 0$, the mode neither grows nor decays (marginal stability). If $\text{Re}(\lambda_i) > 0$, the mode grows without bound (instability).

    For our booster, the matrix $A$ encodes the open-loop dynamics — meaning no control input, just the natural evolution of the system under gravity.
    """)
    return


@app.cell
def _(A, np):
    eigenvalues = np.linalg.eigvals(A)
    print("Eigenvalues of A:", eigenvalues)
    print("Real parts:", np.real(eigenvalues))
    return (eigenvalues,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    All six eigenvalues are exactly zero. This means the system is **not** asymptotically stable.

    Physically, this makes complete sense: a booster hovering at equilibrium ($\theta=0$, $f=Mg$) with no active control has no mechanism to correct itself if perturbed. A small tilt $\Delta\theta$ will generate a horizontal force component, causing the booster to drift sideways — and nothing brings it back. The system is **marginally stable** in the Lyapunov sense: perturbations neither grow exponentially nor decay, but the booster drifts away from equilibrium indefinitely.

    This confirms that **feedback control is necessary** to stabilize the booster.
    """)
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

    #### Can we fix this with control?

    The **Kalman rank condition** says the system $\dot{s} = As + Bu$ is controllable if and only if the controllability matrix

    $$
    \mathcal{C} = \begin{bmatrix} B \mid AB \mid A^2B \mid \cdots \mid A^{n-1}B \end{bmatrix} \in \mathbb{R}^{n \times nm}
    $$

    has rank $n$. Each block $A^k B$ captures which directions in state space become reachable after $k$ steps of applying the input. If they span all of $\mathbb{R}^n$, the system is fully controllable.

    Here $n = 6$ and $m = 2$, so $\mathcal{C} \in \mathbb{R}^{6 \times 12}$.
    """)
    return


@app.cell
def _(A, B, np):
    n = A.shape[0]
    cols = [np.linalg.matrix_power(A, k) @ B for k in range(n)]
    C_kalman = np.hstack(cols)
    rank = np.linalg.matrix_rank(C_kalman)
    print(f"rank(C) = {rank}  /  n = {n}")
    print("System is controllable:", rank == n)
    return C_kalman, rank


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Full rank — the system is **completely controllable**. Even though the booster is unstable in open loop, a stabilizing feedback controller is guaranteed to exist. Now we just have to find one.
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
    return@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    #### Simplifying the problem

    Up to now we've been working with the full 6-dimensional system. But if you think about what actually matters for landing, the vertical dynamics ($y$ and $\dot{y}$) are relatively straightforward — just tune the thrust magnitude $f$. The genuinely tricky part is keeping the booster upright and laterally centered, which involves $x$, $\dot{x}$, $\theta$, $\dot{\theta}$.

    So let's focus on that. We fix $f = Mg$ (thrust exactly cancels gravity) and use only $\phi$ as our control input. The $y$ equations disappear from the picture.

    With $\Delta f = 0$ the linearized equations reduce to:
    $$
    \Delta\ddot{x} = -g(\Delta\theta + \Delta\phi), \qquad \Delta\ddot{\theta} = -\frac{Mg\ell}{2J}\Delta\phi
    $$

    Writing this in state-space form with reduced state $(\Delta x, \Delta\dot{x}, \Delta\theta, \Delta\dot{\theta})$:

    $$
    A_{lat} = \begin{bmatrix}
    0 & 1 & 0 & 0 \\
    0 & 0 & -g & 0 \\
    0 & 0 & 0 & 1 \\
    0 & 0 & 0 & 0
    \end{bmatrix}, \qquad
    B_{lat} = \begin{bmatrix} 0 \\ -g \\ 0 \\ -Mg\ell/(2J) \end{bmatrix}
    $$

    Notice that $A_{lat}$ still has the $-g$ coupling between $\Delta\theta$ and $\Delta\ddot{x}$ — a tilt always accelerates the booster sideways. And $B_{lat}$ shows that $\phi$ affects both the lateral acceleration and the angular acceleration simultaneously.

    Now let's check controllability of this reduced system — we only have one input now, so this is a stricter test.
    """)
    return


@app.cell
def _(J, M, g, l, np):
    A_lat = np.array([
        [0, 1,  0, 0],
        [0, 0, -g, 0],
        [0, 0,  0, 1],
        [0, 0,  0, 0],
    ], dtype=float)

    B_lat = np.array([
        [0],
        [-g],
        [0],
        [-M*g*l/(2*J)],
    ], dtype=float)

    print("A_lat =\n", A_lat)
    print("\nB_lat =\n", B_lat)

    n_lat = A_lat.shape[0]
    cols_lat = [np.linalg.matrix_power(A_lat, k) @ B_lat for k in range(n_lat)]
    C_lat = np.hstack(cols_lat)
    rank_lat = np.linalg.matrix_rank(C_lat)
    print(f"\nrank(C_lat) = {rank_lat}  /  n = {n_lat}")
    print("Lateral system controllable:", rank_lat == n_lat)
    return A_lat, B_lat, rank_lat


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Full rank — even with a single input $\phi$ we can control all four lateral states. This makes physical sense: tilting the nozzle by $\Delta\phi$ creates a torque $\tau = -Mg(\ell/2)\Delta\phi$ that rotates the booster, and a tilted booster with angle $\Delta\theta$ produces a horizontal force $-Mg\Delta\theta$ that moves it laterally. So $\phi$ propagates through the dynamics and indirectly controls everything — it just takes a couple of steps.
    """)
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

    With $\phi = 0$ the closed-loop reduces to $\dot{s} = A_{lat} s$ with no input at all. Let's simulate from $\theta(0) = \pi/4$ and see what happens.
    """)
    return


@app.cell
def _(A_lat, np, plt, scipy):
    s0 = np.array([0.0, 0.0, np.pi/4, 0.0])
    t_eval = np.linspace(0, 10, 500)

    sol_openloop = scipy.integrate.solve_ivp(
        lambda t, s: A_lat @ s,
        [0, 10], s0, t_eval=t_eval
    )

    fig, axes = plt.subplots(1, 2, figsize=(10, 4))

    axes[0].plot(sol_openloop.t, sol_openloop.y[0])
    axes[0].set_title(r"$\Delta x(t)$")
    axes[0].set_xlabel("time (s)")
    axes[0].grid(True)

    axes[1].plot(sol_openloop.t, sol_openloop.y[2])
    axes[1].axhline(np.pi/4, color='r', ls='--', label=r"$\theta(0) = \pi/4$")
    axes[1].set_title(r"$\Delta\theta(t)$")
    axes[1].set_xlabel("time (s)")
    axes[1].legend()
    axes[1].grid(True)

    plt.tight_layout()
    fig
    return (sol_openloop,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Two things stand out:

    **$\theta(t)$ stays constant at $\pi/4$.** With $\phi = 0$ the torque equation gives $J\Delta\ddot{\theta} = 0$, so $\Delta\dot{\theta} = 0$ and $\Delta\theta$ never changes. The booster is stuck tilted with no mechanism to correct itself.

    **$x(t)$ grows parabolically.** The constant tilt $\Delta\theta = \pi/4$ produces a constant horizontal acceleration $\Delta\ddot{x} = -g\Delta\theta = -g\pi/4$. Integrating twice gives $\Delta x(t) = -\frac{g\pi}{8} t^2$ — a parabola, exactly what we see.

    This is the open-loop instability in action. Without any corrective $\phi$, a tilted booster just keeps accelerating sideways indefinitely. This is why active control is not optional — it's the only thing keeping the booster from flying off sideways.
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
    mo.md(r"""
    ### 🔓 Solution

    #### Designing a controller by hand

    The control law is $\Delta\phi = -k_3\Delta\theta - k_4\Delta\dot{\theta}$. The idea is simple: $k_3$ acts like a spring — it creates a restoring torque proportional to the current tilt. $k_4$ acts like a damper — it resists angular velocity to avoid oscillations.

    With this control law, the closed-loop $\theta$ equation becomes:
    $$
    J\Delta\ddot{\theta} = -\frac{Mg\ell}{2}(k_3\Delta\theta + k_4\Delta\dot{\theta})
    $$

    which is exactly a **second-order damped oscillator**:
    $$
    \Delta\ddot{\theta} + \frac{Mg\ell}{2J}k_4\,\Delta\dot{\theta} + \frac{Mg\ell}{2J}k_3\,\Delta\theta = 0
    $$

    Identifying with the standard form $\ddot{\theta} + 2\zeta\omega_n\dot{\theta} + \omega_n^2\theta = 0$:
    $$
    \omega_n = \sqrt{\frac{Mg\ell}{2J}k_3}, \qquad \zeta = \frac{k_4}{2}\sqrt{\frac{Mg\ell}{2Jk_3}}
    $$

    With our values $M=1$, $g=1$, $\ell=2$, $J=1/3$:
    $$
    \frac{Mg\ell}{2J} = \frac{1 \cdot 1 \cdot 2}{2 \cdot 1/3} = 3
    $$

    So $\omega_n = \sqrt{3k_3}$ and $\zeta = \frac{k_4}{2}\sqrt{\frac{3}{k_3}}$.

    For convergence in ~20s we want a time constant $\tau \approx 5$s, so $\zeta\omega_n \approx 1/\tau = 0.2$. For a well-damped response we want $\zeta \approx 0.7$.

    **Starting point:** $\omega_n = 0.2/0.7 \approx 0.3$ rad/s, so $k_3 = \omega_n^2/3 \approx 0.03$. Then $k_4 = 2\zeta/\sqrt{3/k_3} \approx 0.5$.

    Let's try several values and see:
    """)
    return


@app.cell
def _(A_lat, B_lat, np, plt, scipy):
    def sim_K(k3, k4):
        K = np.array([[0, 0, k3, k4]])
        A_cl = A_lat - B_lat @ K
        s0 = np.array([0.0, 0.0, np.pi/4, 0.0])
        sol = scipy.integrate.solve_ivp(
            lambda t, s: A_cl @ s,
            [0, 30], s0,
            t_eval=np.linspace(0, 30, 1000)
        )
        return sol, -(K @ sol.y)[0]

    fig_man, axes_man = plt.subplots(1, 2, figsize=(12, 4))

    for k3, k4, lbl in [
        (0.5, 0,   "k3=0.5, k4=0   — undamped oscillation"),
        (1,   0,   "k3=1,   k4=0   — still oscillating"),
        (2,   3,   "k3=2,   k4=3   — damped but slow"),
        (2,   5,   "k3=2,   k4=5   — converges in ~15s ✓"),
    ]:
        sol_k, phi_k = sim_K(k3, k4)
        axes_man[0].plot(sol_k.t, sol_k.y[2], label=lbl)
        axes_man[1].plot(sol_k.t, phi_k, label=lbl)

    for ax in axes_man:
        ax.axhline( np.pi/2, color='r', ls=':', lw=1, label=r"$\pm\pi/2$ limit")
        ax.axhline(-np.pi/2, color='r', ls=':', lw=1)
        ax.axhline(0, color='k', ls='--', lw=0.8)
        ax.grid(True)
        ax.legend(fontsize=7)
        ax.set_xlabel("time (s)")

    axes_man[0].set_title(r"$\Delta\theta(t)$")
    axes_man[1].set_title(r"$\Delta\phi(t)$")
    plt.tight_layout()
    fig_man
    return sim_K,


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The best candidate is $k_3=2, k_4=5$:
    - $\omega_n = \sqrt{3 \times 2} = \sqrt{6} \approx 2.45$ rad/s
    - $\zeta = \frac{5}{2}\sqrt{\frac{3}{2}} \approx 3.06$ — heavily overdamped, which explains the smooth non-oscillatory convergence

    $\theta$ reaches zero in about 15s, and $|\Delta\phi|$ stays well within $\pi/2$ throughout. Let's verify the closed-loop stability formally:
    """)
    return


@app.cell
def _(A_lat, B_lat, np):
    K_manual = np.array([[0, 0, 2.0, 5.0]])
    A_cl_manual = A_lat - B_lat @ K_manual
    eigs_manual = np.linalg.eigvals(A_cl_manual)
    print("K_manual =", K_manual)
    print("Closed-loop eigenvalues:", np.round(eigs_manual, 4))
    print("All real parts negative?", all(np.real(eigs_manual) < 0))
    return A_cl_manual, K_manual


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Two eigenvalues have strictly negative real part — the $\theta$ and $\omega$ modes are stabilized. But two eigenvalues are still exactly zero, corresponding to the $x$ and $\dot{x}$ modes that we deliberately left uncontrolled. So $\theta \to 0$ as required, but $x$ will keep drifting — which is fine for now, since the problem only asked us to stabilize the tilt.
    """)
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
    mo.md(r"""
    ### 🔓 Solution

    #### From manual tuning to systematic pole placement

    The manual approach worked but it was mostly trial and error. Pole placement gives us a more principled method: we directly **choose where we want the closed-loop eigenvalues to be**, and the algorithm computes the gain matrix $K_{pp}$ that puts them there.

    Recall that the closed-loop dynamics are $\dot{s} = (A_{lat} - B_{lat}K_{pp})s$. The eigenvalues of $A_{lat} - B_{lat}K_{pp}$ are the **poles** of the closed-loop system, and they completely determine how the system responds:

    - A pole at $\lambda = \sigma + j\omega$ gives a mode that evolves like $e^{\sigma t}(\cos\omega t + \sin\omega t)$
    - For stability we need $\sigma < 0$ so the mode decays
    - The time constant is $\tau = 1/|\sigma|$ — how long before that mode dies out
    - For convergence in ~20s we want $\tau \approx 5$s, meaning $|\sigma| \approx 0.2$

    #### Why do we damp $\theta$ faster than $x$?

    This is the key design choice. The dynamics of the system create a **cascade**: $\phi$ directly controls $\theta$, and $\theta$ indirectly controls $x$ through the coupling term $-g\Delta\theta$ in the $\ddot{x}$ equation.

    Think about it physically: if the booster is tilted, it accelerates sideways. So before $x$ can converge, $\theta$ must already be close to zero — otherwise the booster keeps drifting. This means we **must** stabilize $\theta$ faster than $x$, otherwise the controller fights itself.

    If we placed the $\theta$ poles slower than the $x$ poles, the lateral position would try to correct itself while the booster is still tilted, generating a chaotic back-and-forth. The cascade structure of the dynamics imposes a natural ordering: fix the tilt first, then the position follows.

    There's also a practical constraint: $|\Delta\phi| < \pi/2$ at all times. Placing the $\theta$ poles too far left (very fast convergence) would require large $\phi$ corrections right at $t=0$ when $\theta(0) = \pi/4$ — we might violate the constraint. So we can't just push all poles as far left as we want.

    Balancing all this, I choose:
    $$
    \lambda_{1,2} = -0.3 \pm 0.2j \quad \Rightarrow \quad \tau \approx 3.3\text{s} \quad \text{(}x\text{ modes — slower)}
    $$
    $$
    \lambda_{3,4} = -0.5 \pm 0.3j \quad \Rightarrow \quad \tau = 2\text{s} \quad \text{(}\theta\text{ modes — faster)}
    $$

    The imaginary parts $\pm 0.2j$ and $\pm 0.3j$ introduce mild oscillations in the response — just enough to make the convergence smooth without being purely exponential, which would require very large gains.
    """)
    return


@app.cell
def _(A_lat, B_lat, np, plt, scipy):
    desired_poles = np.array([-0.3 + 0.2j, -0.3 - 0.2j, -0.5 + 0.3j, -0.5 - 0.3j])
    result_pp = scipy.signal.place_poles(A_lat, B_lat, desired_poles)
    K_pp = result_pp.gain_matrix

    A_cl_pp = A_lat - B_lat @ K_pp
    eigs_pp = np.linalg.eigvals(A_cl_pp)
    print("K_pp =", np.round(K_pp, 4))
    print("Closed-loop eigenvalues:", np.round(eigs_pp, 4))
    print("Asymptotically stable:", all(np.real(eigs_pp) < 0))

    s0 = np.array([0.0, 0.0, np.pi/4, 0.0])
    sol_pp = scipy.integrate.solve_ivp(
        lambda t, s: A_cl_pp @ s,
        [0, 30], s0,
        t_eval=np.linspace(0, 30, 1000)
    )
    phi_pp = -(K_pp @ sol_pp.y)[0]

    fig_pp, axes_pp = plt.subplots(1, 3, figsize=(14, 4))

    axes_pp[0].plot(sol_pp.t, sol_pp.y[0])
    axes_pp[0].set_title(r"$\Delta x(t)$")
    axes_pp[0].set_xlabel("time (s)")
    axes_pp[0].grid(True)

    axes_pp[1].plot(sol_pp.t, sol_pp.y[2])
    axes_pp[1].axhline(0, color='k', ls='--', lw=0.8)
    axes_pp[1].set_title(r"$\Delta\theta(t)$")
    axes_pp[1].set_xlabel("time (s)")
    axes_pp[1].grid(True)

    axes_pp[2].plot(sol_pp.t, phi_pp)
    axes_pp[2].axhline( np.pi/2, color='r', ls=':', label=r"$\pm\pi/2$ limit")
    axes_pp[2].axhline(-np.pi/2, color='r', ls=':')
    axes_pp[2].set_title(r"$\Delta\phi(t)$")
    axes_pp[2].set_xlabel("time (s)")
    axes_pp[2].legend()
    axes_pp[2].grid(True)

    plt.tight_layout()
    fig_pp
    return A_cl_pp, K_pp, sol_pp


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Both $\Delta x$ and $\Delta\theta$ converge to zero well within 20s, $|\Delta\phi|$ stays within $\pi/2$, and all four closed-loop eigenvalues have strictly negative real part — the system is **asymptotically stable**.

    Compared to the manual controller, pole placement gave us full control over both the $x$ and $\theta$ dynamics simultaneously. The tradeoff is that it requires an accurate model — it's entirely model-based.
    """)
    return

@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controller Tuned with Optimal Control

    Using optimal control, find a gain matrix $K_{oc}$ that satisfies the same set of requirements that the one defined using pole placement.

    Explain how you find the proper design parameters!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Validation

    Test the two control strategies (pole placement and optimal control) on the "true" (nonlinear) model with an animation. Check that both controllers achieve their goal; otherwise, go back to the drawing board and tweak the design parameters until they do!
    """)
    return


if __name__ == "__main__":
    app.run()
