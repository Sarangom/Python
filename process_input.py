import sys

def process_input():
    """
    Reads an integer and a string from standard input, processes them 
    according to the output format, and prints the result to standard output.
    """
    try:
        # Read the first line from standard input
        line1 = sys.stdin.readline()
        if not line1:
            return
        # Convert the first line to an integer N
        N = int(line1)
        
        # Read the second line from standard input
        line2 = sys.stdin.readline()
        if not line2:
            return
        # Remove any trailing newline characters from the string S
        S = line2.rstrip('\r\n')
        
        # Process the integer N to get the result for the first output line
        result_N = N * 2
        
        # Print the first line of the output
        print(result_N)
        # Print the second line of the output
        print(S)
        
    except ValueError:
        # Handle cases where the input is not in the expected format
        print("Invalid input format. Please provide an integer followed by a string.")
    except EOFError:
        # Handle cases where the input ends unexpectedly
        print("End of input reached unexpectedly.")

if __name__ == "__main__":
    process_input()
