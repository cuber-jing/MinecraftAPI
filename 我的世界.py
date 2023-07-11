# -*- coding:utf-8 -*-
import mcpi.vec3
from mcpi import minecraft
#与游戏取得连接
mc = minecraft.Minecraft.create()
while True:
    if mc.getBlock(mcpi.vec3.Vec3(7,1,-6)) == 0:
        mc.setBlock(mcpi.vec3.Vec3(7,1,-6),46)
