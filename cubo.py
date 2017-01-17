from mcpi.minecraft import Minecraft
from muralla import hacerMuralla
from mcpi.vec3 import Vec3

def getPosition():
    mc = Minecraft.create()
    return mc.player.getPos()

def cubo(lado, alto, pos, offset):
	hacerMuralla(lado, alto, 'adelante', pos, offset)
	hacerMuralla(lado, alto, 'derecha', Vec3(pos.x, pos.y, pos.z), offset)
	hacerMuralla(lado, alto, 'atras', Vec3(pos.x + lado, pos.y, pos.z + lado), offset)
	hacerMuralla(lado, alto, 'izquierda', Vec3(pos.x + lado, pos.y, pos.z + lado), offset)
	return
