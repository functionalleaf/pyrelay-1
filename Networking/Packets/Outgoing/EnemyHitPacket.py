class EnemyHitPacket:
    def __init__(self):
        self.type = "ENEMYHIT"
        self.time = 0
        self.bulletId = 0
        self.targetId = 0
        self.kill = False

    def write(self, writer):
        writer.writeInt32(self.time)
        writer.writeByte(self.bulletId)
        writer.writeInt32(self.targetId)
        writer.writeBool(self.kill)
