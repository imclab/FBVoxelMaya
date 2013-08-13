from maya.cmds import *
from pymel.core import *

def createShader(shaderType,shaderColor,useTexture):
	target = ls(sl=True)
	shader=shadingNode(shaderType,asShader=True)
	if(useTexture==True):
		file_node=shadingNode("file",asTexture=True)
	shading_group= sets(renderable=True,noSurfaceShader=True,empty=True)
	try:
		setColor(shader,shaderColor)
	except:
		setColor(shader,(0.5,0.5,0.5))
	connectAttr('%s.outColor' %shader ,'%s.surfaceShader' %shading_group)
	if(useTexture==True):
		connectAttr('%s.outColor' %file_node, '%s.color' %shader)
	select(target)
	return shader

def assignShader(shader):
	hyperShade(a=shader)

def quickShader(shaderType,shaderColor,useTexture):
	shader = createShader(shaderType,shaderColor,useTexture)
	assignShader(shader)

def setColor(s,c):
	cc = (float(c[0]) / 255.0, float(c[1]) / 255.0, float(c[2]) / 255.0)
	t = abs(1-(float(c[3]) / 255.0))
	ct = (t,t,t)
	setAttr(s + ".color", cc)
	if(len(c)>3):
		setAttr(s + ".transparency", ct)

shader1 = createShader("blinn",[100,78,55,255],False)
shader2 = createShader("blinn",[153,192,0,95],False)
shader3 = createShader("blinn",[62,81,27,255],False)
shader4 = createShader("blinn",[153,192,0,95],False)
shader5 = createShader("blinn",[52,172,0,100],False)
shader6 = createShader("blinn",[153,192,0,95],False)
shader7 = createShader("blinn",[62,81,27,255],False)
shader8 = createShader("blinn",[153,192,0,95],False)
shader9 = createShader("blinn",[62,81,27,255],False)
shader10 = createShader("blinn",[116,131,30,175],False)
shader11 = createShader("blinn",[153,192,0,95],False)
shader12 = createShader("blinn",[52,172,0,100],False)
shader13 = createShader("blinn",[153,192,0,95],False)
shader14 = createShader("blinn",[62,81,27,255],False)
shader15 = createShader("blinn",[62,81,27,255],False)
shader16 = createShader("blinn",[52,172,0,100],False)
shader17 = createShader("blinn",[62,81,27,255],False)
shader18 = createShader("blinn",[62,81,27,255],False)
shader19 = createShader("blinn",[153,192,0,95],False)
shader20 = createShader("blinn",[62,81,27,255],False)
shader21 = createShader("blinn",[52,172,0,100],False)
shader22 = createShader("blinn",[52,172,0,100],False)
shader23 = createShader("blinn",[62,81,27,255],False)
shader24 = createShader("blinn",[116,131,30,175],False)
shader25 = createShader("blinn",[62,81,27,255],False)
shader26 = createShader("blinn",[153,192,0,95],False)
shader27 = createShader("blinn",[153,192,0,95],False)
shader28 = createShader("blinn",[52,172,0,100],False)
shader29 = createShader("blinn",[52,172,0,100],False)
shader30 = createShader("blinn",[153,192,0,95],False)
shader31 = createShader("blinn",[100,78,55,255],False)
shader32 = createShader("blinn",[100,78,55,255],False)
shader33 = createShader("blinn",[100,78,55,255],False)
shader34 = createShader("blinn",[147,123,60,255],False)
shader35 = createShader("blinn",[100,78,55,255],False)
shader36 = createShader("blinn",[116,131,30,175],False)
shader37 = createShader("blinn",[52,172,0,100],False)
shader38 = createShader("blinn",[62,81,27,255],False)
shader39 = createShader("blinn",[153,192,0,95],False)
shader40 = createShader("blinn",[62,81,27,255],False)
shader41 = createShader("blinn",[116,131,30,175],False)
shader42 = createShader("blinn",[153,192,0,95],False)
shader43 = createShader("blinn",[52,172,0,100],False)
shader44 = createShader("blinn",[116,131,30,175],False)
shader45 = createShader("blinn",[147,123,60,255],False)
shader46 = createShader("blinn",[147,123,60,255],False)
shader47 = createShader("blinn",[147,123,60,255],False)
shader48 = createShader("blinn",[147,123,60,255],False)
shader49 = createShader("blinn",[52,172,0,100],False)
shader50 = createShader("blinn",[52,172,0,100],False)
shader51 = createShader("blinn",[62,81,27,255],False)
shader52 = createShader("blinn",[62,81,27,255],False)
shader53 = createShader("blinn",[52,172,0,100],False)
shader54 = createShader("blinn",[116,131,30,175],False)
shader55 = createShader("blinn",[62,81,27,255],False)
shader56 = createShader("blinn",[62,81,27,255],False)
shader57 = createShader("blinn",[116,131,30,175],False)
shader58 = createShader("blinn",[62,81,27,255],False)
shader59 = createShader("blinn",[153,192,0,95],False)
shader60 = createShader("blinn",[62,81,27,255],False)
shader61 = createShader("blinn",[116,131,30,175],False)
shader62 = createShader("blinn",[62,81,27,255],False)
shader63 = createShader("blinn",[62,81,27,255],False)
shader64 = createShader("blinn",[62,81,27,255],False)
shader65 = createShader("blinn",[153,192,0,95],False)
shader66 = createShader("blinn",[62,81,27,255],False)
shader67 = createShader("blinn",[62,81,27,255],False)
shader68 = createShader("blinn",[62,81,27,255],False)
shader69 = createShader("blinn",[52,172,0,100],False)
shader70 = createShader("blinn",[62,81,27,255],False)
shader71 = createShader("blinn",[62,81,27,255],False)
shader72 = createShader("blinn",[153,192,0,95],False)
shader73 = createShader("blinn",[52,172,0,100],False)
shader74 = createShader("blinn",[116,131,30,175],False)
shader75 = createShader("blinn",[62,81,27,255],False)
shader76 = createShader("blinn",[62,81,27,255],False)
shader77 = createShader("blinn",[52,172,0,100],False)
shader78 = createShader("blinn",[62,81,27,255],False)
shader79 = createShader("blinn",[62,81,27,255],False)
shader80 = createShader("blinn",[153,192,0,95],False)
shader81 = createShader("blinn",[62,81,27,255],False)
shader82 = createShader("blinn",[52,172,0,100],False)
shader83 = createShader("blinn",[52,172,0,100],False)
shader84 = createShader("blinn",[62,81,27,255],False)
shader85 = createShader("blinn",[116,131,30,175],False)
shader86 = createShader("blinn",[62,81,27,255],False)
shader87 = createShader("blinn",[116,131,30,175],False)
shader88 = createShader("blinn",[116,131,30,175],False)
shader89 = createShader("blinn",[153,192,0,95],False)
shader90 = createShader("blinn",[52,172,0,100],False)
shader91 = createShader("blinn",[52,172,0,100],False)
shader92 = createShader("blinn",[52,172,0,100],False)
shader93 = createShader("blinn",[62,81,27,255],False)
shader94 = createShader("blinn",[153,192,0,95],False)
shader95 = createShader("blinn",[153,192,0,95],False)
shader96 = createShader("blinn",[116,131,30,175],False)

