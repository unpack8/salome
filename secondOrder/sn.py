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
Vertex_1 = geompy.MakeVertexOnCurve(Fixed, 0.5, True)
Vertex_2 = geompy.MakeVertexOnCurve(Load, 0.5, True)
Line_1 = geompy.MakeLineTwoPnt(Vertex_1, Vertex_2)
Face_2 = geompy.MakePartition([Face_1], [Line_1], [], [], geompy.ShapeType["FACE"], 0, [], 0)
Fixed_1 = geompy.CreateGroup(Face_2, geompy.ShapeType["EDGE"])
geompy.UnionIDs(Fixed_1, [4, 14])
Load_1 = geompy.CreateGroup(Face_2, geompy.ShapeType["EDGE"])
geompy.UnionIDs(Load_1, [18, 9])
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( Face_1, 'Face_1' )
geompy.addToStudyInFather( Face_1, Fixed, 'Fixed' )
geompy.addToStudyInFather( Face_1, Load, 'Load' )
geompy.addToStudy( Vertex_1, 'Vertex_1' )
geompy.addToStudy( Vertex_2, 'Vertex_2' )
geompy.addToStudy( Line_1, 'Line_1' )
geompy.addToStudy( Face_2, 'Face_2' )
geompy.addToStudyInFather( Face_2, Fixed_1, 'Fixed' )
geompy.addToStudyInFather( Face_2, Load_1, 'Load' )

###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New()
#smesh.SetEnablePublish( False ) # Set to False to avoid publish in study if not needed or in some particular situations:
                                 # multiples meshes built in parallel, complex and numerous mesh edition (performance)

