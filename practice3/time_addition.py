# Time addition program
def add_times(*times):
    total_seconds = 0
    for time_str in times:
        minutes, seconds = map(int, time_str.split(':'))
        total_seconds += minutes * 60 + seconds
    
    total_minutes, remaining_seconds = divmod(total_seconds, 60)
    return f"{total_minutes:02d}:{remaining_seconds:02d}"

def main():
    print("Enter times in the format mm:ss separated by spaces:")
    input_times = input("Example: 1:20 3:45 2:30\n").split()
    
    result = add_times(*input_times)
    print("Total time:", result)

if __name__ == "__main__":
    main()
