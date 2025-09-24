
# Hiya, fellow code enthusiast! :) Welcome to our little LogFileAnalyzer program.
# What's this snazzy program? Glad you asked! It's a simple python script designed to summarize error counts by type from a log file- Nifty, right?
# It's all command-line based (so no GUIs here, my friend), and it works right off the bat with a fresh install of python - no dependencies, no internet, no hassle.

# First off- let's do our imports (just good ol' built-in python stuff)
import sys
import re

def main():
    # Now let's check if a log file was provided as an argument to our script
    if len(sys.argv) != 2:
        print("Usage: python LogFileAnalyzer.py [log_file]")
        sys.exit(1)
        
    # Great! We have a log file to analyze. Let's fetch that name
    log_file = sys.argv[1]
    
    # We'll create a dictionary to keep count of each type of error
    error_counts = {}

    try:
        # Okay, here comes the fun part! Open up that log file.
        with open(log_file, "r") as file:
            
            # Let's read through each line one by one
            for line in file:
                # We'll assume that error types always follow the pattern "ERROR: [error_type] -"
                match = re.search("ERROR: (.+) -", line)
                
                if match:
                    # If we found an error, increment its count in the dictionary
                    error_type = match.group(1)
                    
                    if error_type in error_counts:
                        error_counts[error_type] += 1
                    else:
                        error_counts[error_type] = 1
        # That's it! Our summarization is complete. Let's print out those results!
        print("\n--- Error Counts ---")

        for error_type, count in error_counts.items():
            print(f"{error_type}: {count}")
    except Exception as e:
        print(f"Oops, an error occurred: {e}")
        sys.exit(1)
        
if __name__ == "__main__":
    # If the script is run directly, start the analysis
    main()
