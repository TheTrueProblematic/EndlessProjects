
# Hello there! This is a Python script designed to simulate a queue with arrivals and service times!
# It's like standing in line at a grocery store but without the long waits and accidental sneezes!
# Exciting, right? Let's get started!

# No worries about ports or platforms, as our beautiful little script is Python-only and compatible with CLI on every system.

# We're starting off by importing the random module,
# the only companion we need in our solitude (since we can't access the internet or use APIs, oh the horror!)
import random

class Customer:
    # Our Customer class will represent both the arrival and departure of a customer.
    def __init__(self, arrival_time, service_start_time, service_time):
        self.arrival_time = arrival_time
        self.service_start_time = service_start_time
        self.service_time = service_time
        self.wait = self.service_start_time - self.arrival_time

def queue_simulation(num_of_cust, arr_interval, serv_time):
    # Let the customer arrivals begin!

    # Create an empty list to store our customers and their respective times.
    customers = []

    # Let's generate our customers!
    for i in range(num_of_cust):

        # No cutting the line here - each customer arrives sequentially after the random interval.
        if i == 0:
            arrival_time = arr_interval[i]
            service_start_time = arrival_time
        else:
            arrival_time += arr_interval[i]
            service_start_time = max(arrival_time, customers[i-1].service_start_time + customers[i-1].service_time)

        # Now we'll create our customer and join them to the queue (our list).
        customers.append(Customer(arrival_time, service_start_time, serv_time[i]))

    # The people must know! We'll print the average wait time after all customers have been created.
    avg_wait_time = sum([customer.wait for customer in customers]) / len(customers)
    print(f"The average wait time is: {avg_wait_time}")
    

# Now let's generate some random arrival intervals and service times
number_of_customers = 100
arrival_intervals = [random.expovariate(1.0) for _ in range(number_of_customers)]
service_times = [random.expovariate(1.0) for _ in range(number_of_customers)]

# And finally - call the function with our generated times
queue_simulation(number_of_customers, arrival_intervals, service_times)

# And there you have it! A command-line, Python-only queue simulation!
# Thanks for joining me on this Pythonic adventure, hope you enjoyed as much as I did!

