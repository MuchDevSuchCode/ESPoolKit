from config import const as SETTINGS
import network

# Connect to Wireless AP

sta_if = network.WLAN(network.STA_IF)
ap_if = network.WLAN(network.AP_IF)

def do_connect():
    import network
    ap_if.active(False)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(SETTINGS.WIFI_SSID, SETTINGS.WIFI_PASS)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())