import pyautogui


class m_input:
    def __init__(self, precision, speed):
        # set precision and speed values for the mouse
        dictionary_precision = {'high': 100,
                                'low': 1000,
                                'medium': 500}
        dictionary_speed = {'fast': 1,
                            'slow': 10,
                            'medium': 5}

        self.precision = dictionary_precision[precision]
        self.speed = dictionary_speed[speed]

# call move function with x and y output of the gaze model
    def move(self, x, y):
        pyautogui.move(x * self.precision, -1 * y * self.precision, duration=self.speed)
