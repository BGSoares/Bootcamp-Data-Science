import numpy as np
import random
import pandas as pd

class Customer():
    """
    A single customer that moves through the supermarket in an MCMC simulation.
    """
    def __init__(self, name:int, state:str, transition_probs:pd.DataFrame, budget=100):
        self.name = name
        self.state = state
        self.transition_probs = transition_probs
        self.initial_state = 'entrance'
        self.final_state = 'checkout'


    def __repr__(self):
        return f'<Customer {self.name} is in {self.state}>'


    def next_state(self):
        """
        Propagates the customer to the next state. 
        Returns nothing.
        """
        self.state = random.choices(['entrance', 'dairy', 'drinks', 'fruit', 'spices', 'checkout'], weights=self.transition_probs.loc[f'{self.state}'])[0]
        # print(self.state[0])


    def is_active(self):
        """
        Returns True if the customer has not reached the checkout yet. 
        """
        if self.state == 'checkout':
            active = False
        else:
            active = True

        return active
        print(is_active)
    

    @property
    def total_store_minutes(self):
        return 1