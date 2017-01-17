from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()

def hacerMuralla(largo, alto, direccion, pos, offset):
	if direccion == 'adelante':
		mc.setBlocks(pos.x + offset, pos.y, pos.z + offset, pos.x + largo + offset, pos.y + alto, pos.z + offset, block.STONE.id)
	elif direccion == 'derecha':
		mc.setBlocks(pos.x + offset, pos.y, pos.z + offset, pos.x + offset, pos.y + alto, pos.z + largo + offset, block.STONE.id)
	elif direccion == 'atras':
		mc.setBlocks(pos.x + offset, pos.y, pos.z + offset, pos.x - largo + offset, pos.y + alto, pos.z + offset, block.STONE.id)
	else:
		mc.setBlocks(pos.x + offset, pos.y, pos.z + offset, pos.x + offset, pos.y + alto, pos.z - largo + offset, block.STONE.id)
	return

