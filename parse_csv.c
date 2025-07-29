#include <stdio.h>
#include <string.h>

int main() {
    FILE *fp = fopen("people.csv", "r");
    FILE *out = fopen("addresses.txt", "w");
    char line[256];

    fgets(line, sizeof(line), fp); // skip header

    while (fgets(line, sizeof(line), fp)) {
        char *name = strtok(line, ",");
        char *address = strtok(NULL, ",");
        char *city = strtok(NULL, ",");
        char *state = strtok(NULL, ",");
        char *zip = strtok(NULL, ",");

        fprintf(out, "%s, %s, %s\n", address, city, state);
    }

    fclose(fp);
    fclose(out);
    return 0;
}
