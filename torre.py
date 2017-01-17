import cubo
from mcpi.vec3 import Vec3
from mcpi.minecraft import Minecraft

def torre(alto, ancho):
	pos = cubo.getPosition()
	offset = 5

	cubo.cubo(alto, ancho, pos, offset)
	
	pos_square = Vec3(pos.x + offset - 1, pos.y + ancho + 1, pos.z + offset - 1)

	mc = Minecraft.create()
	mc.setBlocks(pos_square.x, pos_square.y, pos_square.z, pos_square.x + alto + 2, pos_square.y, pos_square.z + alto + 2, 1)
	return

	
	
