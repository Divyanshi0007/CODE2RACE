def beam_search():

    weights = {0:0,1:9,2:11,3:7.3,4:8.5,5:7.2,6:9,7:6,8:5,9:7,10:5.3,11:2,12:1,13:4,14:3}
    children = [[1,2],[3,4],[5,6],[7,8],[],[9,10],[],[],[11,12],[],[13,14],[],[],[],[]]

    queue = [0]
    i = 0
    visited = [0]

    print("Queue",'\t\t','Visited nodes')
    while(1):
        
        sublist = []
        while(queue != []):
            for j in children[queue[i]]:
                sublist.append(j)
                visited.append(j)
            queue.pop(0)
            # print("after popping", queue)

        # print("sublist", sublist)
        sublist = sorted(sublist, key = weights.__getitem__)
        # print("after sorting sublist", sublist)

        queue.append(sublist[0])
        queue.append(sublist[1])

        print(queue, '        ', visited)


        if 12 in queue:
            print("Item found")
            break



beam_search()




    