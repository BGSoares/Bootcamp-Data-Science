import pandas as pd
from Store import Supermarket
import numpy as np

trans_matrix_file = '/Users/brunnogorgulhosoares/OneDrive/spiced/random-forest-fennel-student-code/08-Supermarket-Markov-Chain/data/trans_matrix.csv'
save_result_dir = '/Users/brunnogorgulhosoares/OneDrive/spiced/random-forest-fennel-student-code/08-Supermarket-Markov-Chain/data/'
trans_matrix = pd.read_csv(trans_matrix_file, index_col=0)

coop = Supermarket(trans_matrix)

def simulate_supermarket(supermarket, max_timestep=900):

    result_matrix = np.empty(shape=(0,3))
    timestep = 1

    while timestep <= max_timestep:

        supermarket.minutes = timestep

        supermarket.next_minute() # propagates all customers to their next states

        supermarket.remove_exiting_customers()

        supermarket.add_new_customers()

        # supermarket.print_customers()

        current_rows = supermarket.return_customers()

        result_matrix = np.concatenate((result_matrix, current_rows), axis=0)
        
        timestep += 1
    
    return result_matrix

result_csv = pd.DataFrame(simulate_supermarket(coop), columns=['timestamp', 'customer_no', 'location'])
result_csv.to_csv(f'{save_result_dir}result.csv')