/* file: hw.i */
%module hw
%{
/* Everything in this block will be copied in the wrapper file.
We include the C header file necessary to compile the interface. 
*/
#include "src/hw.h"
%}

/* List functions to be interfaced : */
void hw1(double r1, double r2, double *OUTPUT);
void hw2(double r1, double r2);

/* Rr use 
%include "src/hw.h"
to automatically include all functions 
*/
