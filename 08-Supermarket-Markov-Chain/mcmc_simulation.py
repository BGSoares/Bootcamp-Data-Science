import pandas as pd
from Store import Supermarket
import time
trans_matrix_loc = '/Users/brunnogorgulhosoares/OneDrive/spiced/random-forest-fennel-student-code/08-Supermarket-Markov-Chain/data/trans_matrix.csv'
trans_matrix = pd.read_csv(trans_matrix_loc, index_col=0)

coop = Supermarket(trans_matrix)

timestep = 1
max_timestep = 20

while timestep <= max_timestep:

    coop.minutes = timestep

    coop.next_minute() # propagates all customers to their next states

    coop.remove_exiting_customers()

    coop.add_new_customers()

    coop.print_customers()

    # if timestep < max_timestep:
    #     time.sleep(max_timestep)

    timestep += 1

