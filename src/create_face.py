import sys
import numpy as np

FREECADPATH = 'D:\\Program Files\\FreeCAD 0.20\\bin' # path to your FreeCAD.so or FreeCAD.pyd file
sys.path.append(FREECADPATH)

import FreeCAD
import Part
from FreeCAD import Base
App = FreeCAD


App = FreeCAD
doc = App.newDocument("HTCCalculator")

vertices = np.array([[0, 0, 0],
                     [1000, 0, 0],
                     [1000, 1000, 0],
                     [0, 1000, 0]])

# create vectors
vectors = [Base.Vector(row) for row in vertices]

# create wire
wire = Part.makePolygon([*vectors, vectors[0]])

# create a face from the wire
face = Part.Face(wire)

# export to FreeCAD file:
doc = App.newDocument()
__o__ = doc.addObject("Part::Feature", 'Simple face')
__o__.Label = 'Simple face'
__o__.Shape = face

doc.recompute()
doc.saveCopy('test.FCStd')

# export to STEP file:
Part.export(doc.Objects, 'test.stp')

# import file:
doc = FreeCAD.open('test.FCStd')
print(doc.Objects[0])

print(wire)
