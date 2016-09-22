from Prac08.car import Taxi, SilverServiceTaxi

taxi = Taxi("Prius 1", 100, 1.20)
taxi.start_fare()
taxi.drive(30)
taxi.get_fare()
print(taxi)

hummer = SilverServiceTaxi("Jimbo's Hummer", 200, 4.80, 2)
hummer.start_fare()
hummer.drive(10)
hummer.get_fare()
print(hummer)