ConstantMesh = smesh.Mesh(Face_1)
CompositeSegment_1D = ConstantMesh.Segment(algo=smeshBuilder.COMPOSITE)
Number_of_Segments_20 = CompositeSegment_1D.NumberOfSegments(20)
QuadFromMedialAxis_1D2D = ConstantMesh.Quadrangle(algo=smeshBuilder.QUAD_MA_PROJ)
CompositeSegment_1D_1 = ConstantMesh.Segment(algo=smeshBuilder.COMPOSITE,geom=Fixed)
Number_of_Segments_10 = CompositeSegment_1D_1.NumberOfSegments(10)
Fixed_2 = ConstantMesh.GroupOnGeom(Fixed,'Fixed',SMESH.EDGE)
Load_2 = ConstantMesh.GroupOnGeom(Load,'Load',SMESH.EDGE)
Fixed_2.SetColor( SALOMEDS.Color( 0, 0.666667, 0 ))
Load_2.SetColor( SALOMEDS.Color( 0.666667, 0, 0 ))
Number_of_Segments_20.SetNumberOfSegments( 20 )
Number_of_Segments_20.SetScaleFactor( 1 )
Number_of_Segments_20.SetReversedEdges( [ 10, 6 ] )
LeftScalingMesh = smesh.Mesh(Face_1)
CompositeSegment_1D_2 = LeftScalingMesh.Segment(algo=smeshBuilder.COMPOSITE)
QuadFromMedialAxis_1D2D_1 = LeftScalingMesh.Quadrangle(algo=smeshBuilder.QUAD_MA_PROJ)
CompositeSegment_1D_3 = LeftScalingMesh.Segment(algo=smeshBuilder.COMPOSITE,geom=Fixed)
status = LeftScalingMesh.AddHypothesis(Number_of_Segments_10,Fixed)
[ Fixed_2, Load_2 ] = ConstantMesh.GetGroups()
Number_of_Segments_20.SetDistrType( 0 )
Number_of_Segments_20.SetNumberOfSegments( 20 )
status = LeftScalingMesh.RemoveHypothesis(QuadFromMedialAxis_1D2D)
ScalingLeft_1 = CompositeSegment_1D_2.NumberOfSegments(20,None,[ 10, 6 ])
Quadrangle_2D = LeftScalingMesh.Quadrangle(algo=smeshBuilder.QUADRANGLE)
[ Fixed_2, Load_2 ] = ConstantMesh.GetGroups()
CompositeSegment_1D_4 = smesh.CreateHypothesis( "CompositeSegment_1D" )
Quadrangle_2D_1 = smesh.CreateHypothesis( "Quadrangle_2D" )
ScalingCorners = smesh.CreateHypothesis('NumberOfSegments')
CompositeSegment_1D_5 = smesh.CreateHypothesis( "CompositeSegment_1D" )
ScalingCorners.SetNumberOfSegments( 5 )
ScalingCorners.SetConversionMode( 1 )
ScalingCorners.SetReversedEdges( [ 4 ] )
ScalingCorners.SetObjectEntry( "Face_2" )
ScalingCorners.SetTableFunction( [ 0, 1, 1, 5 ] )
ScalingLeft_1.SetNumberOfSegments( 20 )
ScalingLeft_1.SetConversionMode( 1 )
ScalingLeft_1.SetReversedEdges( [ 10, 6 ] )
ScalingLeft_1.SetTableFunction( [ 0, 1, 1, 10 ] )
CornerScalingMesh = smesh.Mesh(Face_2)
CompositeSegment_1D_6 = CornerScalingMesh.Segment(algo=smeshBuilder.COMPOSITE)
Quadrangle_2D_2 = CornerScalingMesh.Quadrangle(algo=smeshBuilder.QUADRANGLE)
ScalingLeft_1.SetNumberOfSegments( 20 )
ScalingLeft_1.SetConversionMode( 1 )
ScalingLeft_1.SetReversedEdges( [ 16, 11, 7 ] )
ScalingLeft_1.SetTableFunction( [ 0, 1, 1, 10 ] )
ScalingLeft_1.SetNumberOfSegments( 20 )
ScalingLeft_1.SetConversionMode( 1 )
ScalingLeft_1.SetReversedEdges( [ 16, 11 ] )
ScalingLeft_1.SetTableFunction( [ 0, 10, 1, 1 ] )
ScalingLeft_2 = CompositeSegment_1D_6.NumberOfSegments(10,None,[ 16, 7, 11 ])
ScalingLeft_2.SetNumberOfSegments( 10 )
ScalingLeft_2.SetConversionMode( 1 )
ScalingLeft_2.SetReversedEdges( [ 16, 7, 11 ] )
ScalingLeft_2.SetTableFunction( [ 0, 1, 1, 10 ] )
CompositeSegment_1D_7 = CornerScalingMesh.Segment(algo=smeshBuilder.COMPOSITE,geom=Fixed_1)
status = CornerScalingMesh.AddHypothesis(ScalingCorners,Fixed_1)
ScalingCorners.SetNumberOfSegments( 5 )
ScalingCorners.SetConversionMode( 1 )
ScalingCorners.SetReversedEdges( [ 4 ] )
ScalingCorners.SetObjectEntry( "Face_2" )
ScalingCorners.SetTableFunction( [ 0, 1, 1, 5 ] )
Propagation_of_1D_Hyp = CompositeSegment_1D_1.Propagation()
[ Fixed_2, Load_2 ] = ConstantMesh.GetGroups()
Propagation_of_1D_Hyp_1 = CompositeSegment_1D_3.Propagation()
isDone = LeftScalingMesh.Compute()
Propagation_of_1D_Hyp_2 = CompositeSegment_1D_7.Propagation()
isDone = CornerScalingMesh.Compute()
[ Fixed_2, Load_2 ] = ConstantMesh.GetGroups()
smesh.SetName(ConstantMesh, 'ConstantMesh')
try:
  ConstantMesh.ExportMED(r'/home/unpack/salome_meca/Projects/KursSecondTry/Rectangle_ConstantHorizontalPressure_Files/RunCase_1/Result-Stage_1/_ExportedFromSalomeObject_0_1_2_3.med',auto_groups=0,minor=-1,overwrite=1,meshPart=None,autoDimension=1)
  pass
except:
  print('ExportMED() failed. Invalid file name?')
[ Fixed_2, Load_2 ] = ConstantMesh.GetGroups()
smesh.SetName(ConstantMesh, 'ConstantMesh')
try:
  ConstantMesh.ExportMED(r'/home/unpack/salome_meca/Projects/KursSecondTry/Rectangle_ConstantHorizontalPressure_Files/RunCase_1/Result-Stage_1/_ExportedFromSalomeObject_0_1_2_3.med',auto_groups=0,minor=-1,overwrite=1,meshPart=None,autoDimension=1)
  pass
except:
  print('ExportMED() failed. Invalid file name?')
smesh.SetName(ConstantMesh, 'ConstantMesh')
try:
  ConstantMesh.ExportMED(r'/home/unpack/salome_meca/Projects/KursSecondTry/Rectangle_ConstantHorizontalPressure_Files/RunCase_1/Result-Stage_1/_ExportedFromSalomeObject_0_1_2_3.med',auto_groups=0,minor=-1,overwrite=1,meshPart=None,autoDimension=1)
  pass
