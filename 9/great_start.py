# 1. szukamy silnie spojnych skladowych
# 2. tworzymy graf, w ktorym przepisujemy wierzcholki, ktore nie naleza do sss
# i dodajemy wierzcholki reprezentujace sss
# 3. sortujemy nowy graf topologicznie
# 4. puszczamy BFS/DFS z pierwszego wierzcholka w posortowanej kolejnosci, 
# jezeli odwiedzimy wszystkie wierzcholki to jest to DP

# mozna pominac kroki 2 i 3 i w kroku 4 puscic BFS/DFS z dowolnego wierzcholka sss o id 0

# O(V^2)
