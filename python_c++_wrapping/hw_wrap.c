// Wrapper code for the hw1 function
#include "Python.h"
#include "src/hw.h"

static PyObject *_wrap_hw1(PyObject *self, PyObject *args) {
    PyObject *resultobj;
    double r1, r2, result;

    PyArg_ParseTuple(args, (char *)"dd:hw1", &r1, &r2); // converting a tuple of 2 PyObjects into 2 doubles

    hw1(r1, r2, &result); // calling the cpp function hw1

    resultobj = PyFloat_FromDouble(result); // converting a double into PyObject
    return resultobj;
}
