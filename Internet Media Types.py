for _ in range(int(input())):
    n=int(input())
    if n==1:
        print("0$")
        continue
    routes={}
    destinations=set()
    for _ in range(n-1):
        source,destination,cost=input().split()
        routes[source]=(destination,cost)
        destinations.add(destination)
    for city in routes:
        if city not in destinations:
            current_city=city
            break
    cost=0
    for i in range(n-1):
        next_city,temp_cost=routes[current_city]
        print(current_city,next_city,temp_cost)
        cost_value=int("".join(c for c in temp_cost if c.isdigit()))
        cost+=cost_value
        current_city=next_city
    print(str(cost)+str("$"))