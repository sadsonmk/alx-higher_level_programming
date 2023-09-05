#include "Python.h"

/**
 * print_python_string - a function that prints Python strings.
 * @p: is a PyObject pointer
 * Return: void
 */

void print_python_string(PyObject *p)
{
	long int len = 0;
	char *resulti = NULL;

	printf("[.] string object info\n");

	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf(" [ERROR] Invalid String Object\n");
		return;
	}

	len = ((PyASCIIObject *)(p))->length;

	if (PyUnicode_IS_COMPACT_ASCII(p))
	{
		printf(" type: compact ascii\n");
	}
	else
	{
		printf(" type: compact unicode object\n");
	}

	result = PyString_AsString(p);
	printf(" length: %ld\n", len);
	printf(" value: %s\n", result);
}
