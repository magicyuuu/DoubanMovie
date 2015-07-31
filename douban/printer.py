# -*- coding: utf-8 -*-#
import sys


class Printer(object):
    def __init__(self):
        self.xmlstr = '<?xml version="1.0" encoding="utf-8"?>\n'
        self.item = [self.xmlstr]
        self.__start()

    def __start(self):
        self.item.append('<items>\n')

    def __end(self):
        self.item.append('</items>\n')

    def sendToWorkFlow(self):
        self.__end()

        printData = "".join(self.item)
        sys.stdout.write(printData)
        return printData

    def reset(self):
        self.item = [self.xmlstr]

    def add_item(self, title, subtitle='', arg='', icon='', valid=False):
        it = '''<item valid="%s">
        <title>%s</title>
        <subtitle>%s</subtitle>
        <arg><![CDATA[%s]]></arg>
        <icon>%s</icon>
        </item>\n''' % ('yes' if valid else 'no', title, subtitle, arg, icon)
        self.item.append(it)
