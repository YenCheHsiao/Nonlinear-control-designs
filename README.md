# Nonlinear-control-designs
Codes for Nonlinear control designs and their application to cancer differentiation therapy

# Instruction
* For the control designs and comparison, please go the the folder: Code/Comparison of output responses
  * The figure of the comparison result will be generated after running the codes below
    1. "1. SC and DI optimal (unit).py" has the control design and of the sigmoid-based controller and domain controller. 
    2. "2. PID and IC optimal (unit).py" has the control design and of the PID impulsive controller and impulsive controller.
    3. "3. PDI and DI optimal (unit).py" has the control design and of the polynomial dynamic inversion controller and domain controller.
    4. "4p. Cancer PID Impulsive Domain control Dif D (unit).py" has the control design and of the PID impulsive controller with different value of KD.
    5. "4p. Cancer PID Impulsive Domain control Dif I (unit).py" has the control design and of the PID impulsive controller with different value of KI.
    6. "4p. Cancer PID Impulsive Domain control Dif T (unit).py" has the control design and of the PID impulsive controller with different value of T.
    7. "5p. Unified, sigmoid, and PDI optimal (unit).py" has the control design and of the unified control design of the sigmoid-based controller and the polynomial dynamic inversion controller.
   
* For the robustness test, please go the the folder: Code/Robustness test
  * The figure of the robustness test using Mote carlo simulation will be generated after running the codes below
    1. "Robustness all sens_ Cancer Domain control optimal" has the robustness test of the domain controller.
    2. "Robustness all sens_ Cancer Polynomial DI control optimal" has the robustness test of the polynomial dynamic inversion controller.
    3. "Robustness all sens_ Cancer Sigmoid control optimal" has the robustness test of the sigmoid-based controller.

* For the sensitivity analysis, please go the the folder: Code/Sensitivity analysis
  * The figure of the sensitivity analysis using Sobol Sensitivity analysis will be generated after running the code below
    1. "Sensitivity_analysis.py"
   
* For the convergence result in the parameter plane (𝑇 , 𝐾𝑃), please go the the folder: Code/Simple perceptron
  * The figure of the classification result using simple perceptron will be generated after running the code below
    1. "gain and T in IC control.py" contains the simple perceptron algorithm.
    2. After running "gain and T in IC control.py", a file called "Converge.npy" will be generated under the same folder. Run "(Load) gain and T in IC control.py" to get the figures without re-run the simple perceptron algorithm.
