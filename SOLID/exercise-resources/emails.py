from abc import ABC, abstractmethod


class IContent(ABC):
    def __init__(self, text) -> None:
        self.text = text

    @abstractmethod
    def format(self) -> str:
        pass


class IM(IContent):
    def format(self) -> str:
        return '\n'.join(["I'm", self.text])


class MyMl(IContent):
    def format(self) -> str:
        return '\n'.join(['<myML>', self.text, '</myML>'])


class HTML(IContent):
    def format(self) -> str:
        return '\n'.join(['<html>', self.text, '</html>'])
    
    
class XML(IContent):
    def format(self) -> str:
        return '\n'.join(['<xml>', self.text, '</xml>'])


class IEmail(ABC):
    @abstractmethod
    def set_sender(self, sender) -> None:
        pass

    @abstractmethod
    def set_receiver(self, receiver) -> None:
        pass

    @abstractmethod
    def set_content(self, content) -> None:
        pass


class Email(IEmail):
    def __init__(self, protocol) -> None:
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender: IContent) -> str:
        self.__sender = sender.format()

    def set_receiver(self, receiver: IContent) -> str:
        self.__receiver = receiver.format()

    def set_content(self, content: IContent) -> str:
        self.__content = content.format()

    def __repr__(self) -> str:
        return f"Sender: {self.__sender}\nReceiver: {self.__receiver}\nContent:\n{self.__content}"


myhtml = HTML('Hello, there!')
email = Email('IM')
email.set_sender('qmal')
email.set_receiver('james')
email.set_content(myhtml)
print(email)