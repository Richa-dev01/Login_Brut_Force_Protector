
class LoginDFA:

    def __init__(self):
        self.state = "START"

        self.transitions = {
            "START": {
                "C": "SUCCESS",
                "F": "ONE_FAIL"
            },

            "ONE_FAIL": {
                "C": "SUCCESS",
                "F": "TWO_FAIL"
            },

            "TWO_FAIL": {
                "C": "SUCCESS",
                "F": "LOCKED"
            },

            "SUCCESS": {
                "C": "SUCCESS",
                "F": "ONE_FAIL"
            },

            "LOCKED": {
                "C": "LOCKED",
                "F": "LOCKED"
            }
        }

    def process(self, symbol):

        if self.state == "LOCKED":
            return self.state

        self.state = self.transitions[self.state][symbol]

        return self.state

    def reset(self):
        self.state = "START"