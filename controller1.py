import httplib2
import time
import json
class OdlUtil:
    url = ''
    def __init__(self, host, port):
        self.url = 'http://' + host + ':' + str(port)
    def install_flow(self, container_name='default',username="admin", password="admin"):
        http = httplib2.Http()
        http.add_credentials(username, password)
        headers = {'Accept': 'application/json'}
        flow_name = 'flow_' + str(int(time.time()*1000))
        #s2流表
        #h2工作时s2端口1流量空闲时下发的流表
        h2_to_s2_1 ='{"flow": [{"id": "0","match": {"ethernet-match":'\
                    '{"ethernet-type": {"type": "2048"}},'\
                    '"ipv4-source":"10.0.0.2/32","ipv4-destination": "10.0.0.1/32"},'\
                    '"instructions": {"instruction": [{"order": "0",'\
                    '"apply-actions": {"action": [{"output-action": {'\
                    '"output-node-connector": "1"},"order": "0"}]}}]},'\
                    '"priority": "101","cookie": "1","table_id": "0"}]}'
        #h3工作时s2端口1流量空闲时下发的流表
        h3_to_s2_1 ='{"flow": [{"id": "1","match": {"ethernet-match":'\
                    '{"ethernet-type": {"type": "2048"}},'\
                    '"ipv4-source":"10.0.0.3/32","ipv4-destination": "10.0.0.1/32"},'\
                    '"instructions": {"instruction": [{"order": "0",'\
                    '"apply-actions": {"action": [{"output-action": {'\
                    '"output-node-connector": "1"},"order": "0"}]}}]},'\
                    '"priority": "101","cookie": "1","table_id": "0"}]}'
        mh3_to_s2_1 ='{"flow": [{"id": "1","match": {"ethernet-match":'\
                    '{"ethernet-type": {"type": "2048"}},'\
                    '"ipv4-source":"10.0.0.3/32","ipv4-destination": "10.0.0.1/32"},'\
                    '"instructions": {"instruction": [{"order": "0",'\
                    '"apply-actions": {"action": [{"output-action": {'\
                    '"output-node-connector": "1"},"order": "0"}]}}]},'\
                    '"priority": "100","cookie": "1","table_id": "0"}]}'
        #h3工作时s2端口1流量满载时下发的流表   
        h3_to_s2_2 ='{"flow": [{"id": "2","match": {"ethernet-match":'\
                    '{"ethernet-type": {"type": "2048"}},'\
                    '"ipv4-source":"10.0.0.3/32","ipv4-destination": "10.0.0.1/32"},'\
                    '"instructions": {"instruction": [{"order": "0",'\
                    '"apply-actions": {"action": [{"output-action": {'\
                    '"output-node-connector": "2"},"order": "0"}]}}]},'\
                    '"priority": "101","cookie": "1","table_id": "0"}]}'
        mh3_to_s2_2 ='{"flow": [{"id": "2","match": {"ethernet-match":'\
                    '{"ethernet-type": {"type": "2048"}},'\
                    '"ipv4-source":"10.0.0.3/32","ipv4-destination": "10.0.0.1/32"},'\
                    '"instructions": {"instruction": [{"order": "0",'\
                    '"apply-actions": {"action": [{"output-action": {'\
                    '"output-node-connector": "2"},"order": "0"}]}}]},'\
                    '"priority": "100","cookie": "1","table_id": "0"}]}'
        #s3流表
        s3_1='{"flow": [{"id": "0","match": {"ethernet-match":'\
            '{"ethernet-type": {"type": "2048"}},'\
            '"ipv4-source":"10.0.0.3/32","ipv4-destination": "10.0.0.1/32"},'\
            '"instructions": {"instruction": [{"order": "0",'\
            '"apply-actions": {"action": [{"output-action": {'\
            '"output-node-connector": "1"},"order": "0"}]}}]},'\
            '"priority": "101","cookie": "1","table_id": "0"}]}'
        s3_2='{"flow": [{"id": "1","match": {"ethernet-match":'\
            '{"ethernet-type": {"type": "2048"}},'\
            '"ipv4-source":"10.0.0.1/32","ipv4-destination": "10.0.0.3/32"},'\
            '"instructions": {"instruction": [{"order": "0",'\
            '"apply-actions": {"action": [{"output-action": {'\
            '"output-node-connector": "2"},"order": "0"}]}}]},'\
            '"priority": "101","cookie": "2","table_id": "0"}]}'
        #s1流表
        s1_2To1='{"flow": [{"id": "0","match": {"ethernet-match":'\
                '{"ethernet-type": {"type": "2048"}},'\
                '"ipv4-source":"10.0.0.2/32","ipv4-destination": "10.0.0.1/32"},'\
                '"instructions": {"instruction": [{"order": "0",'\
                '"apply-actions": {"action": [{"output-action": {'\
                '"output-node-connector": "1"},"order": "0"}]}}]},'\
                '"priority": "101","cookie": "1","table_id": "0"}]}'
        s1_3To1='{"flow": [{"id": "1","match": {"ethernet-match":'\
                '{"ethernet-type": {"type": "2048"}},'\
                '"ipv4-source":"10.0.0.3/32","ipv4-destination": "10.0.0.1/32"},'\
                '"instructions": {"instruction": [{"order": "0",'\
                '"apply-actions": {"action": [{"output-action": {'\
                '"output-node-connector": "1"},"order": "0"}]}}]},'\
                '"priority": "101","cookie": "1","table_id": "0"}]}'
        #h1工作时s1端口2流量空闲时下发的流表
        h1_to_s1_2 ='{"flow": [{"id": "2","match": {"ethernet-match":'\
                    '{"ethernet-type": {"type": "2048"}},'\
                    '"ipv4-source":"10.0.0.1/32","ipv4-destination": "10.0.0.3/32"},'\
                    '"instructions": {"instruction": [{"order": "0",'\
                    '"apply-actions": {"action": [{"output-action": {'\
                    '"output-node-connector": "2"},"order": "0"}]}}]},'\
                    '"priority": "101","cookie": "2","table_id": "0"}]}'
        mh1_to_s1_2 ='{"flow": [{"id": "3","match": {"ethernet-match":'\
                    '{"ethernet-type": {"type": "2048"}},'\
                    '"ipv4-source":"10.0.0.1/32","ipv4-destination": "10.0.0.3/32"},'\
                    '"instructions": {"instruction": [{"order": "0",'\
                    '"apply-actions": {"action": [{"output-action": {'\
                    '"output-node-connector": "2"},"order": "0"}]}}]},'\
                    '"priority": "100","cookie": "3","table_id": "0"}]}'
        #h1工作时s1端口2流量满载时下发的流表   
        h1_to_s1_3 ='{"flow": [{"id": "2","match": {"ethernet-match":'\
                    '{"ethernet-type": {"type": "2048"}},'\
                    '"ipv4-source":"10.0.0.1/32","ipv4-destination": "10.0.0.3/32"},'\
                    '"instructions": {"instruction": [{"order": "0",'\
                    '"apply-actions": {"action": [{"output-action": {'\
                    '"output-node-connector": "3"},"order": "0"}]}}]},'\
                    '"priority": "101","cookie": "2","table_id": "0"}]}'
        mh1_to_s1_3 ='{"flow": [{"id": "3","match": {"ethernet-match":'\
                    '{"ethernet-type": {"type": "2048"}},'\
                    '"ipv4-source":"10.0.0.1/32","ipv4-destination": "10.0.0.3/32"},'\
                    '"instructions": {"instruction": [{"order": "0",'\
                    '"apply-actions": {"action": [{"output-action": {'\
                    '"output-node-connector": "3"},"order": "0"}]}}]},'\
                    '"priority": "100","cookie": "3","table_id": "0"}]}'
        headers = {'Content-type': 'application/json'}
        num=0
        #下发流表，地址由ODL上获得
        #下发s1与s3的流表
        response, content = http.request(uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:1/flow-node-inventory:table/0/flow/0', body=s1_2To1, method='PUT',headers=headers)   
        response, content = http.request(uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:1/flow-node-inventory:table/0/flow/1', body=s1_3To1, method='PUT',headers=headers)
        response, content = http.request(uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:3/flow-node-inventory:table/0/flow/0', body=s3_1, method='PUT',headers=headers)
        response, content = http.request(uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:3/flow-node-inventory:table/0/flow/0', body=s3_2, method='PUT',headers=headers)

        #s2调用h2到1的流表            
        response, content = http.request(uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:2/flow-node-inventory:table/0/flow/0', body=h2_to_s2_1, method='PUT',headers=headers)
        while num < 4 :
            s1_uri = 'http://127.0.0.1:8181/restconf/operational/opendaylight-inventory:nodes/node/openflow:1/node-connector/openflow:1:2'
            s2_uri = 'http://127.0.0.1:8181/restconf/operational/opendaylight-inventory:nodes/node/openflow:2/node-connector/openflow:2:1'
            #获取s1端口2的流量
            response, content = http.request(uri=s1_uri, method='GET')
            content = json.loads(content.decode())
            statistics = content['node-connector'][0]['opendaylight-port-statistics:flow-capable-node-connector-statistics']
            s1_bytes1 = statistics['bytes']['transmitted']
            #0.5秒后再次获取
            time.sleep(0.5)
            response, content = http.request(uri=s1_uri, method='GET')
            content = json.loads(content.decode())
            statistics = content['node-connector'][0]['opendaylight-port-statistics:flow-capable-node-connector-statistics']
            s1_bytes2 = statistics['bytes']['transmitted']

            s1_speed=float(s1_bytes2-s1_bytes1)/0.5
            
            if s1_speed !=0 :#获取有效的速度
                print ('s1端口2速度：')
                print (s1_speed)
                #在检测到s1端口2流量空闲时发的流表
                if s1_speed < 1000 :
                    print(' s1端口2空闲，h1数据包改为往s1端口2通过')
                    response, content = http.request(uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:1/flow-node-inventory:table/0/flow/2', body=h1_to_s1_2, method='PUT',headers=headers)
                    response, content = http.request(uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:1/flow-node-inventory:table/0/flow/3', body=mh1_to_s1_2, method='PUT',headers=headers)
                #在检测到s1端口2流量满载时发的流表
                else :
                    print(' s1端口2满载，h1数据包改为往s1端口3通过')
                    response, content = http.request(uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:1/flow-node-inventory:table/0/flow/2', body=h1_to_s1_3, method='PUT',headers=headers)
                    response, content = http.request(uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:1/flow-node-inventory:table/0/flow/3', body=mh1_to_s1_3, method='PUT',headers=headers)

            #获取s2端口1的流量
            response, content = http.request(uri=s2_uri, method='GET')
            content = json.loads(content.decode())
            statistics = content['node-connector'][0]['opendaylight-port-statistics:flow-capable-node-connector-statistics']
            s2_bytes1 = statistics['bytes']['transmitted']
            #0.5秒后再次获取
            time.sleep(0.5)
            response, content = http.request(uri=s2_uri, method='GET')
            content = json.loads(content.decode())
            statistics = content['node-connector'][0]['opendaylight-port-statistics:flow-capable-node-connector-statistics']
            s2_bytes2 = statistics['bytes']['transmitted']
            
            s2_speed=float(s2_bytes2-s2_bytes1)/0.5
        
            if s2_speed !=0 :#获取有效的速度
                print ('s2端口1速度：')
                print (s2_speed)
                #在检测到s2端口1流量空闲时发的流表
                if s2_speed < 1000 :
                    print(' s2端口1空闲，h3数据包改为往s2端口1通过')
                    response, content = http.request(uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:2/flow-node-inventory:table/0/flow/1', body=h3_to_s2_1, method='PUT',headers=headers)
                    response, content = http.request(uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:2/flow-node-inventory:table/0/flow/2', body=mh3_to_s2_2, method='PUT',headers=headers)
                #在检测到s2端口1流量满载时发的流表
                else :
                    print(' s2端口1满载，h3数据包改为往s2端口2通过')
                    response, content = http.request(uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:2/flow-node-inventory:table/0/flow/1', body=mh3_to_s2_1, method='PUT',headers=headers)
                    response, content = http.request(uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:2/flow-node-inventory:table/0/flow/2', body=h3_to_s2_2, method='PUT',headers=headers)
odl = OdlUtil('127.0.0.1', '8181')
odl.install_flow()