polyCube()
move(3,0,2)
assignShader(shader1)
polyCube()
move(0,7,2)
assignShader(shader2)
polyCube()
move(1,7,2)
assignShader(shader3)
polyCube()
move(1,8,2)
assignShader(shader4)
polyCube()
move(2,6,2)
assignShader(shader5)
polyCube()
move(2,7,1)
assignShader(shader6)
polyCube()
move(2,7,2)
assignShader(shader7)
polyCube()
move(2,8,1)
assignShader(shader8)
polyCube()
move(2,8,2)
assignShader(shader9)
polyCube()
move(2,9,1)
assignShader(shader10)
polyCube()
move(2,9,2)
assignShader(shader11)
polyCube()
move(3,6,2)
assignShader(shader12)
polyCube()
move(3,7,0)
assignShader(shader13)
polyCube()
move(3,7,1)
assignShader(shader14)
polyCube()
move(3,7,2)
assignShader(shader15)
polyCube()
move(3,8,0)
assignShader(shader16)
polyCube()
move(3,8,1)
assignShader(shader17)
polyCube()
move(3,8,2)
assignShader(shader18)
polyCube()
move(3,9,1)
assignShader(shader19)
polyCube()
move(3,9,2)
assignShader(shader20)
polyCube()
move(4,7,0)
assignShader(shader21)
polyCube()
move(4,7,1)
assignShader(shader22)
polyCube()
move(4,7,2)
assignShader(shader23)
polyCube()
move(4,8,1)
assignShader(shader24)
polyCube()
move(4,8,2)
assignShader(shader25)
polyCube()
move(4,9,2)
assignShader(shader26)
polyCube()
move(5,7,2)
assignShader(shader27)
polyCube()
move(5,8,2)
assignShader(shader28)
polyCube()
move(5,9,2)
assignShader(shader29)
polyCube()
move(3,10,2)
assignShader(shader30)
polyCube()
move(2,0,3)
assignShader(shader31)
polyCube()
move(3,0,3)
assignShader(shader32)
polyCube()
move(3,0,4)
assignShader(shader33)
polyCube()
move(3,1,3)
assignShader(shader34)
polyCube()
move(4,0,3)
assignShader(shader35)
polyCube()
move(0,7,3)
assignShader(shader36)
polyCube()
move(0,8,3)
assignShader(shader37)
polyCube()
move(1,7,3)
assignShader(shader38)
polyCube()
move(1,7,4)
assignShader(shader39)
polyCube()
move(1,8,3)
assignShader(shader40)
polyCube()
move(1,8,4)
assignShader(shader41)
polyCube()
move(1,9,3)
assignShader(shader42)
polyCube()
move(1,9,4)
assignShader(shader43)
polyCube()
move(2,5,3)
assignShader(shader44)
polyCube()
move(3,2,3)
assignShader(shader45)
polyCube()
move(3,3,3)
assignShader(shader46)
polyCube()
move(3,4,3)
assignShader(shader47)
polyCube()
move(3,5,3)
assignShader(shader48)
polyCube()
move(4,5,3)
assignShader(shader49)
polyCube()
move(2,6,3)
assignShader(shader50)
polyCube()
move(2,7,3)
assignShader(shader51)
polyCube()
move(2,7,4)
assignShader(shader52)
polyCube()
move(2,7,5)
assignShader(shader53)
polyCube()
move(2,7,6)
assignShader(shader54)
polyCube()
move(2,8,3)
assignShader(shader55)
polyCube()
move(2,8,4)
assignShader(shader56)
polyCube()
move(2,8,5)
assignShader(shader57)
polyCube()
move(2,9,3)
assignShader(shader58)
polyCube()
move(2,9,4)
assignShader(shader59)
polyCube()
move(3,6,3)
assignShader(shader60)
polyCube()
move(3,6,4)
assignShader(shader61)
polyCube()
move(3,7,3)
assignShader(shader62)
polyCube()
move(3,7,4)
assignShader(shader63)
polyCube()
move(3,7,5)
assignShader(shader64)
polyCube()
move(3,7,6)
assignShader(shader65)
polyCube()
move(3,8,3)
assignShader(shader66)
polyCube()
move(3,8,4)
assignShader(shader67)
polyCube()
move(3,8,5)
assignShader(shader68)
polyCube()
move(3,8,6)
assignShader(shader69)
polyCube()
move(3,9,3)
assignShader(shader70)
polyCube()
move(3,9,4)
assignShader(shader71)
polyCube()
move(3,9,5)
assignShader(shader72)
polyCube()
move(4,6,3)
assignShader(shader73)
polyCube()
move(4,6,4)
assignShader(shader74)
polyCube()
move(4,7,3)
assignShader(shader75)
polyCube()
move(4,7,4)
assignShader(shader76)
polyCube()
move(4,7,5)
assignShader(shader77)
polyCube()
move(4,8,3)
assignShader(shader78)
polyCube()
move(4,8,4)
assignShader(shader79)
polyCube()
move(4,8,5)
assignShader(shader80)
polyCube()
move(4,9,3)
assignShader(shader81)
polyCube()
move(4,9,4)
assignShader(shader82)
polyCube()
move(4,9,5)
assignShader(shader83)
polyCube()
move(5,7,3)
assignShader(shader84)
polyCube()
move(5,7,4)
assignShader(shader85)
polyCube()
move(5,8,3)
assignShader(shader86)
polyCube()
move(5,8,4)
assignShader(shader87)
polyCube()
move(5,9,3)
assignShader(shader88)
polyCube()
move(6,7,3)
assignShader(shader89)
polyCube()
move(6,7,4)
assignShader(shader90)
polyCube()
move(6,8,3)
assignShader(shader91)
polyCube()
move(2,10,3)
assignShader(shader92)
polyCube()
move(3,10,3)
assignShader(shader93)
polyCube()
move(3,10,4)
assignShader(shader94)
polyCube()
move(3,11,3)
assignShader(shader95)
polyCube()
move(4,10,3)
assignShader(shader96)