def calculate_roi(investment, returns):
    Rentableof investment
    if investment <= 0:
        raise ValueError("Investment must be above 0")
    
    roi = ((returns - investment) / investment) * 100
    return round(roi, 2)


if __name__ == "__main__":
    # Приклад використання
    try:
        inv = 1000
        ret = 1200
        print(f"ROI for investment {inv} with profit {ret} is {calculate_roi(inv, ret)}%")
    except ValueError as e:
        print(f"Помилка: {e}")
