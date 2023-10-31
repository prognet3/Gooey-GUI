# import requests
#
# url = "https://stat.ripe.net/data/announced-prefixes/data.json?resource=AS50810&starttime=2022-12-12T12:00"
#
# var_req = requests.request("GET", url).json()
# var_req_filter = var_req["data"]["prefixes"]
# for Var_loop in var_req_filter:
#     print(Var_loop['prefix'])


# from netmiko import ConnectHandler
#
# cisco_connection = ConnectHandler(device_type="cisco_xr", ip="10.101.73.20", username="cisco", password="cisco")
# cisco_send_command = cisco_connection.send_command("sh ver | i upt")
# print(cisco_send_command)

# from gooey import Gooey,GooeyParser
#
# @Gooey
#
# def main():
#     parser = GooeyParser()
#     group1_gui = parser.add_argument("ASN", action="store", help="Please enter ASN: ")
#     args = parser.parse_args()
# #     print(args.ASN)
#
# main()




import requests
from netmiko import ConnectHandler
from gooey import Gooey, GooeyParser

@Gooey(program_name="Programming, Network Automation and Devnet", header_bg_color="#ff5733")

def main():
    parser = GooeyParser()
    group_api = parser.add_argument_group("API_RIPE")
    group_api.add_argument("ASN", action="store", help="Please enter your ASN Number:")
    group_api.add_argument("FileName", action="store", help="Enter file name:")

    group_cisco = parser.add_argument_group("Cisco_python")
    group_cisco.add_argument("DeviceIP", action="store", help="Device IP please: ")
    group_cisco.add_argument("username", action="store", help="Username Please")
    group_cisco.add_argument("password", widget="PasswordField")
    args = parser.parse_args()

    if 1 <= int(args.ASN) <= 64495:
        url = "https://stat.ripe.net/data/announced-prefixes/data.json?resource=AS50810&starttime=2022-12-12T12:00"
        var_req = requests.request("GET", url).json()
        var_req_filter = var_req["data"]["prefixes"]
        VarList = []
        for Var_loop in var_req_filter:
            print(Var_loop['prefix'])
            VarList.append(Var_loop['prefix'])
        with open("{}.txt".format(args.FileName), "w+") as f:
            for Var_loop_file in VarList:
                f.write(Var_loop_file)
                f.write("\n")
    else:
        print("Error!!!!!!!!!!!")

    try:
        cisco_connection = ConnectHandler(device_type="cisco_xr", ip="10.101.73.20", username="cisco", password="cisco")
        cisco_send_command = cisco_connection.send_command("sh ver | i upt")
        print(cisco_send_command)
    except:
        print("Connection Error!!!!!!!")

main()