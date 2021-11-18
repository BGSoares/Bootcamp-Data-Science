"""
Start with this to implement the supermarket simulator.
"""

import numpy as np
import pandas as pd
from Customer import Customer


class Supermarket:
    """manages multiple Customer instances that are currently in the market.
    """

    def __init__(self, transition_matrix):        
        # a list of Customer objects
        self.customers = []
        self.minutes = 0
        self.last_id = 0
        self.transition_matrix = transition_matrix


    def __repr__(self):
        return f'At {self.minutes} minutes into the simulation, Coop has {len(self.customers)} customers in it'


    def get_time(self):
        """current time in HH:MM format,
        """
        return '{:02d}:{:02d}'.format(*divmod(self.minutes, 60))



    def print_customers(self):
        """print all customers with the current time and id in CSV format.
        """
        for customer in self.customers:
            print(f'{self.get_time()},{customer.name},{customer.state}')


    def next_minute(self):
        """propagates all customers to the next state.
        """
        for customer in self.customers:
            customer.next_state()
    

    def add_new_customers(self):
        """randomly creates new customers.
        """
        for n in range(1,2):
            new_customer = Customer(name=self.last_id + n, state='entrance', transition_probs=self.transition_matrix)
            self.customers.append(new_customer)
            self.last_id += 1


    def remove_exiting_customers(self):
        """removes every customer that is not active any more.
        """
        for customer in self.customers:
            customer.is_active()
            if customer.is_active() == False:
                self.customers.remove(customer)
            else:
                continue
