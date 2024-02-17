import numpy as np
from PyQt6.QtGui import QVector2D
from PyQt6.QtOpenGL import QOpenGLBuffer


class SpriteInfo():

    def getInfo(self, doc, spriteNames):
        docObject = doc.object()
        metaObject = docObject["meta"].toObject()
        sizeObject = metaObject["size"].toObject()
        atlasW = sizeObject["w"].toDouble()
        atlasH = sizeObject["h"].toDouble()

        vertPositions = []
        texCoords = []
        spriteSizes = []
        framesObject = docObject["frames"].toObject()

        for spriteName in spriteNames:
            vertPositions.extend([
                -0.5, 0.5,
                -0.5, -0.5,
                0.5, 0.5,
                0.5, -0.5])

            spriteObject = framesObject[spriteName].toObject()
            frameObject = spriteObject["frame"].toObject()
            tx = frameObject["x"].toDouble() / atlasW
            ty = frameObject["y"].toDouble() / atlasH
            tw = frameObject["w"].toDouble() / atlasW
            th = frameObject["h"].toDouble() / atlasH
            texCoords.extend([
                tx, ty,
                tx, ty + th,
                tx + tw, ty,
                tx + tw, ty + th])

            spriteW = frameObject["w"].toDouble()
            spriteH = frameObject["h"].toDouble()
            spriteSizes.append(QVector2D(spriteW, spriteH))

        vertPositions = np.array(vertPositions, dtype=np.float32)
        vertPosBuffer = QOpenGLBuffer()
        vertPosBuffer.create()
        vertPosBuffer.bind()
        vertPosBuffer.allocate(vertPositions, len(vertPositions) * 4)

        texCoords = np.array(texCoords, dtype=np.float32)
        texCoordBuffer = QOpenGLBuffer()
        texCoordBuffer.create()
        texCoordBuffer.bind()
        texCoordBuffer.allocate(texCoords, len(texCoords) * 4)

        return {
            "vertPosBuffer": vertPosBuffer,
            "texCoordBuffer": texCoordBuffer,
            "spriteSizes": spriteSizes }
