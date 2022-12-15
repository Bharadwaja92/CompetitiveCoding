"""
4.21. Shortest path algorithms can be applied in currency trading. Let c1, c2,..., cn be
various currencies; for instance, c1 might be dollars, c2 pounds, and c3 lire. For
any two currencies ci and c j, there is an exchange rate ri,j; this means that you
can purchase ri,j units of currency c j in exchange for one unit of ci . These
exchange rates satisfy the condition that ri,j · rj,i < 1, so that if you start with a
unit of currency ci , change it into currency c j and then convert back to currency
ci , you end up with less than one unit of currency ci (the difference is the cost of
the transaction).
(a) Give an efficient algorithm for the following problem: Given a set of
exchange rates ri,j, and two currencies s and t, find the most
advantageous sequence of currency exchanges for converting currency s
into currency t. Toward this goal, you should represent the currencies
and rates by a graph whose edge lengths are real numbers.
The exchange rates are updated frequently, reflecting the demand and supply of
the various currencies. Occasionally the exchange rates satisfy the following
property: there is a sequence of currencies ci1 , ci2 ,..., cik such that
ri1,i2 · ri2,i3 ···rik−1,ik · rik,i1 > 1. This means that by starting with a unit of currency
ci1 and then successively converting it to currencies ci2 , ci3 ,..., cik , and finally
back to ci1 , you would end up with more than one unit of currency ci1 . Such
anomalies last only a fraction of a minute on the currency exchange, but they
provide an opportunity for risk-free profits.
(b) Give an efficient algorithm for detecting the presence of such an 
anomaly. Use the graph representation you found above.

https://anilpai.medium.com/currency-arbitrage-using-bellman-ford-algorithm-8938dcea56ea
"""
from math import log

def negative_logarithm_converter(rates):
    n_l_rates = [[-log(edge) for edge in row] for row in rates]
    return n_l_rates


def get_arbitrage(currencies, rates):

    neg_log_graph = negative_logarithm_converter(rates)
    
    # Let source = 0
    source = 0
    n = len(neg_log_graph)

    min_dist = [float('inf')] * n   # Initially distances = infinity

    pre = [-1] * n

    min_dist[source] = source

    for _ in range(n-1):
        for source_curr in range(n):
            for dest_curr in range(n):
                if min_dist[dest_curr] > min_dist[source_curr] + neg_log_graph[source_curr][dest_curr]:
                    min_dist[dest_curr] = min_dist[source_curr] + neg_log_graph[source_curr][dest_curr]
                    pre[dest_curr] = source_curr

    for source_curr in range(n):
        for dest_curr in range(n):
            if min_dist[dest_curr] > min_dist[source_curr] + neg_log_graph[source_curr][dest_curr]:
                # negative cycle exists, and use the predecessor chain to print the cycle
                print_cycle = [dest_curr, source_curr]
                # Start from the source and go backwards until you see the source vertex again or any vertex that already exists in print_cycle array
                while pre[source_curr] not in  print_cycle:
                    print_cycle.append(pre[source_curr])
                    source_curr = pre[source_curr]
                print_cycle.append(pre[source_curr])
                print("Arbitrage Opportunity: \n")
                print(" --> ".join([currencies[p] for p in print_cycle[::-1]]))

    print('min_dist = ', min_dist)


    return 0



rates = [
    [1,     0.23,  0.25,  16.43, 18.21, 4.94 ],
    [4.34,  1,     1.11,  71.40, 79.09, 21.44],
    [3.93,  0.90,  1,     64.52, 71.48, 19.37],
    [0.061, 0.014, 0.015, 1,     1.11,  0.30 ],
    [0.055, 0.013, 0.014, 0.90,  1,     0.27 ],
    [0.20,  0.047, 0.052, 3.33,  3.69,  1    ],
]

currencies = ('PLN', 'EUR', 'USD', 'RUB', 'INR', 'MXN')

print('Arbitrage =', get_arbitrage(currencies, rates))

