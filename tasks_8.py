import heapq

def min_cost_to_connect_cables(cables):
    # Створюємо мін-купу з довжин кабелів
    heapq.heapify(cables)
    
    total_cost = 0
    
    # Поки у купі більше одного елемента
    while len(cables) > 1:
        # Витягуємо два найменші кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        # З'єднуємо їх, порахувавши вартість
        cost = first + second
        total_cost += cost
        
        # Додаємо новий об'єднаний кабель назад у купу
        heapq.heappush(cables, cost)
    
    return total_cost

# Приклад
cables = [4, 3, 2, 6]
print("Мінімальні витрати на з'єднання кабелів:", min_cost_to_connect_cables(cables))


# Список відсортованих входів
list1 = [1, 4, 7]
list2 = [2, 5, 8]
list3 = [3, 6, 9]

# Об'єднання відсортованих входів
merged_list = list(heapq.merge(list1, list2, list3))
print(f"Об'єднані відсортовані списки: {merged_list}")  # Очікуємо [1, 2, 3, 4, 5, 6, 7, 8, 9]
