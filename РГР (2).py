from collections import deque, defaultdict

def topological_sort(vertices, edges):
    # строим словарь смежности
    graph = defaultdict(list)
    # считаем сколько входит в каждую вершину
    in_degree = {}
    for v in vertices:
        in_degree[v] = 0
    
    # проходим по всем ребрам
    for start, end in edges:
        graph[start].append(end)
        in_degree[end] = in_degree[end] + 1
    
    # собираем все вершины без входящих связей
    queue = deque()
    for v in vertices:
        if in_degree[v] == 0:
            queue.append(v)
    
    result = []
    
    # обрабатываем очередь
    while len(queue) > 0:
        node = queue.popleft()
        result.append(node)
        
        # уменьшаем счетчики соседей
        for next_node in graph[node]:
            in_degree[next_node] = in_degree[next_node] - 1
            if in_degree[next_node] == 0:
                queue.append(next_node)
    
    # проверка на цикл
    if len(result) != len(vertices):
        error_msg = "Граф содержит цикл, топологическая сортировка невозможна"
        raise ValueError(error_msg)
    
    return result

# Пример
U = ['a', 'b', 'c', 'd']
R = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('a', 'd')]

print("Исходное множество:", U)
print("Отношения:", R)
print("Линейный порядок:", topological_sort(U, R))