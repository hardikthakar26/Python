"""
Simple Calculator Program
A command-line calculator that performs basic arithmetic operations:
addition, subtraction, multiplication, and division.
"""

import math
import sys

class SimpleCalculator:
    """
    A simple calculator class that handles basic arithmetic operations
    and maintains calculation history.
    """
    
    def __init__(self):
        """Initialize calculator with empty history and default settings."""
        self.history = []
        self.current_result = 0
        self.is_new_calculation = True
    
    def display_menu(self):
        """
        Display the main calculator menu with available operations.
        """
        print("\n" + "="*50)
        print("            SIMPLE CALCULATOR")
        print("="*50)
        print("Available Operations:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Power (^)")
        print("6. Square Root (√)")
        print("7. Show Calculation History")
        print("8. Clear History")
        print("9. Exit")
        print("="*50)
    
    def get_number_input(self, prompt="Enter a number: "):
        """
        Get and validate numeric input from user.
        
        Args:
            prompt (str): The prompt to display to user
            
        Returns:
            float: Validated numeric input from user
        """
        while True:
            try:
                value = input(prompt)
                
                # Allow using current result as input
                if value.lower() == 'ans':
                    return self.current_result
                
                # Convert to float
                return float(value)
            except ValueError:
                print("❌ Invalid input! Please enter a valid number or 'ans' for previous result.")
    
    def get_operation_choice(self):
        """
        Get and validate user's operation choice.
        
        Returns:
            int: Validated operation choice (1-9)
        """
        while True:
            try:
                choice = int(input("Select operation (1-9): "))
                if 1 <= choice <= 9:
                    return choice
                else:
                    print("❌ Please enter a number between 1 and 9.")
            except ValueError:
                print("❌ Invalid input! Please enter a number between 1 and 9.")
    
    def add(self, a, b):
        """
        Perform addition of two numbers.
        
        Args:
            a (float): First number
            b (float): Second number
            
        Returns:
            float: Result of a + b
        """
        return a + b
    
    def subtract(self, a, b):
        """
        Perform subtraction of two numbers.
        
        Args:
            a (float): First number
            b (float): Second number
            
        Returns:
            float: Result of a - b
        """
        return a - b
    
    def multiply(self, a, b):
        """
        Perform multiplication of two numbers.
        
        Args:
            a (float): First number
            b (float): Second number
            
        Returns:
            float: Result of a * b
        """
        return a * b
    
    def divide(self, a, b):
        """
        Perform division of two numbers with zero division check.
        
        Args:
            a (float): Numerator
            b (float): Denominator
            
        Returns:
            float: Result of a / b
            
        Raises:
            ZeroDivisionError: If denominator is zero
        """
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed!")
        return a / b
    
    def power(self, base, exponent):
        """
        Calculate base raised to the power of exponent.
        
        Args:
            base (float): The base number
            exponent (float): The exponent
            
        Returns:
            float: Result of base^exponent
        """
        return math.pow(base, exponent)
    
    def square_root(self, number):
        """
        Calculate square root of a number with validation.
        
        Args:
            number (float): The number to find square root of
            
        Returns:
            float: Square root of the number
            
        Raises:
            ValueError: If number is negative
        """
        if number < 0:
            raise ValueError("Cannot calculate square root of a negative number!")
        return math.sqrt(number)
    
    def format_result(self, result):
        """
        Format the result for display, handling large numbers and decimals.
        
        Args:
            result (float): The result to format
            
        Returns:
            str: Formatted result string
        """
        if result == int(result):
            return str(int(result))
        else:
            # Limit to 6 decimal places for readability
            return f"{result:.6f}".rstrip('0').rstrip('.')
    
    def add_to_history(self, operation, operands, result):
        """
        Add a calculation to the history.
        
        Args:
            operation (str): Description of the operation
            operands (list): List of operands used
            result (float): The result of the calculation
        """
        history_entry = {
            'operation': operation,
            'operands': operands,
            'result': result,
            'timestamp': self.get_current_time()
        }
        self.history.append(history_entry)
    
    def get_current_time(self):
        """
        Get current time in a formatted string.
        
        Returns:
            str: Formatted current time
        """
        from datetime import datetime
        return datetime.now().strftime("%H:%M:%S")
    
    def show_history(self):
        """
        Display the calculation history.
        """
        if not self.history:
            print("\nNo calculations in history.")
            return
        
        print("\n" + "="*60)
        print("                  CALCULATION HISTORY")
        print("="*60)
        print(f"{'Time':<10} {'Operation':<25} {'Result':<15}")
        print("-"*60)
        
        for entry in self.history:
            # Format the operation display
            if entry['operation'] == 'Square Root':
                op_display = f"√{entry['operands'][0]}"
            elif entry['operation'] == 'Power':
                op_display = f"{entry['operands'][0]}^{entry['operands'][1]}"
            else:
                op_display = f"{entry['operands'][0]} {self.get_operator_symbol(entry['operation'])} {entry['operands'][1]}"
            
            print(f"{entry['timestamp']:<10} {op_display:<25} {self.format_result(entry['result']):<15}")
    
    def get_operator_symbol(self, operation):
        """
        Get the symbol for an operation.
        
        Args:
            operation (str): The operation name
            
        Returns:
            str: Symbol for the operation
        """
        symbols = {
            'Addition': '+',
            'Subtraction': '-',
            'Multiplication': '*',
            'Division': '/',
            'Power': '^'
        }
        return symbols.get(operation, '?')
    
    def clear_history(self):
        """
        Clear the calculation history.
        """
        self.history.clear()
        print("\n✅ Calculation history cleared!")
    
    def perform_calculation(self, choice):
        """
        Perform the calculation based on user's choice.
        
        Args:
            choice (int): The operation choice from menu
        """
        try:
            if choice == 1:  # Addition
                if self.is_new_calculation:
                    num1 = self.get_number_input("Enter first number: ")
                else:
                    num1 = self.current_result
                    print(f"Using previous result: {self.format_result(num1)}")
                
                num2 = self.get_number_input("Enter second number: ")
                result = self.add(num1, num2)
                operation = "Addition"
                operands = [num1, num2]
                
            elif choice == 2:  # Subtraction
                if self.is_new_calculation:
                    num1 = self.get_number_input("Enter first number: ")
                else:
                    num1 = self.current_result
                    print(f"Using previous result: {self.format_result(num1)}")
                
                num2 = self.get_number_input("Enter second number: ")
                result = self.subtract(num1, num2)
                operation = "Subtraction"
                operands = [num1, num2]
                
            elif choice == 3:  # Multiplication
                if self.is_new_calculation:
                    num1 = self.get_number_input("Enter first number: ")
                else:
                    num1 = self.current_result
                    print(f"Using previous result: {self.format_result(num1)}")
                
                num2 = self.get_number_input("Enter second number: ")
                result = self.multiply(num1, num2)
                operation = "Multiplication"
                operands = [num1, num2]
                
            elif choice == 4:  # Division
                if self.is_new_calculation:
                    num1 = self.get_number_input("Enter numerator: ")
                else:
                    num1 = self.current_result
                    print(f"Using previous result: {self.format_result(num1)}")
                
                num2 = self.get_number_input("Enter denominator: ")
                result = self.divide(num1, num2)
                operation = "Division"
                operands = [num1, num2]
                
            elif choice == 5:  # Power
                if self.is_new_calculation:
                    base = self.get_number_input("Enter base: ")
                else:
                    base = self.current_result
                    print(f"Using previous result: {self.format_result(base)}")
                
                exponent = self.get_number_input("Enter exponent: ")
                result = self.power(base, exponent)
                operation = "Power"
                operands = [base, exponent]
                
            elif choice == 6:  # Square Root
                number = self.get_number_input("Enter number: ")
                result = self.square_root(number)
                operation = "Square Root"
                operands = [number]
                
            else:
                return
            
            # Display result
            self.display_result(operation, operands, result)
            
            # Update calculator state
            self.current_result = result
            self.is_new_calculation = False
            self.add_to_history(operation, operands, result)
            
        except ZeroDivisionError as e:
            print(f"❌ Error: {e}")
        except ValueError as e:
            print(f"❌ Error: {e}")
        except OverflowError:
            print("❌ Error: Result is too large!")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
    
    def display_result(self, operation, operands, result):
        """
        Display the calculation result in a formatted way.
        
        Args:
            operation (str): The operation performed
            operands (list): List of operands used
            result (float): The calculation result
        """
        print("\n" + "="*40)
        print("          CALCULATION RESULT")
        print("="*40)
        
        if operation == "Square Root":
            print(f"Operation: √{operands[0]}")
        elif operation == "Power":
            print(f"Operation: {operands[0]}^{operands[1]}")
        else:
            operator = self.get_operator_symbol(operation)
            print(f"Operation: {operands[0]} {operator} {operands[1]}")
        
        print(f"Result: {self.format_result(result)}")
        print("="*40)
    
    def run(self):
        """
        Main method to run the calculator program.
        Handles the main loop and user interaction.
        """
        print("🚀 Welcome to the Simple Calculator!")
        print("💡 Tip: You can use 'ans' to use the previous result in your next calculation.")
        
        while True:
            self.display_menu()
            
            try:
                choice = self.get_operation_choice()
                
                if choice == 7:  # Show History
                    self.show_history()
                    continue
                elif choice == 8:  # Clear History
                    self.clear_history()
                    continue
                elif choice == 9:  # Exit
                    print("\n👋 Thank you for using the Simple Calculator! Goodbye!")
                    sys.exit()
                
                # Perform calculation for choices 1-6
                self.perform_calculation(choice)
                
                # Ask if user wants to continue with result
                if not self.is_new_calculation:
                    continue_choice = input("\nDo you want to perform another operation with this result? (y/n): ").lower()
                    if continue_choice != 'y':
                        self.is_new_calculation = True
                        reset_choice = input("Do you want to reset calculator? (y/n): ").lower()
                        if reset_choice == 'y':
                            self.current_result = 0
                        
            except KeyboardInterrupt:
                print("\n\n⚠️  Program interrupted by user. Exiting...")
                sys.exit()
            except Exception as e:
                print(f"\n❌ An unexpected error occurred: {e}")
                print("Please try again.")

# Main execution
if __name__ == "__main__":
    """
    Program entry point.
    Creates a calculator instance and starts the program.
    """
    try:
        calculator = SimpleCalculator()
        calculator.run()
    except Exception as e:
        print(f"Failed to start calculator: {e}")
        sys.exit(1)