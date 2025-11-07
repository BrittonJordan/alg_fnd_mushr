from __future__ import division
import numpy as np

from control.controller import BaseController
from control.controller import compute_position_in_frame


class PurePursuitController(BaseController):
    def __init__(self, **kwargs):
        self.car_length = kwargs.pop("car_length")

        # Get the keyword args that we didn't consume with the above initialization
        super(PurePursuitController, self).__init__(**kwargs)


    def get_error(self, pose, reference_xytv):
        """Compute the Pure Pursuit error.

        Args:
            pose: current state of the vehicle [x, y, heading]
            reference_xytv: reference state and speed

        Returns:
            error: Pure Pursuit error
        """
        return compute_position_in_frame(reference_xytv[:3], pose)

    def get_control(self, pose, reference_xytv, error):
        """Compute the Pure Pursuit control law.

        Args:
            pose: current state of the vehicle [x, y, heading]
            reference_xytv: reference state and speed
            error: error vector from get_error

        Returns:
            control: np.array of velocity and steering angle
        """
        # BEGIN QUESTION 3.1

        e_x, e_y = float(error[0]), float(error[1])
        
        lookahead_squared = e_x**2 + e_y**2

        if lookahead_squared < 1e-6:
            steering_angle = 0.0
        else:
            steering_angle = np.arctan2(2.0 * self.car_length * e_y, lookahead_squared)

        control = np.array([reference_xytv[3], steering_angle])
        return control
        # END QUESTION 3.1

        # alpha =  (np.arctan2((reference_xytv[1] - pose[1]), (reference_xytv[0] - pose[0])) - pose[2]) # tracks wave but not circle
        # alpha =  (np.arctan((reference_xytv[1] - pose[1]) / (reference_xytv[0] - pose[0])) - pose[2]) # tracks wave but not circle
        # alpha =  -(np.arctan((reference_xytv[1] - pose[1]) / (reference_xytv[0] - pose[0])) - pose[2]) # passes unit test