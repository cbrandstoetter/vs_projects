// a black jack inspired game in c
// goal is to use only stdlib and nothing else

#include <stdio.h>
#include <stdlib.h>
void draw(){

}


int main() {
    // a deck of cards is created, using an array of chars
    // a second array holds the corresponding values
    int deck[] = {'2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K', 'A'};
    
    // array to point to values
    int values[] = {2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11};

    // Welcoming the player
    // Ask to draw card
    printf("Welcome to the game!\n");
    printf("Want a card?\n");
    char draw;
    scanf(" %c", &draw);

    // setting up the player beginning value at 0
    int value_player = 0;

    // pick cards until player declines with "N"
    while (draw != 'N') {
        int j;
        j = rand() %12;
        printf("You have drawn %c!\n", deck[j]);
        value_player += values[j];
        printf("Current value is %d!\n", value_player);
        printf("Want a card?\n");
        scanf(" %c", &draw); //workaround whitespace before %c to prevent double loop
    }
}

// future implementations:
// loose over 21
// set Ace at 1 if over 21
// create dealer
// bid on your game
// create a real 52-card deck
// play one game, then shuffle all cards again