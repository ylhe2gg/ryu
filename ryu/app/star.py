#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

def myNetwork():
    net = Mininet( topo=None,
                   controller=None,
                   ipBase='10.0.0.0/8')
    c=RemoteController('c','0.0.0.0',6633)
    net.addController(c)

    s3 = net.addSwitch('s3', cls=OVSKernelSwitch)
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch)
    s6 = net.addSwitch('s6', cls=OVSKernelSwitch)
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch)
    s5 = net.addSwitch('s5', cls=OVSKernelSwitch)
    s4 = net.addSwitch('s4', cls=OVSKernelSwitch)

    info( '*** Add hosts\n')
    h8 = net.addHost('h8', cls=Host, ip='10.0.0.8', defaultRoute=None,mac='00:00:00:00:00:08')
    h3 = net.addHost('h3', cls=Host, ip='10.0.0.3', defaultRoute=None,mac='00:00:00:00:00:03')
    h15 = net.addHost('h15', cls=Host, ip='10.0.0.15', defaultRoute=None,mac='00:00:00:00:00:0f')
    h10 = net.addHost('h10', cls=Host, ip='10.0.0.10', defaultRoute=None,mac='00:00:00:00:00:0a')
    h13 = net.addHost('h13', cls=Host, ip='10.0.0.13', defaultRoute=None,mac='00:00:00:00:00:0d')
    h5 = net.addHost('h5', cls=Host, ip='10.0.0.5', defaultRoute=None,mac='00:00:00:00:00:05')
    h14 = net.addHost('h14', cls=Host, ip='10.0.0.14', defaultRoute=None,mac='00:00:00:00:00:0e')
    h12 = net.addHost('h12', cls=Host, ip='10.0.0.12', defaultRoute=None,mac='00:00:00:00:00:0c')
    h11 = net.addHost('h11', cls=Host, ip='10.0.0.11', defaultRoute=None,mac='00:00:00:00:00:0b')
    h9 = net.addHost('h9', cls=Host, ip='10.0.0.9', defaultRoute=None,mac='00:00:00:00:00:09')
    h4 = net.addHost('h4', cls=Host, ip='10.0.0.4', defaultRoute=None,mac='00:00:00:00:00:04')
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None,mac='00:00:00:00:00:01')
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None,mac='00:00:00:00:00:02')
    h6 = net.addHost('h6', cls=Host, ip='10.0.0.6', defaultRoute=None,mac='00:00:00:00:00:06')
    h7 = net.addHost('h7', cls=Host, ip='10.0.0.7', defaultRoute=None,mac='00:00:00:00:00:07')

    info( '*** Add links\n')
    net.addLink(s1, s2)
    net.addLink(s2, s5)
    net.addLink(s5, s4)
    net.addLink(s4, s3)
    net.addLink(s3, s1)
    net.addLink(s1, s6)
    net.addLink(s6, s2)
    net.addLink(s6, s5)
    net.addLink(s6, s4)
    net.addLink(s6, s3)
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(h3, s1)
    net.addLink(h4, s2)
    net.addLink(h5, s2)
    net.addLink(h6, s2)
    net.addLink(h7, s5)
    net.addLink(h8, s5)
    net.addLink(h9, s5)
    net.addLink(h12, s4)
    net.addLink(h10, s4)
    net.addLink(h11, s4)
    net.addLink(h13, s3)
    net.addLink(h14, s3)
    net.addLink(h15, s3)

    info( '*** Starting network\n')
    net.start()

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()

