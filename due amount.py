def main():
    total = 2.55
    paid = 4.00
    change = paid - total
    print(f"The shopkeeper should return ₹{change:.2f} to Vishal." if change >= 0
          else f"Vishal still owes ₹{abs(change):.2f}")

if __name__ == "__main__":
    main()
