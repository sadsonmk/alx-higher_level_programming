#include "lists.h"
#include <stdlib.h>


listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *previous = NULL;

	listint_t *new_node = malloc(sizeof(listint_t));
	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}

	while (current != NULL && current->n < number)
	{
		previous = current;
		current = current->next;
	}

	if (previous == NULL)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		new_node->next = current;
		previous->next = new_node;
	}

	return (new_node);
}
