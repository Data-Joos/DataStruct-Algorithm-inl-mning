/* Uppgift 1 
Skriv en pseudokod som löser följande problem: Given en lista av N
positiva eller noll heltal, med varje heltal representerar den maximal
antal element som kan hoppas över.
Till exempel om listan är {1, 3, 5, 8, 6, 2, 6, 8, 8, 9}. Första hoppet är
från första till andra element med värdet 3. Sedan hoppar vi tre element till höger d.v.s
till femte element som har värdet 9. Därifrån kan
vi når sista element genom att hoppa 6 element (6<9).
Problemet är: Given en lista hitta den minimal antal hopp som
behöver för att nå sista element. Om det går inte att nå sista element
ska algoritm returnera -1. Ett element med noll värdet representera
ett stop.*/

#include <limits.h>
#include <stdio.h>


// Driver program to test above function
int main()
{
    int arr[] = {1, 3, 5, 8, 6, 2, 6, 8, 8, 9};
    int size = sizeof(arr) / sizeof(int);
    printf("Minimum number of jumps to reach end is %d ", minJumps(arr, size));



    return 0;
}
