
# Kinetic model

def live_energy_calculator():
    volume = float(input("Enter Volume: "))
    open_price = float(input("Enter Open Price: "))
    close_price = float(input("Enter Close Price: "))
    delta_t = float(input("Enter Delta Time (in minutes): "))

    delta_p = abs(close_price - open_price)
    velocity = delta_p / delta_t
    energy = 0.5 * volume * (velocity ** 2)

    print("\nLive Energy (QEU):", energy)


live_energy_calculator()


# storage

def range_energy_calculator():
    n = int(input("Enter number of candles in range: "))
    total_energy = 0.0

    for i in range(n):
        print(f"\nCandle {i+1}")
        volume = float(input("Volume: "))
        open_price = float(input("Open Price: "))
        close_price = float(input("Close Price: "))
        delta_t = float(input("Delta Time (minutes): "))

        delta_p = abs(close_price - open_price)
        velocity = delta_p / delta_t
        energy = 0.5 * volume * (velocity ** 2)

        total_energy += energy

    print("\nTotal Range Energy (QEU):", total_energy)


range_energy_calculator()


# potential model

def rest_energy_calculator():
    compression_energy = float(input("Enter Compression Energy: "))
    breakout_energy = float(input("Enter Breakout Energy: "))

    rest_energy = compression_energy - breakout_energy

    print("\nRest Energy (QEU):", rest_energy)


rest_energy_calculator()
