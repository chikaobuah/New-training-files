class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.bottom = bottom
        self.top = top
        self.current = current
        pass
    def up(self):
        """Makes the elevator go up one floor."""
        self.current += 1
        if self.current >= self.top:
           self.current =  self.top              
        pass
    def down(self):
        """Makes the elevator go down one floor."""
        self.current -= 1
        if self.current <= self.bottom:
           self.current =  self.bottom  
        pass
    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        self.floor = floor
        self.current = floor
        pass

elevator = Elevator(-1, 10, 0)
