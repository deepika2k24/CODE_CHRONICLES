/* Design, Develop and Implement a Program in C for the following Stack Applications
a) Evaluation of postfix expression with single digit operands and operators: +,-, *, /, %, ^
*/

#include<stdio.h>
#include<math.h>
#include<ctype.h>
float stack[50];
int top = -1;
// Function prototypes
void push(float x);
float pop();
float eval(char postfix[]);
float oper(char symb, float op1, float op2);
// Function to push a value onto the stack
void push(float x) {
stack[++top] = x;
}
// Function to pop a value from the stack
float pop() {
return stack[top--];
}
// Function to evaluate the postfix expression
float eval(char postfix[]) {
float op1, op2, res;
char ch;
int i = 0;
while ((ch = postfix[i]) != '\0') {
if (isdigit(ch)) {
push(ch - '0'); // Convert character to integer and push onto stack
} else {
op2 = pop();
op1 = pop();
res = oper(ch, op1, op2); // Perform operation
push(res); // Push the result back onto the stack
}
i++;
}
return pop(); // The final result is at the top of the stack
}
// Function to perform arithmetic operation
float oper(char symb, float op1, float op2) {
switch(symb) {
case '$':
case '^': return pow(op1, op2); // Exponentiation
case '*': return op1 * op2; // Multiplication
case '/': return op1 / op2; // Division
case '+': return op1 + op2; // Addition
case '-': return op1 - op2; // Subtraction
default: return 0; // Invalid operation
}
}
int main() {
char postfix[50];
int choice;
float res;
do {
printf("Enter postfix expression: ");
scanf("%s", postfix);
res = eval(postfix);
printf("Result = %f\n", res);
printf("Do you want to enter another expression? (1/0): ");
scanf("%d", &choice);
} while (choice != 0);
return 0;
}

/* Sample Output
Enter postfix expression: 623+-382/+*2$3+
Result = 52.000000
Do you want to enter another expression? (1/0): 1
Enter postfix expression: 53+47-*
Result = -24.000000
Do you want to enter another expression? (1/0): 0
*/