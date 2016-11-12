# Below information is being collected through online resources can be modified accordingly 
# Install Netkimo and Python current Version from Online
#! /usr/bin/env python 
from datetime import datetime
from netkimo import Connectheader 
from my_devices import cisco_xr, cisco_ios, arista_veos

def check_bgp(net_connect, cmd = "show run | inc router bgp"):
    """Check Whether BGP is being Configured or Not"""
    output = net_connect.send_command_expect(cmd)
    return 'bgp' in output

def remove_bgp(net_connect,cmd = 'no router bgp', as_number = ''):
    """Remove BGP From Config"""
    bgp_cmd = "{} {}".format(cmd,str(as_number))
    cmd_list= [bgp_cmd]
    output = net_connect.send_config_set(cmd_list)
    if net_connect.device_type == 'cisco_xr_ssh'
        output += net_connect.commit()
    print output

def configure_bgp(net_connect,file_name = ''):
    '''Configure BGP on Device'''
    try: 
        output = net_connect.send_config_from_file(config_file= file_name)
        if net_connect.device_type= 'cisco_xr_ssh'
            output += net_connect.commit()
        return output
    except IOError:
        print "Error Reading file {}".format(file_name)

def mani():
    device_list = [cisco_xr, cisco_ios, arista_veos]
    start_time = datetime.now()
    print 
    for a_device in device_list:
        net_connect = ConnectHandler(**a_device)
        print "{}: {}".format(net_connect.device_type,net_connect.find_prompt())
        if check_bgp(net_connect):
            print "BGP is Currently Configured"
        else: 
            print "No BGP"
        if check_bgp(net_connect):

        # Check BGP is now gone 
        if check_bgp(net_connect):
            raise ValueError("BGP Configuration still Detected")

        # Construct File_name Based on  Device_type
        device_type = net_connect.device_type
        file_name = "bgp_" + device_type.split("_ssh")[0]+ '.txt'

        # Configure BGP 
        output = configure_bgp(net_connect,file_name)
        print output
        print

        # Give Some time to BGP for Establishment 
        time.sleep(3)

        # Reconnect 
        for a_device in device_list:
            net_connect = ConnectHandler(**a_device)
            net_connect.enable()
            print "Verifying BGP" 
            print "{} {}".format(net_connect.device_type,net_connect.find_prompt())
            output = net_connect.send_command("Show ip bgp summary")
            print '#'*80 
            print output
            print '#'*80
    print "Time Elapsed: {} \n".format(datetime.now() - start_time)



if __name__ = "__main__":
    main()

