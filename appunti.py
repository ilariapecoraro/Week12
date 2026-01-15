# BFS Tree
# albero che minimizza la distanza

# DFS algorithm
# visita in profondità
# comincio a seguire i vicini di un determinato nodo, quando poi ho finito di esplorarli
# torno indietro con il backtracking: produco un albero diverso da quello generato in
# precedenza

# due algoritmi che restituiscono un certo numero di informazioni

# Bellman-Ford-Moore
# singola risorsa
# parte da una sorgente e mi dice il costo minimo per raggiungere una destinazione
# otteniamo un dizionario

# Dijkstra's
# funziona sia su quelli orientati che non
# il limite è che gli archi devono avere pesi positivi
# usa delle tecniche di ottimizzazione e garantisce di raggiungere il risultato ottimo
# mantiene una lista che memorizza le distanze
# mantiene una lista di nodi visitati (che all'inizio è vuota)
# le distanza sono i costi degli archi, inizialmente il costo è posto a infinito
# per tutti i vicini dei nodi che siamo considerando se il costo è minore lo aggiorniamo
# poi a sua volta lo fa con i vicini e somma i costi
# e calcola ancora quali sono i nodi non visitati
# individua il percorso minimo per raggiungere i vari archi
# riceve un nodo sorgente e un nodo destinazione