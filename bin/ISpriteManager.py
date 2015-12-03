#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ISpriteManager():

	def CreateSprite(self, xPosition, yPosition, width, height, imagePath):
		raise NotImplementedError("Should have implemented this")

	def CreateSpriteFromSurface(self, xPosition, yPosition, width, height, sourceface):
		raise NotImplementedError("Should have implemented this")

	def GetSprite(self):
		raise NotImplementedError("Should have implemented this")

	def FlipSpriteImage(self):
		raise NotImplementedError("Should have implemented this")

	def UpdateSprite(self, xPosition, yPosition, width = None, height = None, imagePath = None):
		raise NotImplementedError("Should have implemented this")

	def UpdateSpriteFromSurface(self, xPosition, yPosition, width, height, sourceface):
		raise NotImplementedError("Should have implemented this")

	def UpdateSpriteImage(self, imagePath):
		raise NotImplementedError("Should have implemented this")