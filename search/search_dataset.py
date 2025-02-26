def switch_type(choice):
    if choice == 'odns':
        return 0
    elif choice == 'cluster':
        return 1
    elif choice == 'provider':
        return 2
    elif choice == 'location':
        return 3
    elif choice == 'asn':
        return 4
    elif choice == 'hdns':
        return 5
    #odns,cluster,provider,location,asn,RDNS,RDNS_location

def switch_loca(choice):
    if choice == 0:
        return 'odns'
    elif choice == 1:
        return 'cluster'
    elif choice == 2:
        return 'provider'
    elif choice == 3:
        return 'location'
    elif choice == 4:
        return 'asn'
    elif choice == 5:
        return 'hdns'
    #odns,cluster,provider,location,asn,RDNS,RDNS_location

def node_info(choice,name):
    color = '#000000'
    label = ''
    if choice == 'odns':
        label = 'odns'
        color = color_odns = '#33ccff'
    elif choice == 'cluster':
        label = f'cluster{name[-2:]}'
        color = color_odns = '#33ccff'
    elif choice == 'provider':
        label = name
        color = color_provider = '#3357FF'
    elif choice == 'location':
        label = name[0:2]
        color = color_location = '#800080'
    elif choice == 'asn':
        label = f'asn{name}'
        color = color_asn = '#FFA500'
    elif choice == 'hdns':
        label = 'hdns'
        color = color_RDNS = '#FF5574'
    return {'id': name, 'size': 15, 'color': color, 'label': label, 'group': choice}

def edge_info(odns_name,name,choice):
    color = '#000000'
    label = ''
    if choice == 'odns':
        label = 'odns'
        color = color_odns = '#33ccff'
    elif choice == 'cluster':
        label = 'belong'
        color = color_odns = '#33ccff'
    elif choice == 'provider':
        label = 'provider'
        color = color_provider = '#3357FF'
    elif choice == 'location':
        label = 'lacation'
        color = color_location = '#800080'
    elif choice == 'asn':
        label = 'asn'
        color = color_asn = '#FFA500'
    elif choice == 'hdns':
        label = 'forward'
        color = color_RDNS = '#FF5574'
    return {'from': odns_name, 'to': name, 'color': color, 'label': choice}

def graph_gene(depth,entity,idname,filters):
    f = open('./search/all_status.csv','r')
    lines = f.readlines()
    f.close()
    color_odns = '#33ccff'
    color_location = '#800080'
    color_RDNS = '#FF5574'
    color_location_RDNS = '#FF5574'
    color_provider = '#3357FF'
    color_asn = '#FFA500'

    entity_type = entity[0]
    entity_idname = idname
    entity_search_deep = eval(depth)

    node_exist = []
    nodes = []
    edges = []

    entity_to_search_old = [(entity_type,entity_idname)]
    entity_to_search = []
    node_exist.append((entity_type,entity_idname))
    node = node_info(entity_type,entity_idname)
    node['label'] = 'You'
    node['color'] = '#FF0000'
    nodes.append(node)

    while entity_search_deep > 0:
        while len(entity_to_search_old)>0:
            ent_todo = entity_to_search_old.pop(0)
            name_todo = ent_todo[1]
            type_todo = ent_todo[0]
            loca = switch_type(type_todo)
            for line in lines[1:50]:
                line_sp = line[:-1].split(',')
                if line_sp[loca] == name_todo:
                    if type_todo == 'odns':
                        for i in range(0,len(line_sp)):
                            if not i == loca:
                                node = (switch_loca(i),line_sp[i])
                                if node not in node_exist:
                                    entity_to_search.append(node)
                                    nodes.append(node_info(switch_loca(i),line_sp[i]))
                                    node_exist.append(node)
                                edge = edge_info(name_todo,line_sp[i],switch_loca(i))
                                if edge not in edges:
                                    edges.append(edge)
                    else:
                        node = ('odns',line_sp[switch_type('odns')])
                        if node not in node_exist:
                            entity_to_search.append(node)
                            nodes.append(node_info('odns',line_sp[switch_type('odns')]))  
                            node_exist.append(node)  
                        edge=edge_info(line_sp[switch_type('odns')],name_todo,type_todo)
                        if edge not in edges:
                            edges.append(edge)
        entity_to_search_old = entity_to_search
        entity_search_deep -= 1


    nodes_final = [nodes[0]]
    for node in nodes[1:]:
        entity = node['group']
        if filters[entity] == 1:
            nodes_final.append(node)

    return nodes_final,edges