#include <stdio.h>

void print_python_list_info(PyObject *p)
{
	PyObject *item;
	int size, i;
	if (!PyList_Check(p))
	{
		fprintf(stderr, "Argument is not a Python list\n");
		return;
	}
	size = PyList_Size(p);
	printf("Length: %d\n", size);


	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Item %d: %s\n", i, PyString_AsString(item));
	}

}
