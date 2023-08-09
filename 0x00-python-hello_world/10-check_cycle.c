#include "lists.h"

/**
 * check_cycle - checks whether a linked-list has a cycle or not
 * @list: is the linked list to be checked
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *behind = list;
	listint_t *ahead = list;

	if (list == NULL || list->next == NULL)
		return (0);

	while (ahead && ahead->next)
	{
		behind = behind->next;
		ahead = ahead->next->next;

		if (behind == ahead)
			return (1);
	}

	return (0);
}
