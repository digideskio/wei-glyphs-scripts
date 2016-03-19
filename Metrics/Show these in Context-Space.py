#MenuTitle: Show these in Context (Space separated items)
# -*- coding: utf-8 -*-
__doc__="""
Show selected items, each separated by /space, in spacing context in a new tab.
"""
import GlyphsApp
from PyObjCTools.AppHelper import callAfter
import kernMakerFunc
reload(kernMakerFunc)
from kernMakerFunc import kernMaker

# Glyphs.clearLog()
Font = Glyphs.font
Doc = Glyphs.currentDocument
selectedLayers = Font.selectedLayers

TextStoreage = Doc.windowController().activeEditViewController().graphicView().textStorage()
String = TextStoreage.text().string()

editString = ""

# Get the name of each selected glyph and insert a '/space\n/space' for new line character instead (/space added to slit this into it's own item)
namesOfSelectedGlyphs = ''.join([ "/%s" % l.parent.name if hasattr(l.parent, 'name') else '/space\n/space' for l in selectedLayers ])
# namesOfSelectedGlyphs = ''.join([ "/%s" % l.parent.name for l in selectedLayers if hasattr(l.parent, 'name')])

editList = namesOfSelectedGlyphs.split('/space')
# Removed blank items which were added as a result of filtering out new line characters
editList = filter(None, editList)

print editList

for eachItem in editList:
	if eachItem == u"\n":
		editString += "\n"
	else:
		editString += kernMaker(eachItem)

editString = "{0}\n{1}".format(String, editString)

# print editString
# callAfter( Doc.windowController().addTabWithString_, editString )
Font.newTab(editString)