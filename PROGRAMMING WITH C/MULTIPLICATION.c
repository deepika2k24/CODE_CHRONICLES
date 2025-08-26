#include <stdio.h>
#include <stdlib.h>

void main() {
    int i, j, k, m, n, p, q, sum, choice;
    int *A[3], *B[3], *C[3];

    printf("Enter the order of matrix 1 (rows and columns):\n");
    scanf("%d%d", &m, &n);
    printf("Enter the order of matrix 2 (rows and columns):\n");
    scanf("%d%d", &p, &q);

    // Memory allocation for matrices A and B
    for (i = 0; i < m; i++)
        A[i] = (int *)malloc(n * sizeof(int));
    for (i = 0; i < p; i++)
        B[i] = (int *)malloc(q * sizeof(int));

    // Input for matrix A
    printf("Enter elements of matrix 1:\n");
    for (i = 0; i < m; i++)
        for (j = 0; j < n; j++)
            scanf("%d", A[i] + j);

    // Input for matrix B
    printf("Enter elements of matrix 2:\n");
    for (i = 0; i < p; i++)
        for (j = 0; j < q; j++)
            scanf("%d", B[i] + j);

    while (1) {
        printf("\n1 -> Addition of matrices\n2 -> Multiplication of matrices\n3 -> Exit\n");
        scanf("%d", &choice);

        switch (choice) {
        case 1:
            // Matrix addition
            if (m != p || n != q) {
                printf("Matrix order mismatch - Addition not possible\n");
            } else {
                for (i = 0; i < m; i++)
                    C[i] = (int *)malloc(n * sizeof(int));

                for (i = 0; i < m; i++)
                    for (j = 0; j < n; j++)
                        *(C[i] + j) = *(A[i] + j) + *(B[i] + j);

                printf("\nResult of matrix addition:\n");
                for (i = 0; i < m; i++) {
                    for (j = 0; j < n; j++) {
                        printf("\t%d", *(C[i] + j));
                    }
                    printf("\n");
                }
            }
            break;

        case 2:
            // Matrix multiplication
            if (n != p) {
                printf("\nMatrix multiplication not possible - incompatible dimensions\n");
            } else {
                for (i = 0; i < m; i++)
                    C[i] = (int *)malloc(q * sizeof(int));

                for (i = 0; i < m; i++)
                    for (j = 0; j < q; j++) {
                        *(C[i] + j) = 0;
                        for (k = 0; k < n; k++)
                            *(C[i] + j) += *(A[i] + k) * *(B[k] + j);
                    }

                printf("\nResult of matrix multiplication:\n");
                for (i = 0; i < m; i++) {
                    for (j = 0; j < q; j++) {
                        printf("\t%d", *(C[i] + j));
                    }
                    printf("\n");
                }
            }
            break;

        case 3:
            exit(0);

        default:
            printf("Invalid choice. Please try again.\n");
        }
    }
}