except:
  print('ExportMED() failed. Invalid file name?')
smesh.SetName(ConstantMesh, 'ConstantMesh')
try:
  ConstantMesh.ExportMED(r'/home/unpack/salome_meca/Projects/KursSecondTry/Rectangle_ConstantHorizontalPressure_Files/RunCase_1/Result-Stage_1/_ExportedFromSalomeObject_0_1_2_3.med',auto_groups=0,minor=-1,overwrite=1,meshPart=None,autoDimension=1)
  pass
except:
  print('ExportMED() failed. Invalid file name?')
[ Fixed_2, Load_2 ] = ConstantMesh.GetGroups()
smesh.SetName(ConstantMesh, 'ConstantMesh')
try:
  ConstantMesh.ExportMED(r'/home/unpack/salome_meca/Projects/KursSecondTry/Rectangle_ConstantHorizontalPressure_Files/RunCase_1/Result-Stage_1/_ExportedFromSalomeObject_0_1_2_3.med',auto_groups=0,minor=-1,overwrite=1,meshPart=None,autoDimension=1)
  pass
except:
  print('ExportMED() failed. Invalid file name?')
[ Fixed_2, Load_2 ] = ConstantMesh.GetGroups()
smesh.SetName(ConstantMesh, 'ConstantMesh')
try:
  ConstantMesh.ExportMED(r'/home/unpack/salome_meca/Projects/KursSecondTry/Rectangle_ConstantHorizontalPressure_Files/RunCase_1/Result-Stage_1/_ExportedFromSalomeObject_0_1_2_3.med',auto_groups=0,minor=-1,overwrite=1,meshPart=None,autoDimension=1)
  pass
except:
  print('ExportMED() failed. Invalid file name?')
[ Fixed_2, Load_2 ] = ConstantMesh.GetGroups()
smesh.SetName(ConstantMesh, 'ConstantMesh')
try:
  ConstantMesh.ExportMED(r'/home/unpack/salome_meca/Projects/KursSecondTry/Rectangle_ConstantHorizontalPressure_Files/RunCase_1/Result-Stage_1/_ExportedFromSalomeObject_0_1_2_3.med',auto_groups=0,minor=-1,overwrite=1,meshPart=None,autoDimension=1)
  pass
except:
  print('ExportMED() failed. Invalid file name?')
status = ConstantMesh.RemoveHypothesis(CompositeSegment_1D)
status = ConstantMesh.RemoveHypothesis(QuadFromMedialAxis_1D2D)
status = ConstantMesh.RemoveHypothesis(Number_of_Segments_20)
NETGEN_1D_2D = ConstantMesh.Triangle(algo=smeshBuilder.NETGEN_1D2D)
NETGEN_2D_Parameters_1 = NETGEN_1D_2D.Parameters()
NETGEN_2D_Parameters_1.SetMaxSize( 11.1803 )
NETGEN_2D_Parameters_1.SetMinSize( 3.72678 )
NETGEN_2D_Parameters_1.SetSecondOrder( 1 )
NETGEN_2D_Parameters_1.SetFineness( 2 )
NETGEN_2D_Parameters_1.SetChordalError( -1 )
NETGEN_2D_Parameters_1.SetChordalErrorEnabled( 0 )
NETGEN_2D_Parameters_1.SetUseSurfaceCurvature( 1 )
NETGEN_2D_Parameters_1.SetFuseEdges( 1 )
NETGEN_2D_Parameters_1.SetWorstElemMeasure( 22045 )
NETGEN_2D_Parameters_1.SetUseDelauney( 0 )
[ Fixed_2, Load_2 ] = ConstantMesh.GetGroups()
NETGEN_2D_Parameters_1.SetOptimize( 0 )
NETGEN_2D_Parameters_1.SetQuadAllowed( 1 )
NETGEN_2D_Parameters_1.SetCheckChartBoundary( 112 )
isDone = ConstantMesh.Compute()
[ Fixed_2, Load_2 ] = ConstantMesh.GetGroups()
smesh.SetName(ConstantMesh, 'ConstantMesh')
try:
  ConstantMesh.ExportMED(r'/home/unpack/salome_meca/Projects/KursSecondTry/Rectangle_ConstantHorizontalPressure_Files/RunCase_2/Result-Stage_1/_ExportedFromSalomeObject_0_1_2_3.med',auto_groups=0,minor=-1,overwrite=1,meshPart=None,autoDimension=1)
  pass
except:
  print('ExportMED() failed. Invalid file name?')
