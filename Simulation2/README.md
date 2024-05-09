# Simulation 2

This scenario is a *non-stationary* variant of Simulation 1.

After each *Scan* command sent by the attacker, the Server will detect the attempt at scanning with probability *probdetection*. If the scan is detected, the Server will move the flag to a new random port.

This code has been modified to implement several agents attacking a single server of n ports. The agents each take a certain number of ports and focus their efforts on those ports. Then, after they've finished, the matrices of each agent are combined into a final product.
