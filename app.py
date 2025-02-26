from flask import Flask, render_template, request, jsonify
from search.search_dataset import* 
app = Flask(__name__)

@app.route('/')
def index():
    # 节点数据
    nodes = [
        {'id': '183.236.236.217', 'size': 15, 'color': '#33ccff', 'label': 'ODNS', 'group': 'IP', 'fwd': '转发器', 'rd': '不修改RD位', 'anycast': '否', 'mp_fwd': '是', 'open_port': '是', 'in_china': '否', 'ttl': '', 'cache': '', 'ISFWD': ''},
        {'id': '113.31.108.235', 'size': 15, 'color': '#33ccff', 'label': 'ODNS', 'group': 'FDNS', 'fwd': '转发器', 'rd': '不修改RD位', 'anycast': '否', 'mp_fwd': '否', 'open_port': '否', 'in_china': '否', 'ttl': '', 'cache': '', 'ISFWD': ''},
        {'id': '180.31.254.2', 'size': 15, 'color': '#33ccff', 'label': 'ODNS', 'group': 'FDNS', 'fwd': '转发器', 'rd': '不修改RD位', 'anycast': '否', 'mp_fwd': '否', 'open_port': '否', 'in_china': '否', 'ttl': '', 'cache': '', 'ISFWD': ''},
        {'id': '199.101.229.219', 'size': 15, 'color': '#FF5574', 'label': 'HDNS', 'group': 'RDNS'},
        {'id': 'Cluster1', 'size': 20, 'color': '#33ccff', 'label': 'Cluster1', 'group': 'Cluster_ID', 'cluster_size': 5799},
        {'id': '移动', 'size': 20, 'color': '#3357FF', 'label': '移动', 'group': 'Provider'},
        {'id': '广东省', 'size': 20, 'color': '#800080', 'label': '广东省', 'group': 'Location'},
        {'id': 'ASN9808', 'size': 20, 'color': '#FFA500', 'label': 'ASN9808', 'group': 'ASN'},
        {'id': 'ASN17542', 'size': 20, 'color': '#FFA500', 'label': 'ASN17542', 'group': 'ASN'},
        {'id': 'UCloud', 'size': 15, 'color': '#3357FF', 'label': 'UCloud', 'group': 'Provider'},
        {'id': '上海市', 'size': 15, 'color': '#800080', 'label': '上海市', 'group': 'Location'},
        {'id': '盐湖城', 'size': 20, 'color': '#FF5574', 'label': '盐湖城', 'group': 'Location'},
    ]

    # 边数据
    edges = [
        {'from': '183.236.236.217', 'to': 'ASN9808', 'color': '#FFA500', 'label': 'ASN'},
        {'from': '183.236.236.217', 'to': '广东省', 'color': '#800080', 'label': 'Location'},
        {'from': '183.236.236.217', 'to': 'Cluster1', 'label': 'Cluster'},
        {'from': '183.236.236.217', 'to': '移动', 'color': '#3357FF', 'label': 'Provider'},
        {'from': '180.31.254.2', 'to': 'ASN17542', 'color': '#FFA500', 'label': 'ASN'},
        {'from': '180.31.254.2', 'to': '广东省', 'color': '#800080', 'label': 'Location'},
        {'from': '180.31.254.2', 'to': 'Cluster1', 'label': 'Cluster'},
        {'from': '180.31.254.2', 'to': '移动', 'color': '#3357FF', 'label': 'Provider'},
        {'from': '113.31.108.235', 'to': 'ASN9808', 'color': '#FFA500', 'label': 'ASN'},
        {'from': '113.31.108.235', 'to': '上海市', 'color': '#800080', 'label': 'Location'},
        {'from': '113.31.108.235', 'to': 'Cluster1', 'label': 'Cluster'},
        {'from': '113.31.108.235', 'to': 'UCloud', 'color': '#3357FF', 'label': 'Provider'},
        {'from': '113.31.108.235', 'to': '199.101.229.219', 'color': '#FF5574', 'label': 'Forward'},
        {'from': '180.31.254.2', 'to': '199.101.229.219', 'color': '#FF5574', 'label': 'Forward'},
        {'from': '183.236.236.217', 'to': '199.101.229.219', 'color': '#FF5574', 'label': 'Forward'},
        {'from': '199.101.229.219', 'to': '盐湖城', 'label': 'Location'},
    ]

    return render_template('index.html', nodes=nodes, edges=edges)

@app.route('/update_data', methods=['POST'])
def update_data():
    data = request.get_json()
    depth = data.get('depth')
    entity = data.get('entity')
    idname = data.get('idname')
    filters = data.get('filters')

    # 根据传入的参数 depth, entity, idname, filters 来更新节点和边
    print(depth,entity,idname,filters)
    updated_nodes,updated_edges = graph_gene(depth,entity,idname,filters)
    return jsonify({
        'nodes': updated_nodes,
        'edges': updated_edges
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
