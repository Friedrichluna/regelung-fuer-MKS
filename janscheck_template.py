import control as ctrl
import matplotlib.pyplot as plt
from janscheck_lib import *

# process parameters
V_p = 0.5
d = 0.01
w = 1
w_par = 10*w

#sop(d_0, w_0) -- second order polynomial {d_0, w_0}
#fop(w_0) -- first order polynomial [w_0]

# process
P = V_p/(sop(d_0=d, w_0=w) * fop(w_0=w_par))

# controller
H = 4*sop(d_0=0.1, w_0=w) / (s() * fop(w_0=10*w))

open_loop = H * P
closed_loop = ctrl.feedback(open_loop, 1)

bode_plot(open_loop)

step_response_plot(closed_loop)
disturbance_step_response_plot(H, P)
nyquist_plot(open_loop)
nichols_plot(open_loop)

input("Press Enter to close plots and exit...")
plt.close('all')
