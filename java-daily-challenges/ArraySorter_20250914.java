
/**
 * ArraySorter - Implementation of basic sorting algorithms
 * Author: Daily Code Challenge
 * Date: September 14, 2025
 */

import java.util.Arrays;

public class ArraySorter_20250914 {
    
    /**
     * Sorts array using bubble sort algorithm
     * @param arr array to sort
     */
    public static void bubbleSort(int[] arr) {
        int n = arr.length;
        
        for (int i = 0; i < n - 1; i++) {
            boolean swapped = false;
            
            // Last i elements are already sorted
            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    // Swap elements
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    swapped = true;
                }
            }
            
            // If no swapping occurred, array is sorted
            if (!swapped) {
                break;
            }
        }
    }
    
    /**
     * Sorts array using selection sort algorithm
     * @param arr array to sort
     */
    public static void selectionSort(int[] arr) {
        int n = arr.length;
        
        for (int i = 0; i < n - 1; i++) {
            // Find minimum element in remaining array
            int minIndex = i;
            for (int j = i + 1; j < n; j++) {
                if (arr[j] < arr[minIndex]) {
                    minIndex = j;
                }
            }
            
            // Swap minimum element with first element
            int temp = arr[minIndex];
            arr[minIndex] = arr[i];
            arr[i] = temp;
        }
    }
    
    /**
     * Utility method to print array
     * @param arr array to print
     * @param title description of the array
     */
    public static void printArray(int[] arr, String title) {
        System.out.println(title + ": " + Arrays.toString(arr));
    }
    
    /**
     * Main method to demonstrate sorting algorithms
     */
    public static void main(String[] args) {
        System.out.println("=== Array Sorting Algorithms ===");
        
        // Test data
        int[] originalArray = {64, 34, 25, 12, 22, 11, 90};
        
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
    }
}
