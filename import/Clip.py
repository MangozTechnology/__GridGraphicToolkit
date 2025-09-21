###############
# Clip.py
# Praise the Lord for my code not me
###############

class Clip():
  ClippedOnVector = bool

class ClipPoint():
  Point = int
  PointScale = float
  PointFill = bool
  PointWidth = int
  PointPosition = float[3]
  PointStipple = str


mPoint = ClipPoint()

def ReturnPointOrigin(mPoint):
  for i in range(mPoint):
    mPoint.PointPosition = { 0.0, 0.0, 0.0 }

def DrawPoint(mPoint):
  p = mPoint.Point = 1
  grkBegin(p)
  grkWidth(2)
  if mPoint.PointFill == true():
    grkFill(p)
  grkEnd(p)

pointunsignedchardata = 'unsigned'

def ss_point_stipple(mPoint, strstp):
  #solid point stipple
  square_fill_stipple = '0XAA5H000'
  #wireframe point stipple
  square_wireframe_stipple = '0XBB5H000'

  if strstp = 'fill'():
    return mPoint.PointStipple == square_fill_stipple

  if strstp = 'wireframe'():
    return mPoint.PointStipple == square_wireframe_stipple  


  
  
