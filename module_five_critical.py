months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def main():
    # Get the number of years
    num_years = int(input("Enter the number of years: "))

    total_rainfall = 0
    total_months = num_years * 12

    # Outer loop for each year
    for year in range(1, num_years + 1):
        print(f"\nYear {year}")
        
        # Inner loop for each month
        for month in range(0, 12):
            while True:
                try:
                    rainfall = float(input(f"Enter the inches of rainfall for month {months[month]}: "))
                    if rainfall < 0:
                        raise ValueError("Rainfall cannot be negative.")
                    total_rainfall += rainfall
                    break
                except ValueError as e:
                    print(f"Invalid input: {e}. Please try again.")

    # Calculate average rainfall
    average_rainfall = total_rainfall / total_months

    # Display the results
    print("\nRainfall Data Summary")
    print(f"Total months: {total_months}")
    print(f"Total inches of rainfall: {total_rainfall:.2f}")
    print(f"Average rainfall per month: {average_rainfall:.2f}")

if __name__ == "__main__":
    main()
