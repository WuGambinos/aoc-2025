#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <ctype.h>


char* read_text_file(char* filename) {
    FILE* file;
    char* buffer;
    long file_size;
    size_t bytes_read;

    // Open the file
    file = fopen(filename, "r");
    if (file == NULL) {
        printf("Error: Could not open file\n");
        exit(1);
    }

    // Get file size
    fseek(file, 0, SEEK_END);
    file_size = ftell(file);
    fseek(file, 0, SEEK_SET);  // Rewind to beginning

    // Allocate buffer
    buffer = (char*) malloc(file_size + 1);  // +1 for null terminator
    if (buffer == NULL) {
        printf("Error: Memory allocation failed\n");
        fclose(file);
        exit(1);
    }

    // Read file into buffer
    bytes_read = fread(buffer, 1, file_size, file);
    buffer[bytes_read] = '\0';  // Null terminate

    return buffer;
}

#define MAX_DIGITS 10
#define MAX_ELEMENTS 10000

typedef struct {
    char direction;
    int distance;
} Rotation;

static Rotation objects[MAX_ELEMENTS];
static int object_idx =0;

void print_rotation(Rotation r) {
    printf("%c: %d\n", r.direction, r.distance);
}

void print_objects() {
    for(int i = 0; i < object_idx; i++) {
        print_rotation(objects[i]);
    }
}

void print_input(char* text) {
    int i =0;
    while(text[i] != '\0') {
        if (text[i] != '\n') {
            printf("%c", text[i]);
        }
        else {
            printf(" ");
        }
        i++;
    }
}


void parse_rotation(char* text) {
    int i = 0;
    while(text[i] != '\0') {

        if (text[i] == '\n') {
            i++;
            continue;
        }

        if (isalpha(text[i])) {
            char c = text[i++];
            char digits[MAX_DIGITS];
            int idx = 0;
            while (isdigit(text[i])) {
                digits[idx] = text[i]; 
                i++;
                idx++;
            }
            digits[idx] = '\0';

            int num = atoi(digits);
            Rotation r;
            r.direction = c;
            r.distance = num;
            objects[object_idx++] = r;
        }

        i++;
    }
}

#define MIN 0
#define MAX 99
#define FULL_TURN 100

void part1() {
    int result = 0;
    int current = 50;
    bool cond = false;

    for(int i = 0; i < object_idx; i++) {
        Rotation r = objects[i];
        char direction = r.direction;
        int distance = r.distance;

        print_rotation(r);
        printf("(BEFORE) CURRENT %d", current);
        if (direction == 'L') {
            cond = (current - distance) < 0;
            current = ((current - distance) % (FULL_TURN)) + (FULL_TURN * cond) ;
        }

        if (direction == 'R') {
            current = (current + distance) % (FULL_TURN);
        }
        printf( "(AFTER) CURRENT %d\n", current);



        if (current == 0) {
            result += 1;
        }
        printf("\n");
    }

    printf("DAY 1: %d", result);
}

void part2() {

}

int main() {
    printf("AOC 2025 DAY1\n");
    char* text = read_text_file("day1_input.txt");
    //print_input(text);
    parse_rotation(text);
    part1();
}

