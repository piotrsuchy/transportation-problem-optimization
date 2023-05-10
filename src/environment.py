'''
First draft:
This Environment class represents the transportation problem as a Markov decision process (MDP). 
The state is represented by the truck positions and remaining orders/deadlines,
the actions are represented by the possible moves of each truck, 
and the rewards are given by successful deliveries and missed deadlines.

The step() method applies an action to the environment, 
updating the state and returning a new state, reward,
and a boolean indicating whether the episode is done.
'''
class Environment:
    def __init__(self, n_trucks, vertices, orders, deadlines):
        # Initialize the state
        self.truck_positions = [0] * n_trucks  # assuming all trucks start at position 0
        self.remaining_orders = orders  # list of orders yet to be delivered
        self.remaining_deadlines = deadlines  # corresponding deadlines for the orders

        # Define the set of possible actions
        # For simplicity, we assume that each truck can move to any vertex
        self.actions = [(i, v) for i in range(n_trucks) for v in vertices]

    def step(self, action):
        # Apply the action (move a truck to a new vertex)
        truck, vertex = action
        self.truck_positions[truck] = vertex

        # Check if any orders can be delivered
        delivered_orders = [o for o in self.remaining_orders if o['vertex'] == vertex and o['truck'] == truck]
        for order in delivered_orders:
            self.remaining_orders.remove(order)

        # Calculate the reward
        reward = len(delivered_orders)  # positive reward for each delivery
        overdue_orders = [o for o in self.remaining_orders if o['deadline'] < 0]
        reward -= len(overdue_orders)  # negative reward for each overdue order

        # Update the deadlines
        for order in self.remaining_orders:
            order['deadline'] -= 1

        return self.get_state(), reward, self.is_done()

    def get_state(self):
        # The state representation will depend on your specific problem
        # For this example, we'll just return the raw data
        return {
            'truck_positions': self.truck_positions,
            'remaining_orders': self.remaining_orders,
            'remaining_deadlines': self.remaining_deadlines,
        }

    def is_done(self):
        # The episode ends when all orders have been delivered or all deadlines have passed
        return not self.remaining_orders or all(o['deadline'] < 0 for o in self.remaining_orders)