Sub_mesh_1 = CompositeSegment_1D_1.GetSubMesh()
Sub_mesh_2 = CompositeSegment_1D_3.GetSubMesh()
Sub_mesh_3 = CompositeSegment_1D_7.GetSubMesh()


## Set names of Mesh objects
smesh.SetName(CompositeSegment_1D.GetAlgorithm(), 'CompositeSegment_1D')
smesh.SetName(Quadrangle_2D.GetAlgorithm(), 'Quadrangle_2D')
smesh.SetName(QuadFromMedialAxis_1D2D.GetAlgorithm(), 'QuadFromMedialAxis_1D2D')
smesh.SetName(Number_of_Segments_10, 'Number of Segments_10')
smesh.SetName(NETGEN_1D_2D.GetAlgorithm(), 'NETGEN 1D-2D')
smesh.SetName(Number_of_Segments_20, 'Number of Segments_20')
smesh.SetName(ScalingCorners, 'ScalingCorners')
smesh.SetName(ScalingLeft_1, 'ScalingLeft_1')
smesh.SetName(ScalingLeft_2, 'ScalingLeft_2')
smesh.SetName(ConstantMesh.GetMesh(), 'ConstantMesh')
smesh.SetName(LeftScalingMesh.GetMesh(), 'LeftScalingMesh')
smesh.SetName(CornerScalingMesh.GetMesh(), 'CornerScalingMesh')
smesh.SetName(Sub_mesh_2, 'Sub-mesh_2')
smesh.SetName(Sub_mesh_3, 'Sub-mesh_3')
smesh.SetName(NETGEN_2D_Parameters_1, 'NETGEN 2D Parameters_1')
smesh.SetName(Propagation_of_1D_Hyp_2, 'Propagation of 1D Hyp. on Opposite Edges_3')
smesh.SetName(Propagation_of_1D_Hyp_1, 'Propagation of 1D Hyp. on Opposite Edges_2')
smesh.SetName(Propagation_of_1D_Hyp, 'Propagation of 1D Hyp. on Opposite Edges_1')
smesh.SetName(Fixed_2, 'Fixed')
smesh.SetName(Load_2, 'Load')
smesh.SetName(Sub_mesh_1, 'Sub-mesh_1')

###
### ASTERSTUDY component
###

###
### PARAVIS component
###

import pvsimple
pvsimple.ShowParaviewView()
# trace generated using paraview version 5.6.0-RC1

#### import the simple module from the paraview
from pvsimple import *
#### disable automatic camera reset on 'Show'
pvsimple._DisableFirstRenderCameraReset()

# create a new 'MED Reader'
mEDReader1 = MEDReader(FileName='/home/unpack/salome_meca/Projects/KursSecondTry/Constant_ConstantHorizontalPressure.rmed')

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1472, 672]

# show data in view
mEDReader1Display = Show(mEDReader1, renderView1)

# trace defaults for the display properties.
mEDReader1Display.Representation = 'Surface'

# set scalar coloring
ColorBy(mEDReader1Display, ('POINTS', 'result__DEPL', 'Magnitude'))

# rescale color and/or opacity maps used to exactly fit the current data range
mEDReader1Display.RescaleTransferFunctionToDataRange(False, True)

# reset view to fit data
renderView1.ResetCamera()

# reset view to fit data
renderView1.ResetCamera()

# get color transfer function/color map for 'result__DEPL'
result__DEPLLUT = GetColorTransferFunction('result__DEPL')

# get opacity transfer function/opacity map for 'result__DEPL'
result__DEPLPWF = GetOpacityTransferFunction('result__DEPL')

# change representation type
mEDReader1Display.SetRepresentationType('Surface With Edges')

# Properties modified on mEDReader1
mEDReader1.AllArrays = ['TS0/mesh/ComSup0/result__DEPL@@][@@P1']
mEDReader1.GenerateVectors = 1

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on mEDReader1Display
mEDReader1Display.InputVectors = ['POINTS', 'result__DEPL_Vector']

# Properties modified on mEDReader1Display
mEDReader1Display.SelectInputVectors = ['POINTS', 'result__DEPL_Vector']

# set scalar coloring
ColorBy(mEDReader1Display, ('POINTS', 'result__DEPL', 'DX'))

# rescale color and/or opacity maps used to exactly fit the current data range
mEDReader1Display.RescaleTransferFunctionToDataRange(False, False)

# Update a scalar bar component title.
UpdateScalarBarsComponentTitle(result__DEPLLUT, mEDReader1Display)

