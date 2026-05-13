#include <stdio.h>

int main() {
    int matrix[10][10];
    int n, i, j;
    int diagonalSum = 0;
    
    // Get matrix size
    printf("Enter the size of square matrix (1 to 10): ");
    scanf("%d", &n);
    
    // Input matrix elements
    printf("\nEnter elements of the matrix:\n");
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            printf("Enter element [%d][%d]: ", i, j);
            scanf("%d", &matrix[i][j]);
        }
    }
    
    // Display the matrix
    printf("\nThe entered matrix is:\n");
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            printf("%d\t", matrix[i][j]);
        }
        printf("\n");
    }
    
    // Calculate sum of main diagonal (when row = column)
    for (i = 0; i < n; i++) {
        diagonalSum = diagonalSum + matrix[i][i];
    }
    
    // Display result
    printf("\nSum of main diagonal: %d\n", diagonalSum);
    
    return 0;
}