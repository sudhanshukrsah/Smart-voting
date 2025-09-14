#!/usr/bin/env python3
"""
Daily Java Code Generator
Generates a new Java file with a programming problem and solution each day.
Ensures code looks natural and human-written.
"""

import os
import random
from datetime import datetime
import hashlib

class JavaCodeGenerator:
    def __init__(self):
        self.base_path = "java-daily-challenges"
        self.problems = [
            {
                "name": "PalindromeChecker",
                "description": "Check if a given string is a palindrome",
                "template": """
/**
 * PalindromeChecker - A utility class to check if strings are palindromes
 * Author: Daily Code Challenge
 * Date: {date}
 */

public class PalindromeChecker {{
    
    /**
     * Checks if a given string is a palindrome (reads same forwards and backwards)
     * @param str the string to check
     * @return true if string is palindrome, false otherwise
     */
    public static boolean isPalindrome(String str) {{
        // Handle null or empty strings
        if (str == null || str.length() == 0) {{
            return true;
        }}
        
        // Convert to lowercase and remove spaces for comparison
        String cleaned = str.toLowerCase().replaceAll("\\\\s+", "");
        
        int left = 0;
        int right = cleaned.length() - 1;
        
        // Check characters from both ends moving inward
        while (left < right) {{
            if (cleaned.charAt(left) != cleaned.charAt(right)) {{
                return false;
            }}
            left++;
            right--;
        }}
        
        return true;
    }}
    
    /**
     * Main method to test the palindrome checker
     */
    public static void main(String[] args) {{
        // Test cases
        String[] testStrings = {{
            "racecar",
            "A man a plan a canal Panama",
            "race a car",
            "hello world",
            "Madam"
        }};
        
        System.out.println("=== Palindrome Checker Test ===");
        
        for (String test : testStrings) {{
            boolean result = isPalindrome(test);
            System.out.printf("'%s' -> %s%n", test, result ? "Palindrome" : "Not a palindrome");
        }}
    }}
}}
"""
            },
            {
                "name": "FibonacciSequence",
                "description": "Generate Fibonacci sequence up to n terms",
                "template": """
/**
 * FibonacciSequence - Generate and display Fibonacci numbers
 * Author: Daily Code Challenge
 * Date: {date}
 */

public class FibonacciSequence {{
    
    /**
     * Generates Fibonacci sequence up to n terms
     * @param n number of terms to generate
     */
    public static void generateFibonacci(int n) {{
        if (n <= 0) {{
            System.out.println("Please enter a positive number");
            return;
        }}
        
        long first = 0, second = 1;
        
        System.out.println("Fibonacci Sequence:");
        
        if (n >= 1) {{
            System.out.print(first + " ");
        }}
        if (n >= 2) {{
            System.out.print(second + " ");
        }}
        
        // Generate remaining terms
        for (int i = 3; i <= n; i++) {{
            long next = first + second;
            System.out.print(next + " ");
            
            // Update for next iteration
            first = second;
            second = next;
        }}
        System.out.println(); // New line after sequence
    }}
    
    /**
     * Calculates nth Fibonacci number using recursion
     * @param n position in sequence
     * @return nth Fibonacci number
     */
    public static long fibonacciRecursive(int n) {{
        if (n <= 1) {{
            return n;
        }}
        return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2);
    }}
    
    /**
     * Main method to demonstrate Fibonacci generation
     */
    public static void main(String[] args) {{
        int terms = 15;
        
        System.out.println("=== Fibonacci Sequence Generator ===");
        System.out.println("Generating first " + terms + " terms:");
        
        generateFibonacci(terms);
        
        System.out.println("\\nUsing recursive method:");
        System.out.print("First 10 terms: ");
        for (int i = 0; i < 10; i++) {{
            System.out.print(fibonacciRecursive(i) + " ");
        }}
        System.out.println();
    }}
}}
"""
            },
            {
                "name": "PrimeNumberChecker",
                "description": "Check if a number is prime and find prime numbers in a range",
                "template": """
/**
 * PrimeNumberChecker - Utility for working with prime numbers
 * Author: Daily Code Challenge
 * Date: {date}
 */

public class PrimeNumberChecker {{
    
    /**
     * Checks if a given number is prime
     * @param number the number to check
     * @return true if number is prime, false otherwise
     */
    public static boolean isPrime(int number) {{
        // Handle edge cases
        if (number <= 1) {{
            return false;
        }}
        if (number <= 3) {{
            return true;
        }}
        if (number % 2 == 0 || number % 3 == 0) {{
            return false;
        }}
        
        // Check for divisors from 5 to sqrt(number)
        for (int i = 5; i * i <= number; i += 6) {{
            if (number % i == 0 || number % (i + 2) == 0) {{
                return false;
            }}
        }}
        
        return true;
    }}
    
    /**
     * Finds all prime numbers in a given range
     * @param start starting number (inclusive)
     * @param end ending number (inclusive)
     */
    public static void findPrimesInRange(int start, int end) {{
        System.out.println("Prime numbers between " + start + " and " + end + ":");
        
        boolean foundPrime = false;
        for (int i = start; i <= end; i++) {{
            if (isPrime(i)) {{
                System.out.print(i + " ");
                foundPrime = true;
            }}
        }}
        
        if (!foundPrime) {{
            System.out.print("No prime numbers found in this range");
        }}
        System.out.println();
    }}
    
    /**
     * Main method to test prime number functionality
     */
    public static void main(String[] args) {{
        System.out.println("=== Prime Number Checker ===");
        
        // Test individual numbers
        int[] testNumbers = {{17, 25, 29, 100, 97}};
        
        System.out.println("Testing individual numbers:");
        for (int num : testNumbers) {{
            System.out.printf("%d is %s%n", num, isPrime(num) ? "prime" : "not prime");
        }}
        
        System.out.println();
        
        // Find primes in range
        findPrimesInRange(1, 50);
        findPrimesInRange(50, 100);
    }}
}}
"""
            },
            {
                "name": "StringReverser",
                "description": "Various methods to reverse strings and words",
                "template": """
/**
 * StringReverser - Different approaches to reverse strings
 * Author: Daily Code Challenge
 * Date: {date}
 */

public class StringReverser {{
    
    /**
     * Reverses a string using StringBuilder
     * @param str the string to reverse
     * @return reversed string
     */
    public static String reverseUsingStringBuilder(String str) {{
        if (str == null) {{
            return null;
        }}
        return new StringBuilder(str).reverse().toString();
    }}
    
    /**
     * Reverses a string using character array
     * @param str the string to reverse
     * @return reversed string
     */
    public static String reverseUsingCharArray(String str) {{
        if (str == null) {{
            return null;
        }}
        
        char[] chars = str.toCharArray();
        int left = 0;
        int right = chars.length - 1;
        
        // Swap characters from both ends
        while (left < right) {{
            char temp = chars[left];
            chars[left] = chars[right];
            chars[right] = temp;
            left++;
            right--;
        }}
        
        return new String(chars);
    }}
    
    /**
     * Reverses words in a sentence while keeping word order
     * @param sentence the sentence to process
     * @return sentence with reversed words
     */
    public static String reverseWordsOnly(String sentence) {{
        if (sentence == null || sentence.trim().isEmpty()) {{
            return sentence;
        }}
        
        String[] words = sentence.split(" ");
        StringBuilder result = new StringBuilder();
        
        for (int i = 0; i < words.length; i++) {{
            if (i > 0) {{
                result.append(" ");
            }}
            result.append(reverseUsingStringBuilder(words[i]));
        }}
        
        return result.toString();
    }}
    
    /**
     * Main method to demonstrate string reversal techniques
     */
    public static void main(String[] args) {{
        System.out.println("=== String Reverser Demo ===");
        
        String[] testStrings = {{
            "Hello World",
            "Java Programming",
            "Reverse This String",
            "12345"
        }};
        
        for (String test : testStrings) {{
            System.out.println("\\nOriginal: " + test);
            System.out.println("Reversed (StringBuilder): " + reverseUsingStringBuilder(test));
            System.out.println("Reversed (Char Array): " + reverseUsingCharArray(test));
            System.out.println("Words Reversed: " + reverseWordsOnly(test));
        }}
    }}
}}
"""
            },
            {
                "name": "ArraySorter",
                "description": "Implementation of bubble sort and selection sort algorithms",
                "template": """
/**
 * ArraySorter - Implementation of basic sorting algorithms
 * Author: Daily Code Challenge
 * Date: {date}
 */

import java.util.Arrays;

public class ArraySorter {{
    
    /**
     * Sorts array using bubble sort algorithm
     * @param arr array to sort
     */
    public static void bubbleSort(int[] arr) {{
        int n = arr.length;
        
        for (int i = 0; i < n - 1; i++) {{
            boolean swapped = false;
            
            // Last i elements are already sorted
            for (int j = 0; j < n - i - 1; j++) {{
                if (arr[j] > arr[j + 1]) {{
                    // Swap elements
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    swapped = true;
                }}
            }}
            
            // If no swapping occurred, array is sorted
            if (!swapped) {{
                break;
            }}
        }}
    }}
    
    /**
     * Sorts array using selection sort algorithm
     * @param arr array to sort
     */
    public static void selectionSort(int[] arr) {{
        int n = arr.length;
        
        for (int i = 0; i < n - 1; i++) {{
            // Find minimum element in remaining array
            int minIndex = i;
            for (int j = i + 1; j < n; j++) {{
                if (arr[j] < arr[minIndex]) {{
                    minIndex = j;
                }}
            }}
            
            // Swap minimum element with first element
            int temp = arr[minIndex];
            arr[minIndex] = arr[i];
            arr[i] = temp;
        }}
    }}
    
    /**
     * Utility method to print array
     * @param arr array to print
     * @param title description of the array
     */
    public static void printArray(int[] arr, String title) {{
        System.out.println(title + ": " + Arrays.toString(arr));
    }}
    
    /**
     * Main method to demonstrate sorting algorithms
     */
    public static void main(String[] args) {{
        System.out.println("=== Array Sorting Algorithms ===");
        
        // Test data
        int[] originalArray = {{64, 34, 25, 12, 22, 11, 90}};
        
        // Test bubble sort
        int[] bubbleArray = originalArray.clone();
        printArray(bubbleArray, "Original Array");
        bubbleSort(bubbleArray);
        printArray(bubbleArray, "After Bubble Sort");
        
        System.out.println();
        
        // Test selection sort
        int[] selectionArray = originalArray.clone();
        printArray(selectionArray, "Original Array");
        selectionSort(selectionArray);
        printArray(selectionArray, "After Selection Sort");
    }}
}}
"""
            },
            {
                "name": "NumberGuessingGame",
                "description": "Simple number guessing game with user interaction simulation",
                "template": """
/**
 * NumberGuessingGame - A simple number guessing game implementation
 * Author: Daily Code Challenge
 * Date: {date}
 */

import java.util.Random;
import java.util.Scanner;

public class NumberGuessingGame {{
    
    private static final int MAX_ATTEMPTS = 7;
    private static final int MIN_NUMBER = 1;
    private static final int MAX_NUMBER = 100;
    
    /**
     * Generates a random number within the specified range
     * @return random number between MIN_NUMBER and MAX_NUMBER
     */
    public static int generateRandomNumber() {{
        Random random = new Random();
        return random.nextInt(MAX_NUMBER - MIN_NUMBER + 1) + MIN_NUMBER;
    }}
    
    /**
     * Provides hint based on the guess compared to target
     * @param guess user's guess
     * @param target the target number
     * @return hint string
     */
    public static String getHint(int guess, int target) {{
        if (guess == target) {{
            return "Congratulations! You guessed it right!";
        }} else if (guess < target) {{
            return "Too low! Try a higher number.";
        }} else {{
            return "Too high! Try a lower number.";
        }}
    }}
    
    /**
     * Simulates the number guessing game
     * @param target the number to guess
     */
    public static void simulateGame(int target) {{
        System.out.println("=== Number Guessing Game Simulation ===");
        System.out.printf("I'm thinking of a number between %d and %d%n", MIN_NUMBER, MAX_NUMBER);
        System.out.printf("You have %d attempts to guess it!%n%n", MAX_ATTEMPTS);
        
        // Simulate some guesses for demonstration
        int[] simulatedGuesses = {{50, 75, 62, 68, 65, 67, target}};
        
        for (int attempt = 1; attempt <= MAX_ATTEMPTS; attempt++) {{
            int guess = (attempt <= simulatedGuesses.length) ? 
                       simulatedGuesses[attempt - 1] : target;
                       
            System.out.printf("Attempt %d: Guess = %d%n", attempt, guess);
            String hint = getHint(guess, target);
            System.out.println(hint);
            
            if (guess == target) {{
                System.out.printf("Game won in %d attempts!%n", attempt);
                return;
            }}
            
            System.out.println();
        }}
        
        System.out.printf("Game over! The number was %d%n", target);
    }}
    
    /**
     * Interactive version of the game (commented out for automation)
     */
    public static void playInteractiveGame() {{
        // This method would be used for actual user interaction
        // Scanner scanner = new Scanner(System.in);
        // int target = generateRandomNumber();
        // ... interactive logic would go here
        System.out.println("Interactive game disabled for automation demo");
    }}
    
    /**
     * Main method to demonstrate the number guessing game
     */
    public static void main(String[] args) {{
        // Generate target number
        int targetNumber = generateRandomNumber();
        
        // Simulate game
        simulateGame(targetNumber);
        
        System.out.println("\\n" + "=".repeat(40));
        System.out.println("Game Statistics:");
        System.out.printf("Target number: %d%n", targetNumber);
        System.out.printf("Range: %d - %d%n", MIN_NUMBER, MAX_NUMBER);
        System.out.printf("Max attempts allowed: %d%n", MAX_ATTEMPTS);
    }}
}}
"""
            },
            {
                "name": "TemperatureConverter",
                "description": "Convert temperatures between Celsius, Fahrenheit, and Kelvin",
                "template": """
/**
 * TemperatureConverter - Convert between different temperature scales
 * Author: Daily Code Challenge
 * Date: {date}
 */

public class TemperatureConverter {{
    
    /**
     * Converts Celsius to Fahrenheit
     * @param celsius temperature in Celsius
     * @return temperature in Fahrenheit
     */
    public static double celsiusToFahrenheit(double celsius) {{
        return (celsius * 9.0 / 5.0) + 32.0;
    }}
    
    /**
     * Converts Fahrenheit to Celsius
     * @param fahrenheit temperature in Fahrenheit
     * @return temperature in Celsius
     */
    public static double fahrenheitToCelsius(double fahrenheit) {{
        return (fahrenheit - 32.0) * 5.0 / 9.0;
    }}
    
    /**
     * Converts Celsius to Kelvin
     * @param celsius temperature in Celsius
     * @return temperature in Kelvin
     */
    public static double celsiusToKelvin(double celsius) {{
        return celsius + 273.15;
    }}
    
    /**
     * Converts Kelvin to Celsius
     * @param kelvin temperature in Kelvin
     * @return temperature in Celsius
     */
    public static double kelvinToCelsius(double kelvin) {{
        return kelvin - 273.15;
    }}
    
    /**
     * Converts Fahrenheit to Kelvin
     * @param fahrenheit temperature in Fahrenheit
     * @return temperature in Kelvin
     */
    public static double fahrenheitToKelvin(double fahrenheit) {{
        return celsiusToKelvin(fahrenheitToCelsius(fahrenheit));
    }}
    
    /**
     * Converts Kelvin to Fahrenheit
     * @param kelvin temperature in Kelvin
     * @return temperature in Fahrenheit
     */
    public static double kelvinToFahrenheit(double kelvin) {{
        return celsiusToFahrenheit(kelvinToCelsius(kelvin));
    }}
    
    /**
     * Formats temperature display with proper units
     * @param temp temperature value
     * @param unit temperature unit
     * @return formatted string
     */
    public static String formatTemperature(double temp, String unit) {{
        return String.format("%.2f°%s", temp, unit);
    }}
    
    /**
     * Main method to demonstrate temperature conversions
     */
    public static void main(String[] args) {{
        System.out.println("=== Temperature Converter Demo ===");
        
        // Test temperatures
        double[] testTemps = {{0, 100, 32, 212, -40}};
        
        System.out.println("\\nCelsius to other scales:");
        for (double celsius : testTemps) {{
            double fahrenheit = celsiusToFahrenheit(celsius);
            double kelvin = celsiusToKelvin(celsius);
            
            System.out.printf("%s -> %s -> %s%n",
                formatTemperature(celsius, "C"),
                formatTemperature(fahrenheit, "F"),
                formatTemperature(kelvin, "K"));
        }}
        
        System.out.println("\\nSpecial temperature points:");
        System.out.println("Water freezing point:");
        System.out.printf("  %s = %s = %s%n",
            formatTemperature(0, "C"),
            formatTemperature(32, "F"),
            formatTemperature(273.15, "K"));
            
        System.out.println("Water boiling point:");
        System.out.printf("  %s = %s = %s%n",
            formatTemperature(100, "C"),
            formatTemperature(212, "F"),
            formatTemperature(373.15, "K"));
            
        System.out.println("Absolute zero:");
        System.out.printf("  %s = %s = %s%n",
            formatTemperature(-273.15, "C"),
            formatTemperature(-459.67, "F"),
            formatTemperature(0, "K"));
    }}
}}
"""
            },
            {
                "name": "SimpleCalculator",
                "description": "Basic calculator with arithmetic operations",
                "template": """
/**
 * SimpleCalculator - Perform basic arithmetic operations
 * Author: Daily Code Challenge
 * Date: {date}
 */

public class SimpleCalculator {{
    
    /**
     * Performs addition
     * @param a first number
     * @param b second number
     * @return sum of a and b
     */
    public static double add(double a, double b) {{
        return a + b;
    }}
    
    /**
     * Performs subtraction
     * @param a first number
     * @param b second number
     * @return difference of a and b
     */
    public static double subtract(double a, double b) {{
        return a - b;
    }}
    
    /**
     * Performs multiplication
     * @param a first number
     * @param b second number
     * @return product of a and b
     */
    public static double multiply(double a, double b) {{
        return a * b;
    }}
    
    /**
     * Performs division with error handling
     * @param a dividend
     * @param b divisor
     * @return quotient of a and b
     * @throws ArithmeticException if b is zero
     */
    public static double divide(double a, double b) {{
        if (b == 0) {{
            throw new ArithmeticException("Division by zero is not allowed");
        }}
        return a / b;
    }}
    
    /**
     * Calculates power (a raised to the power of b)
     * @param base the base number
     * @param exponent the exponent
     * @return base raised to the power of exponent
     */
    public static double power(double base, int exponent) {{
        if (exponent == 0) {{
            return 1.0;
        }}
        
        double result = 1.0;
        int absExponent = Math.abs(exponent);
        
        for (int i = 0; i < absExponent; i++) {{
            result *= base;
        }}
        
        return exponent < 0 ? 1.0 / result : result;
    }}
    
    /**
     * Calculates square root
     * @param number the number to find square root of
     * @return square root of the number
     */
    public static double squareRoot(double number) {{
        if (number < 0) {{
            throw new IllegalArgumentException("Square root of negative number is not real");
        }}
        return Math.sqrt(number);
    }}
    
    /**
     * Formats calculation result for display
     * @param operation the operation performed
     * @param operand1 first operand
     * @param operand2 second operand (can be null for unary operations)
     * @param result the result
     */
    public static void displayResult(String operation, double operand1, Double operand2, double result) {{
        if (operand2 != null) {{
            System.out.printf("%.2f %s %.2f = %.2f%n", operand1, operation, operand2, result);
        }} else {{
            System.out.printf("%s(%.2f) = %.2f%n", operation, operand1, result);
        }}
    }}
    
    /**
     * Main method to demonstrate calculator operations
     */
    public static void main(String[] args) {{
        System.out.println("=== Simple Calculator Demo ===");
        
        double a = 15.5;
        double b = 4.2;
        
        System.out.println("Basic arithmetic operations:");
        displayResult("+", a, b, add(a, b));
        displayResult("-", a, b, subtract(a, b));
        displayResult("*", a, b, multiply(a, b));
        displayResult("/", a, b, divide(a, b));
        
        System.out.println("\\nAdvanced operations:");
        displayResult("power", a, 3.0, power(a, 3));
        displayResult("sqrt", a, null, squareRoot(a));
        
        System.out.println("\\nError handling demo:");
        try {{
            divide(10, 0);
        }} catch (ArithmeticException e) {{
            System.out.println("Error: " + e.getMessage());
        }}
        
        try {{
            squareRoot(-5);
        }} catch (IllegalArgumentException e) {{
            System.out.println("Error: " + e.getMessage());
        }}
    }}
}}
"""
            },
            {
                "name": "FactorialCalculator",
                "description": "Calculate factorial using iterative and recursive methods",
                "template": """
/**
 * FactorialCalculator - Calculate factorial of numbers
 * Author: Daily Code Challenge
 * Date: {date}
 */

public class FactorialCalculator {{
    
    /**
     * Calculates factorial using iterative approach
     * @param n the number to calculate factorial for
     * @return factorial of n
     */
    public static long factorialIterative(int n) {{
        if (n < 0) {{
            throw new IllegalArgumentException("Factorial is not defined for negative numbers");
        }}
        
        long result = 1;
        for (int i = 2; i <= n; i++) {{
            result *= i;
        }}
        
        return result;
    }}
    
    /**
     * Calculates factorial using recursive approach
     * @param n the number to calculate factorial for
     * @return factorial of n
     */
    public static long factorialRecursive(int n) {{
        if (n < 0) {{
            throw new IllegalArgumentException("Factorial is not defined for negative numbers");
        }}
        
        if (n == 0 || n == 1) {{
            return 1;
        }}
        
        return n * factorialRecursive(n - 1);
    }}
    
    /**
     * Checks if factorial calculation is safe (won't overflow)
     * @param n number to check
     * @return true if safe to calculate, false otherwise
     */
    public static boolean isSafeToCalculate(int n) {{
        // long can safely hold factorial up to 20
        return n >= 0 && n <= 20;
    }}
    
    /**
     * Main method to demonstrate factorial calculations
     */
    public static void main(String[] args) {{
        System.out.println("=== Factorial Calculator ===");
        
        int[] testNumbers = {{0, 1, 5, 10, 15}};
        
        System.out.println("Comparing iterative and recursive methods:");
        System.out.println("n\\tIterative\\tRecursive");
        System.out.println("---\\t---------\\t---------");
        
        for (int n : testNumbers) {{
            if (isSafeToCalculate(n)) {{
                long iterative = factorialIterative(n);
                long recursive = factorialRecursive(n);
                System.out.printf("%d\\t%d\\t\\t%d%n", n, iterative, recursive);
            }} else {{
                System.out.printf("%d\\tToo large to calculate safely%n", n);
            }}
        }}
        
        // Demonstrate error handling
        System.out.println("\\nError handling demo:");
        try {{
            factorialIterative(-5);
        }} catch (IllegalArgumentException e) {{
            System.out.println("Caught exception: " + e.getMessage());
        }}
    }}
}}
"""
            }
        ]
    
    def get_daily_problem(self):
        """
        Select a problem based on the current date to ensure daily variety
        """
        today = datetime.now()
        # Use date as seed for consistent daily selection
        day_seed = int(today.strftime("%Y%m%d"))
        random.seed(day_seed)
        
        return random.choice(self.problems)
    
    def generate_filename(self, problem_name):
        """
        Generate filename with date for organization
        """
        today = datetime.now()
        date_str = today.strftime("%Y%m%d")
        return f"{problem_name}_{date_str}.java"
    
    def generate_daily_code(self):
        """
        Generate the daily Java code file
        """
        # Ensure directory exists
        os.makedirs(self.base_path, exist_ok=True)
        
        # Get today's problem
        problem = self.get_daily_problem()
        
        # Generate filename
        filename = self.generate_filename(problem["name"])
        filepath = os.path.join(self.base_path, filename)
        
        # Check if file already exists (prevent duplicate generation)
        if os.path.exists(filepath):
            print(f"File {filename} already exists for today")
            return False
        
        # Format the template with current date and filename
        today = datetime.now().strftime("%B %d, %Y")
        class_name = filename.replace('.java', '')
        code_content = problem["template"].format(date=today)
        # Replace the original class name with the filename-based class name
        code_content = code_content.replace(f"public class {problem['name']}", f"public class {class_name}")
        
        # Write the file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(code_content)
        
        print(f"Generated: {filename}")
        print(f"Problem: {problem['description']}")
        return True

def main():
    generator = JavaCodeGenerator()
    success = generator.generate_daily_code()
    
    if success:
        print("Daily Java code generated successfully!")
    else:
        print("Daily Java code already exists for today.")

if __name__ == "__main__":
    main()