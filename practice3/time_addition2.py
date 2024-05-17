class TimeAdder:
    def __init__(self):
        self.total_seconds = 0

    def add_times(self, *times):
        for time_str in times:
            time_parts = list(map(int, time_str.split(':')))
            
            if len(time_parts) == 2:  # mm:ss format
                minutes, seconds = time_parts
                hours = 0
            elif len(time_parts) == 3:  # hh:mm:ss format
                hours, minutes, seconds = time_parts
            else:
                raise ValueError(f"Invalid time format: {time_str}")
            
            self.total_seconds += hours * 3600 + minutes * 60 + seconds

        return self.format_time(self.total_seconds)

    def format_time(self, total_seconds):
        total_hours, remaining_seconds = divmod(total_seconds, 3600)
        total_minutes, remaining_seconds = divmod(remaining_seconds, 60)
        return f"{total_hours:02d}:{total_minutes:02d}:{remaining_seconds:02d}"

def main():
    print("Enter times in the format hh:mm:ss or mm:ss separated by a custom separator:")
    separator = input("Enter the separator (default is space): ").strip() or ' '
    
    input_times = input(f"Example: 1:20 3:45 2:30 (using '{separator}' as separator)\n").split(separator)
    
    time_adder = TimeAdder()
    try:
        result = time_adder.add_times(*input_times)
        print("Total time:", result)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
