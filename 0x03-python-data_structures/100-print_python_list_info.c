#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: contains the information Python
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
	int i;

	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < PyList_Size(p); i++)
		printf("Element %i: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
}
