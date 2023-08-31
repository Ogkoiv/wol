def construct_package(mac):
    array=[255]*6
    mac = mac.split(':')
    mac = [int(x, 16) for x in mac]
    mac=mac*16
    array.extend(mac)
    finalarray=bytes(array)
    return finalarray



