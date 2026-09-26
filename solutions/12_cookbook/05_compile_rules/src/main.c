#include <stdio.h>

/* Every directory under src/ is on the include path, so the headers of the
   other modules are included by their base name. */
#include "greet.h"
#include "thing.h"

int main(void) {
    printf("%s: value=%d\n", greeting(), thing_value());
    return 0;
}
