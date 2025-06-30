class DateCalculator:
    def __init__(self, year, month, day):
        # Adjust for January and February
        if month < 3:
            month += 12
            year -= 1
        self.day = day
        self.month = month
        self.year = year

    def calculate_day_of_week(self):
        q = self.day
        m = self.month
        K = self.year % 100
        J = self.year // 100

        h = (q + (13 * (m + 1)) // 5 + K + (K // 4) + (J // 4) + (5 * J)) % 7
        return h

    def get_day_name(self):
        days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        return days[self.calculate_day_of_week()]


# Example usage
if __name__ == "__main__":
    date = DateCalculator(2025, 5, 5)  # May 5, 2025
    print("The day of the week is:", date.get_day_name())
