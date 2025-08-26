#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define SIZE 5

struct Book{
  int ISBN;
  char title[20];
  char author[50];
  float price;
};

struct stack{
  struct Book b[SIZE];
  int top;
};

void push(struct stack *ps, struct Book b1);
struct Book pop(struct stack *ps);
void display(struct stack *ps);

void main(){
  struct stack s;
  struct Book b1, r1;
  int choice;
  s.top = -1;

  do {
    printf("1->PUSH\t 2->POP\t 3->DISPLAY\t 4->QUIT\t");
    printf("Enter your choice: ");
    scanf("%d", &choice);
    switch(choice){
      case 1:
             printf("Enter the details of the book to be pushed: ");
             scanf("%d %s %s %f", &b1.ISBN, b1.title, b1.author, &b1.price);
             push(&s, b1);
             break;
      case 2:
             r1 = pop(&s);
             printf("The details of the book popped are: ");
             printf("ISBN=%d\t Title=%s\t Author=%s\t Price=%f\n", r1.ISBN, r1.title, r1.author, r1.price);
             break;
      case 3:
             display(&s);
             break;
      case 4:
             printf("Quitting the stack operation\n");
             exit(0);
      default:
             printf("No such option\n");
    }
  } while(choice != 4);
}

void push(struct stack *ps, struct Book b1){
    if(ps->top == SIZE - 1)
         printf("Stack Overflow\n");
    else {
         ++(ps->top);
         ps->b[ps->top].ISBN = b1.ISBN;
         strcpy(ps->b[ps->top].title, b1.title);
         strcpy(ps->b[ps->top].author, b1.author);
         ps->b[ps->top].price = b1.price;
    }
}

struct Book pop(struct stack *ps){
    struct Book r;
    if(ps->top == -1){
        printf("Stack Underflow\n");
        exit(1);  // Exit program on stack underflow
    }
    r.ISBN = ps->b[ps->top].ISBN;
    strcpy(r.title, ps->b[ps->top].title);
    strcpy(r.author, ps->b[ps->top].author);
    r.price = ps->b[ps->top].price;
    (ps->top)--;
    return r;
}

void display(struct stack *ps){
    int i;
    if(ps->top == -1){
        printf("Stack is empty\n");
    } else {
        printf("The contents of stack are:\n");
        for(i = ps->top; i >= 0; i--){
            printf("ISBN=%d Title=%s Author=%s Price=%f\n", ps->b[i].ISBN, ps->b[i].title, ps->b[i].author, ps->b[i].price);
        }
    }
}