# set scalar coloring
ColorBy(mEDReader1Display, ('POINTS', 'result__DEPL', 'DY'))

# rescale color and/or opacity maps used to exactly fit the current data range
mEDReader1Display.RescaleTransferFunctionToDataRange(False, False)

# Update a scalar bar component title.
UpdateScalarBarsComponentTitle(result__DEPLLUT, mEDReader1Display)

# change representation type
mEDReader1Display.SetRepresentationType('Point Gaussian')

# change representation type
mEDReader1Display.SetRepresentationType('Points')

# change representation type
mEDReader1Display.SetRepresentationType('Point Gaussian')

# change representation type
mEDReader1Display.SetRepresentationType('Surface With Edges')

# change representation type
mEDReader1Display.SetRepresentationType('Point Gaussian')

# change representation type
mEDReader1Display.SetRepresentationType('Surface With Edges')

# Properties modified on mEDReader1
mEDReader1.AllArrays = ['TS0/mesh/ComSup0/result__DEPL@@][@@P1', 'TS0/mesh/ComSup0/result__SIEQ_NOEU@@][@@P1']

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(mEDReader1Display, ('POINTS', 'result__SIEQ_NOEU_Vector', 'Magnitude'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(result__DEPLLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
mEDReader1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
mEDReader1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'result__SIEQ_NOEU_Vector'
result__SIEQ_NOEU_VectorLUT = GetColorTransferFunction('result__SIEQ_NOEU_Vector')

# get opacity transfer function/opacity map for 'result__SIEQ_NOEU_Vector'
result__SIEQ_NOEU_VectorPWF = GetOpacityTransferFunction('result__SIEQ_NOEU_Vector')

# set scalar coloring
ColorBy(mEDReader1Display, ('POINTS', 'result__SIEQ_NOEU_Vector', 'VMIS'))

# rescale color and/or opacity maps used to exactly fit the current data range
mEDReader1Display.RescaleTransferFunctionToDataRange(False, False)

# Update a scalar bar component title.
UpdateScalarBarsComponentTitle(result__SIEQ_NOEU_VectorLUT, mEDReader1Display)

# set scalar coloring
ColorBy(mEDReader1Display, ('POINTS', 'result__SIEQ_NOEU', 'Magnitude'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(result__SIEQ_NOEU_VectorLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
mEDReader1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
mEDReader1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'result__SIEQ_NOEU'
result__SIEQ_NOEULUT = GetColorTransferFunction('result__SIEQ_NOEU')

# get opacity transfer function/opacity map for 'result__SIEQ_NOEU'
result__SIEQ_NOEUPWF = GetOpacityTransferFunction('result__SIEQ_NOEU')

# set scalar coloring
ColorBy(mEDReader1Display, ('POINTS', 'result__DEPL_Vector', 'Magnitude'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(result__SIEQ_NOEULUT, renderView1)

# rescale color and/or opacity maps used to include current data range
mEDReader1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
mEDReader1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'result__DEPL_Vector'
result__DEPL_VectorLUT = GetColorTransferFunction('result__DEPL_Vector')

# get opacity transfer function/opacity map for 'result__DEPL_Vector'
result__DEPL_VectorPWF = GetOpacityTransferFunction('result__DEPL_Vector')

# set scalar coloring
ColorBy(mEDReader1Display, ('POINTS', 'result__DEPL_Vector', 'DX'))

# rescale color and/or opacity maps used to exactly fit the current data range
mEDReader1Display.RescaleTransferFunctionToDataRange(False, False)

# Update a scalar bar component title.
UpdateScalarBarsComponentTitle(result__DEPL_VectorLUT, mEDReader1Display)

# set scalar coloring
ColorBy(mEDReader1Display, ('POINTS', 'result__DEPL_Vector', 'DY'))

# rescale color and/or opacity maps used to exactly fit the current data range
mEDReader1Display.RescaleTransferFunctionToDataRange(False, False)

# Update a scalar bar component title.
UpdateScalarBarsComponentTitle(result__DEPL_VectorLUT, mEDReader1Display)

# change representation type
mEDReader1Display.SetRepresentationType('Streaming Particles')

# change representation type
mEDReader1Display.SetRepresentationType('Stream Lines')

# change representation type
mEDReader1Display.SetRepresentationType('Outline')

# change representation type
mEDReader1Display.SetRepresentationType('Point Gaussian')

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [0.0, 0.0, 147.52242393313352]
renderView1.CameraParallelScale = 55.90169943749474


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
