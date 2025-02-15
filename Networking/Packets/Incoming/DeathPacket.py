class DeathPacket:
    def __init__(self):
        self.type = "DEATH"
        self.accountId = ""
        self.charId = 0
        self.killedBy = ""
        self.zombieType = 0
        self.zombieId = 0
        self.isZombie = False

    def read(self, reader):
        self.accountId = reader.readStr()
        self.charId = reader.readInt32()
        self.killedBy = reader.readStr()
        self.zombieType = reader.readInt32()
        self.zombieId = reader.readInt32()
        self.isZombie = self.zombieId != -1

    def write(self, writer):
        writer.writeStr(self.accountId)
        writer.writeInt32(self.charId)
        writer.writeStr(self.killedBy)
        writer.writeInt32(self.zombieType)
        writer.writeInt32(self.zombieId)
