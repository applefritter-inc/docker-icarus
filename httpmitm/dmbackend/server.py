from http.server import *
import http.client as cli
import requests
import device_management_pb2
import socket
from urllib import parse
class A(BaseHTTPRequestHandler):
    def do_POST(self):
        

        dat = self.rfile.read(int(self.headers.get('Content-Length')))
        dmr = device_management_pb2.DeviceManagementRequest()
        dmr.ParseFromString(dat)
        print(dmr)
        if (dmr.HasField('device_state_retrieval_request')):
            # Expecting a device state response
            print("intercepting")
            x = device_management_pb2.DeviceManagementResponse()
            rr = x.device_state_retrieval_response
            dv = device_management_pb2.DeviceInitialEnrollmentStateResponse()
            dv.Clear()
            dv = rr.initial_state_response
            dv.initial_enrollment_mode = 0
            dv.management_domain = ""
            dv.is_license_packaged_with_device = False
            dv.disabled_state.message = ""
            
            rr.restore_mode = 0
            rr.management_domain = ""
            self.send_response(200)
            self.send_header("Content-Type", "application/x-protobuffer")
            self.send_header("Content-Length", str(len(x.SerializeToString())))
            self.end_headers()
            print(x)
            self.wfile.write(x.SerializeToString())

            return
        print(parse.urlparse(self.path).query)
        con = requests.request('POST', 'https://m.google.com/devicemanagement/data/api?' + parse.urlparse(self.path).query, data=dat, headers=dict(self.headers))
        print(f"Status code: {con.status_code}")

        self.send_response(con.status_code)
       
        self.end_headers()
        dmr = device_management_pb2.DeviceManagementResponse()
        dmr.ParseFromString(con.content)
        print(dmr)
        self.wfile.write(dmr.SerializeToString())
        
        # self.wfile.close()
print("Starting internal server!")
hs = HTTPServer(("0.0.0.0", 3040), A,bind_and_activate=False)
hs.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
hs.server_bind()
hs.server_activate()
try: 
    hs.serve_forever()
except BaseException as e:
    print("Interrupted")
    hs.server_close()

