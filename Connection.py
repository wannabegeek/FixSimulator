import importlib
from unittest import mock

from pyfix.codec import Codec
from pyfix.message import FIXMessage, FIXContext


class Connection:
    def __init__(self):
        self.isServer = False
        self.messages = []

        protocol = importlib.import_module("pyfix.FIX44")
        self.codec = Codec(protocol)

        s = 1
        mock_session = mock.Mock()
        mock_session.senderCompId = "sender"
        mock_session.targetCompId = "target"
        mock_session.allocateSndSeqNo.return_value = s

        msg = FIXMessage(self.codec.protocol.msgtype.NEWORDERSINGLE)
        msg.setField(self.codec.protocol.fixtags.Price, "123.45")
        msg.setField(self.codec.protocol.fixtags.OrderQty, 9876)
        msg.setField(self.codec.protocol.fixtags.Symbol, "VOD.L")
        msg.setField(self.codec.protocol.fixtags.SecurityID, "GB00BH4HKS39")
        msg.setField(self.codec.protocol.fixtags.SecurityIDSource, "4")
        msg.setField(self.codec.protocol.fixtags.Symbol, "VOD.L")
        msg.setField(self.codec.protocol.fixtags.Account, "TEST")
        msg.setField(self.codec.protocol.fixtags.HandlInst, "1")
        msg.setField(self.codec.protocol.fixtags.ExDestination, "XLON")
        msg.setField(self.codec.protocol.fixtags.Side, 1)
        msg.setField(self.codec.protocol.fixtags.ClOrdID, "abcdefg")
        msg.setField(self.codec.protocol.fixtags.Currency, "GBP")

        rptgrp1 = FIXContext()
        rptgrp1.setField("611", "aaa")
        rptgrp1.setField("612", "bbb")
        rptgrp1.setField("613", "ccc")

        msg.addRepeatingGroup("444", rptgrp1, 0)

        for i in range(0,20):
            encoded = self.codec.pack(msg, mock_session)
            self.messages.append(self.codec.parse(encoded.encode('utf-8'))[0])

    def isServer(self):
        return self.isServer

    def name(self):
        return "A Session"

    def messages(self):
        return self.messages
