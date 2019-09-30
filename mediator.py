class Mediator:
    """
    Implement cooperative behavior by coordinating Colleague objects.
    Know and maintains its colleagues.
    """

    def __init__(self):
        self.elements = {}
        self.tasks = {}

    def SetElement(self, element):
        if self.elements.get(element.guid) is None:
            self.elements[element.guid] = element

    def SetTasks(self,task):
        if self.tasks.get(task.taskid) is None:
            self.tasks[task.taskid] = task

    def GetElement(self, id):
        return self.elements[id].do()

    def GetTask(self, id):
        return self.tasks[id].do()


class Element:
    """
    Know its Mediator object.
    Communicate with its mediator whenever it would have otherwise
    communicated with another colleague.
    """

    def __init__(self, mediator, guid, taskid):
        self.mediator = mediator
        self.guid = guid
        self.taskid = taskid

    def do(self):
        print("element guid: ", self.guid)

class Task:
    """
    Know its Mediator object.
    Communicate with its mediator whenever it would have otherwise
    communicated with another colleague.
    """

    def __init__(self, mediator, taskid, guid):
        self.mediator = mediator
        self.taskid = taskid
        self.guid = guid

    def do(self):
        print("taskid: ",self.taskid)


def main():
    mediator = Mediator()
    # element class
    element1 = Element(mediator,1,5)
    element2 = Element(mediator,2,6)
    # task class
    task5 = Task(mediator,5,1)
    task6 = Task(mediator,6,2)
    mediator.SetElement(element1)
    mediator.SetElement(element2)
    mediator.SetTasks(task5)
    mediator.SetTasks(task6)

    #element1 find corresponding task attribute
    element1.mediator.GetTask(5)

    #element2 find corresponding task attribute
    element2.mediator.GetTask(6)

    #task5 find corresponding element attribute
    task5.mediator.GetElement(1)

    #task6 find corresponding element attribute
    task6.mediator.GetElement(2)
    print("done")

if __name__ == "__main__":
    main()