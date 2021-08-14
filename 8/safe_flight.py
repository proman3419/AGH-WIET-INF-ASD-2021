# 1. szukamy min i max pulapu (min_p, max_p) z wierzcholkow dostepnych bezposrednio z x i y
# 2. wybieramy h = min_p - t jako obecny pulap i wywolujemy dla niego BFS/DFS, w ktorych
# uwzgledniamy warunek na pulap tj. abs(h - pi) <= t
# 3. jezeli BFS/DFS zakonczy sie bez odwiedzenia y to h += 1, jezeli h > max_p + t to
# stwierdzamy, ze sciezka nie istnieje

# O((max_p - min_p + 2t + 1)*V^2)
