import json

class HotelDataAnalysis:
    def __init__(self, json_file_path):
        with open(json_file_path, "r") as file:
            self.data = json.load(file)

    def find_cheapest_price(self):
        cheapest_price = float('inf')
        cheapest_room_type = ""
        for room_type, price in self.data["assignment_results"][0]["shown_price"].items():
            current_price = float(price)
            if current_price < cheapest_price:
                cheapest_price = current_price
                cheapest_room_type = room_type
        return cheapest_price, cheapest_room_type

    def calculate_total_prices(self):
        total_prices = {}
        for room_type, net_price in self.data["assignment_results"][0]["net_price"].items():
            taxes = json.loads(self.data["assignment_results"][0]["ext_data"]["taxes"])
            total_price = float(net_price) + float(taxes.get("TAX", 0)) + float(taxes.get("City tax", 0))
            total_prices[room_type] = total_price
        return total_prices

    def write_output_to_file(self, output_file_path, cheapest_price, cheapest_room_type, number_of_guests, total_prices):
        with open(output_file_path, "w") as output_file:
            output_file.write(f"Cheapest Shown Price: {cheapest_price} USD\n")
            output_file.write(f"Room Type: {cheapest_room_type}\n")
            output_file.write(f"Number of Guests: {number_of_guests}\n\n")
            output_file.write("Total Prices:\n")
            for room_type, total_price in total_prices.items():
                output_file.write(f"Room Type: {room_type}, Total Price: {total_price:.2f} USD\n")

    def process_data(self, output_file_path):
        cheapest_price, cheapest_room_type = self.find_cheapest_price()
        number_of_guests = self.data["assignment_results"][0]["number_of_guests"]
        total_prices = self.calculate_total_prices()
        self.write_output_to_file(output_file_path, cheapest_price, cheapest_room_type, number_of_guests, total_prices)

        print(f"Output written to {output_file_path}")



hotel_data_analysis = HotelDataAnalysis("python_task.json")
output_file_path = "output.txt"
hotel_data_analysis.process_data(output_file_path)
 