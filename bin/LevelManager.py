# -*- coding: utf-8 -*-
import os

from Checkpoint import *
from Enviroment import *
from Tile import *


class LevelManager():

	def __init__(self, imageManager, surcefaceManager, spriteManager):
		self.__actualLevel__ = 0
		self.__sprite__ = None
		self.imageManager = imageManager
		self.enviroment = None
		self.surfaceManager = surcefaceManager
		self.spriteManager = spriteManager

		self.levels = self.GetLevels()
		self.tile = Tile(imageManager)
		self.checkpoint = Checkpoint(imageManager)

	def CreateSpriteFromSurface(self):
		sourceface = self.surfaceManager.GetSurface()
		width = self.imageManager.GetImageWidth()
		height = self.imageManager.GetImageHeight()
		self.spriteManager.CreateSpriteFromSurface(0, 0, width*self.tile.Width, height*self.tile.Height, sourceface)

	def GetEnviroment(self):
		if self.enviroment is None:
			raise Exception("Level not rendered")
		return self.enviroment

	def GetLevel(self):
		return self.levels[self.__actualLevel__]

	def GetLevelPath(self):
		return os.path.join('..', 'bin','Resources','levels', self.GetLevel() + '.png')

	def GetLevels(self):
		levels = ["leap_of_faith"]
		levels.append("jumpering")
		levels.append("think_fast")
		levels.append("not_so_hard_maze")
		levels.append("one_jump")
		levels.append("ruins")
		levels.append("jumper")
		levels.append("nl10")
		levels.append("free_runner")
		levels.append("unknown")
		levels.append("nl9")
		levels.append("woah")
		levels.append("roof_climber")
		levels.append("zigzag")
		levels.append("nl7")
		levels.append("jump")
		levels.append("luck")
		levels.append("tower")
		levels.append("cheap_level")
		levels.append("just_an_other_level")
		levels.append("perhaps")
		levels.append("trial")
		levels.append("nl1")
		levels.append("nl6")
		levels.append("nl4")
		levels.append("spam")
		levels.append("nl3")
		levels.append("nl8")
		levels.append("bad_level")
		levels.append("frustration")
		levels.append("nl2")
		levels.append("pure_luck")
		levels.append("wild_guess")
		levels.append("nl5")
		levels.append("fly")

		return levels

	def GetRenderedLevel(self):
		self.LoadAndRenderLevel()
		self.CreateSpriteFromSurface()
		self.GetSprite()

		return self.__sprite__

	def GetSprite(self):
		self.__sprite__ = self.spriteManager.GetSprite()

	def GoToNextLevel(self):
		if(self.__actualLevel__ >= (len(self.levels)-1)):
			self.__actualLevel__ = 0	
		self.__actualLevel__ += 1

		self.LoadAndRenderLevel()
		self.UpdateSpriteFromSurface()
		self.GetSprite()
		
		return self.__sprite__ 

	def LoadAndRenderLevel(self):
		levelPath = self.GetLevelPath()

		self.imageManager.LoadImage(levelPath)
		
		width = self.imageManager.GetImageWidth()
		height = self.imageManager.GetImageHeight()

		pixelArray = self.imageManager.GetPixelArray()

		black = self.imageManager.GetImageColor(0, 0, 0)
		red = self.imageManager.GetImageColor(255, 0, 0)
		green = self.imageManager.GetImageColor(76, 255, 0)

		self.surfaceManager.CreateSurface(width*self.tile.Width, height*self.tile.Height)

		startCord = None
		finishCord = None
		tilesCords = []

		for x in xrange(0,width):
			for y in xrange(0,height):
 				color = self.imageManager.GetPixelArrayItemColor(pixelArray[x, y])
				if color == black:
					if(x != 20):
						self.surfaceManager.BlitIntoSurface(self.tile.Image, x*self.tile.Width, y*self.tile.Height)
						tilesCords.append(Point(x, y))
				elif color == red:
					if(x != 20): startCord = Point(x, y)
				elif color == green:
					if(x != 20): 
						self.surfaceManager.BlitIntoSurface(self.checkpoint.Image, x*self.tile.Width, y*self.tile.Height)
						finishCord = Point(x, y)

		self.enviroment = Enviroment(startCord, finishCord, tilesCords)

	def UpdateSpriteFromSurface(self):
		sourceface = self.surfaceManager.GetSurface()
		width = self.imageManager.GetImageWidth()
		height = self.imageManager.GetImageHeight()
		self.spriteManager.UpdateSpriteFromSurface(0, 0, width*self.tile.Width, height*self.tile.Height, sourceface)