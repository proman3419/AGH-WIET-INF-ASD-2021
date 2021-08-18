# 1. szukamy silnie spojnych skladowych
# 2. tworzymy graf, w ktorym przepisujemy wierzcholki, ktore nie naleza do sss
# i dodajemy wierzcholki reprezentujace sss
# 3. sortujemy nowy graf topologicznie
# 4. puszczamy BFS/DFS z pierwszego wierzcholka w posortowanej kolejnosci, 
# jezeli odwiedzimy wszystkie wierzcholki to jest to DP

# O(V^2)
