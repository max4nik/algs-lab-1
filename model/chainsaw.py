class Chainsaw:
    def __init__(self, name='chainsaw', power_in_watt=0, rolls_per_minute=0):
        """
        chainsaw class constructor
        :param name: model of chainsaw
        """
        self.name = name
        self.power_in_watt = power_in_watt
        self.rolls_per_minute = rolls_per_minute

    def __str__(self):
        """
        :return: chainsaw class string representation
        """
        return '\nName: "' + str(self.name) + \
               '"\nPower in watt: ' + str(self.power_in_watt) + \
               '\nRolls per minute: ' + str(self.rolls_per_minute) + "\n"
