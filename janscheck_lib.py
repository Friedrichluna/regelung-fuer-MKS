import control as ctrl
import matplotlib.pyplot as plt

#{w_0}
def sop_ud(w_0):
    pol = ctrl.TransferFunction([1/(w_0**2), 0 , 1], [1])
    return pol

#{d_0, w_0}
def sop(d_0, w_0):
    pol = ctrl.TransferFunction([1/(w_0**2), 2*d_0/w_0, 1], [1])
    return pol

#[w_0]
def fop(w_0):
    pol = ctrl.TransferFunction([1/w_0, 1], [1])
    return pol

def s():
    pol = ctrl.TransferFunction([1, 0], [1])
    return pol


def pid(Kp, Ki, Kd):
    C = ctrl.TransferFunction([Kd, Kp, Ki], [1, 0])
    return C



def bode_plot(sys):
    plt.figure()
    ctrl.bode_plot(sys)
    plt.show(block=False)

def step_response_plot(sys):
    t, y = ctrl.step_response(sys)
    plt.figure()
    plt.plot(t, y)
    plt.title("Step Response")
    plt.xlabel("Time (s)")
    plt.ylabel("Output")
    plt.grid(True)
    plt.show(block=False)

def disturbance_step_response_plot(H, P):
    closed_loop = ctrl.feedback(P, H)
    t, y = ctrl.step_response(closed_loop)
    plt.figure()
    plt.plot(t, y)
    plt.title("Closed-Loop Disturbance Step Response")
    plt.xlabel("Time (s)")
    plt.ylabel("Output")
    plt.grid(True)
    plt.show(block=False)

def nichols_plot(open_loop):
    plt.figure()
    ctrl.nichols_plot(open_loop)
    plt.grid(True)
    plt.show(block=False)

def nyquist_plot(sys):
    plt.figure()
    ctrl.nyquist_plot(sys)
    plt.grid(True)
    plt.show(block=False)