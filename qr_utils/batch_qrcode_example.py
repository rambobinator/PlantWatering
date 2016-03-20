#!/usr/bin/env python2.7
# coding: utf8

if __name__ == '__main__':
	from batch_qrcode import batch_qrcode
	
	size = 100
	titles = []
	for id in range(0, size):
	    titles.append("test-{}".format(id))
	
	qrs = batch_qrcode(titles)
	qrs.create_images()
	qrs.create_sheet()
