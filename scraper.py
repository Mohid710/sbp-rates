from datetime import date

# Function to build KIBOR data
def get_kibor_data(rates):
    data = {
        "baseRate": 22.00,  # update manually if needed
        "kibor1M": rates.get("1Month"),
        "kibor3M": rates.get("3Month"),
        "kibor6M": rates.get("6Month"),
        "kibor12M": rates.get("12Month"),
        "lastUpdated": str(date.today())
    }
    return data


# Function to calculate interest
def calculate_interest(principal, months, rate_percent):
    monthly_rate = (rate_percent / 100) / 12   # convert annual % to monthly decimal
    interest = principal * monthly_rate * months
    total_payment = principal + interest
    return interest, total_payment


# Example test (you can remove this later)
if __name__ == "__main__":
    # Example rates
    rates = {"1Month": 22.0, "3Month": 21.5, "6Month": 21.75, "12Month": 21.9}
    
    data = get_kibor_data(rates)
    interest, total = calculate_interest(100000, 6, data["kibor1M"])
    
    print("Interest:", interest)
    print("Total Payment:", total)
