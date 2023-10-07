from abc import ABC, abstractmethod


class BaseWorker(ABC):
    @staticmethod
    @abstractmethod
    def work() -> None:
        pass


class Worker(BaseWorker):
    @staticmethod
    def work() -> None:
        print("I'm working!!")


class SuperWorker(BaseWorker):
    @staticmethod
    def work() -> None:
        print("I work very hard!!!")


class LazyWorker(BaseWorker):
    @staticmethod
    def work() -> None:
        print("I rarely work!")


class Manager:
    def __init__(self) -> None:
        self.worker = None

    def set_worker(self, worker) -> None:
        if not isinstance(worker, BaseWorker):
            raise AssertionError(
                f"`worker` must subclass of type {BaseWorker}")

        self.worker = worker

    def manage(self) -> None:
        if self.worker is not None:
            self.worker.work()


worker = Worker()
manager = Manager()
manager.set_worker(worker)
manager.manage()
super_worker = SuperWorker()

try:
    manager.set_worker(super_worker)
    manager.manage()
except AssertionError:
    print("manager fails to support super_worker....")
