import sys
import numpy as np

#
#   Create a circle and extrude it
#   see: https://wiki.freecadweb.org/Part_scripting

FREECADPATH = 'D:\\Program Files\\FreeCAD 0.20\\bin' # path to your FreeCAD.so or FreeCAD.pyd file
sys.path.append(FREECADPATH)

import FreeCAD
import Part
from FreeCAD import Base
App = FreeCAD

# create edge to extrude:
center = App.Vector(0, 0, 0)
axis = App.Vector(0, 0, 1)
radius = 10
circle = Part.Circle(center, axis, radius)
edge = circle.toShape()
edge_wire = Part.Wire(edge)

# create edge to extrude along:
V1 = App.Vector(0, 0, 0)
V2 = App.Vector(0, 500, 0)
VC1 = App.Vector(0, 250, 250)
C1 = Part.Arc(V1, VC1, V2)

profile = Part.Shape([C1])
profile_wire = Part.Wire([edge])

extruded_face = edge.extrude(App.Vector(0, 10, 10))


doc = App.newDocument()

__o__ = doc.addObject("Part::Feature", 'extruded face')
__o__.Label = 'extruded face'
__o__.Shape = extruded_face

doc.recompute()
doc.saveCopy('extruded.FCStd')


print('done')
