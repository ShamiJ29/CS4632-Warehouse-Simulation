class MetricsCollector:
    def __init__(self):

        #initialize the metrics collector to track order fulfillment times

        #attributes : fulfillment_times(list) : Stores the total fulfillment time
        # for each completed order
        self.fulfillment_times = []

    def record_order(self, order, current_time):
        #Records the fulfillment time for a completed order

        #parameters : order (Order) : The completed order to record
        # current_time (float) : The simulation time when the order was completed
        self.fulfillment_times.append(order.completion_time - order.arrival_time)

    def report(self):
            #Generates a summary report of the simulation metrics
        if self.fulfillment_times:
            avg_time = sum(self.fulfillment_times) / len(self.fulfillment_times)
            print(f"Orders completed: {len(self.fulfillment_times)}")
            print(f"Average fulfillment time: {avg_time:.2f} minutes")