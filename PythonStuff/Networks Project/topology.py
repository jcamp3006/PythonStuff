#!/usr/bin/python

""" Setting the position of Nodes (only for Stations and Access Points) and providing mobility using mobility models."""

import os
from mininet.net import Mininet
from mininet.node import Controller,RemoteController
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.link import Intf
from mininet.log import setLogLevel,info

def myNetwork():

	"Create a network."
	net = Mininet( topo=None, build=False )

	info('*** Adding Controller\n')
	net.addController(name='c0')

	print "*** Add Access Points\n"
	s1=net.addSwitch('s1')

	info('*** Add hosts\n')
	h1 = net.addHost('h1',ip='10.0.0.1')
	h2 = net.addHost('h2',ip='10.0.0.2')
	h3 = net.addHost('h3', ip='10.0.0.3')
	info('*** Add links\n')
	net.addLink(h1,s1,cls=TCLink,bw=10,delay='1ms',loss=0)
	net.addLink(h2,s1,cls=TCLink,bw=10,delay='1ms',loss=0)
	net.addLink(h3,s1,cls=TCLink,bw=10,delay='1ms',loss=0) 
	print "*** Starting network"
	net.start()
	CLI(net)
	net.stop()


if __name__ == '__main__':
	setLogLevel('info')
	myNetwork()
