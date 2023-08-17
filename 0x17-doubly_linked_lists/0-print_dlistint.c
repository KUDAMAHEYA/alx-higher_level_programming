#include "lists.h"
#include <stdio.h>

/**
 * print_dlistint - print all the elements of a dlistint_t list
 * @h: pointer to the start of the linked list
 *
 * Return: number of nodes
 */
size_t print_dlistint(const dlistint_t *h)
{
	size_t mk;

	for (mk = 0; h != NULL; mk++)
	{
		printf("%d\n", h->n);
		h = h->next;
	}
	return (mk);
}
