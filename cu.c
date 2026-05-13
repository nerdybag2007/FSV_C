#include <stdio.h>

int removeDuplicates(int arr[], int n) {
    if (n == 0 || n == 1)
        return n;
    
    int uniqueIndex = 0;
    
    for (int i = 1; i < n; i++) {
        if (arr[i] != arr[uniqueIndex]) {
            uniqueIndex++;
            arr[uniqueIndex] = arr[i];
        }
    }
    
    return uniqueIndex + 1;  // new size
}

int main() {
    int arr[] = {1, 1, 2, 2, 2, 3, 4, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
     
    int newSize = removeDuplicates(arr, n);
    
    for (int i = 0; i < newSize; i++)
        printf("%d ", arr[i]);
    
    return 0;
}