#!/usr/bin/env python

###
### This file is generated automatically by SALOME v9.3.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
import salome_notebook
notebook = salome_notebook.NoteBook()
sys.path.insert(0, r'/home/unpack/salome_meca/Projects/KursSecondTry')

###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS


geompy = geomBuilder.New()

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
Face_1 = geompy.MakeFaceHW(100, 50, 1)
Fixed = geompy.CreateGroup(Face_1, geompy.ShapeType["EDGE"])
geompy.UnionIDs(Fixed, [3])
Load = geompy.CreateGroup(Face_1, geompy.ShapeType["EDGE"])
geompy.UnionIDs(Load, [8])
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( Face_1, 'Face_1' )
geompy.addToStudyInFather( Face_1, Fixed, 'Fixed' )
geompy.addToStudyInFather( Face_1, Load, 'Load' )

###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New()
#smesh.SetEnablePublish( False ) # Set to False to avoid publish in study if not needed or in some particular situations:
                                 # multiples meshes built in parallel, complex and numerous mesh edition (performance)

Segments_16 = smesh.CreateHypothesis('NumberOfSegments')
Segments_16.SetNumberOfSegments( 16 )
CompositeSegment_1D = smesh.CreateHypothesis('CompositeSegment_1D')
Quadrangle_2D = smesh.CreateHypothesis('Quadrangle_2D')
Segments_8 = smesh.CreateHypothesis('NumberOfSegments')
Segments_8.SetNumberOfSegments( 8 )
Propagation_of_1D_Hyp = smesh.CreateHypothesis('Propagation')
Mesh_1 = smesh.Mesh(Face_1)
status = Mesh_1.AddHypothesis(Segments_16)
status = Mesh_1.AddHypothesis(CompositeSegment_1D)
status = Mesh_1.AddHypothesis(Quadrangle_2D)
status = Mesh_1.AddHypothesis(CompositeSegment_1D,Fixed)
status = Mesh_1.AddHypothesis(Segments_8,Fixed)
status = Mesh_1.AddHypothesis(Propagation_of_1D_Hyp,Fixed)
isDone = Mesh_1.Compute()
Mesh_1.ConvertToQuadratic(0, Mesh_1,True)
aCriteria = []
aCriterion = smesh.GetCriterion(SMESH.ALL,SMESH.FT_LinearOrQuadratic,SMESH.FT_Undefined,0)
aCriteria.append(aCriterion)
Sub_mesh_1 = Mesh_1.GetSubMesh( Fixed, 'Sub-mesh_1' )


## Set names of Mesh objects
smesh.SetName(CompositeSegment_1D, 'CompositeSegment_1D')
smesh.SetName(Quadrangle_2D, 'Quadrangle_2D')
smesh.SetName(Segments_8, 'Segments_8')
smesh.SetName(Propagation_of_1D_Hyp, 'Propagation of 1D Hyp. on Opposite Edges_1')
smesh.SetName(Segments_16, 'Segments_16')
smesh.SetName(Mesh_1.GetMesh(), 'Mesh_1')
smesh.SetName(Sub_mesh_1, 'Sub-mesh_1')


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
