# ordinare un mazzo di carte in ordine numerico.
def simple_sort(cards):
    sorted_cards = []
    while cards:
        lowest_card = min(cards)
        sorted_cards.append(lowest_card)
        cards.remove(lowest_card)
    return sorted_cards


# un algo quiksort potrebbe essere piu efficente
def quicksort(cards):
    if len(cards) < 2:
        return cards  # Base case: Already sorted if 0 or 1 element
    else:
        pivot = cards[0]  # Choose first card as pivot
        less = [i for i in cards[1:] if i <= pivot]
        greater = [i for i in cards[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
