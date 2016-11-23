from datetime import datetime


class MessageLogAdaptor:
    def __init__(self, connection, messageLog):
        self.connection = connection
        self.messageLog = messageLog

        self.messageCache = []

        for message in self.connection.messages:

            msgType = message.msgType
            senderCompId = message.getField(connection.codec.protocol.fixtags.SenderCompID)
            targetCompId = message.getField(connection.codec.protocol.fixtags.TargetCompID)
            seqNo = message.getField(connection.codec.protocol.fixtags.MsgSeqNum)

            timestamp = datetime.now()
            details = {"timestamp": timestamp, "message": message, "summary": "{}] {} {} {} --> {}".format(timestamp, senderCompId, seqNo, connection.codec.protocol.msgtype.msgTypeToName(msgType), targetCompId)}
            self.messageCache.append(details)
            self.messageLog.addMessage(details["summary"])

            self.messageLog.onSelection(self.selectMessage)

    def selectMessage(self, index):
        message = self.messageCache[index]
