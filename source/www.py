#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  www.py
#  
#  Copyright 2012 Átila Camurça <camurca.home@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import gtk
import webkit

browser = None
go_button = None
url_entry = None

def main():
	window = gtk.Window()
	window.set_title("WorldWideWeb")
	window.set_default_size(800, 600)
	window.connect("delete-event", gtk.main_quit)
	
	# window elements
	vbox = gtk.VBox()
	vbox.pack_start(mainbar(), padding=10)
	vbox.pack_start(webview())
	
	go_button.connect("clicked", goclicked)
	
	window.add(vbox)
	window.set_position(gtk.WIN_POS_CENTER)
	window.show_all()
	gtk.main()
	return 0

def mainbar():
	hbox = gtk.HBox()
	global url_entry
	url_entry = gtk.Entry()
	url_entry.set_text("http://localhost:9669/index.html")
	global go_button
	go_button = gtk.Button("Go")
	hbox.pack_start(url_entry, padding=5)
	hbox.pack_start(go_button, False, False, 10)
	return hbox

def goclicked(btn):
	global browser
	browser.open(url_entry.get_text())

def webview():
	global browser
	browser = webkit.WebView()
	browser.open("http://localhost:9669/index.html")
	return browser

if __name__ == '__main__':
	main()

