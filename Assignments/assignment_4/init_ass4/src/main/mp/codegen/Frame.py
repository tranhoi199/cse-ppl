from Utils import *

class Frame():
    def __init__(self, name, returnType):
        #name: String
        #returnType: Type

        self.name = name
        self.returnType = returnType
        self.currentLabel = 0
        self.currOpStackSize = 0
        self.maxOpStackSize = 0
        self.currIndex = 0
        self.maxIndex = 0
        self.startLabel = list()
        self.endLabel = list()
        self.indexLocal = list()
        self.conLabel = list()
        self.brkLabel = list()

    def getCurrIndex(self):
        return self.currIndex

    def setCurrIndex(self, index):
        #index: Int

        self.currIndex = index

    '''
    *   return a new label in the method.
    *   @return an integer representing the label.
    '''
    def getNewLabel(self):
        tmp = self.currentLabel
        self.currentLabel = self.currentLabel + 1
        return tmp

    '''
    *   simulate an instruction that pushes a value onto operand stack.
    '''
    def push(self):
        self.currOpStackSize = self.currOpStackSize + 1
        if self.maxOpStackSize < self.currOpStackSize:
            self.maxOpStackSize = self.currOpStackSize

    '''
    *   simulate an instruction that pops a value out of operand stack.
    '''
    def pop(self):
        self.currOpStackSize = self.currOpStackSize - 1
        if self.currOpStackSize < 0:
            raise IllegalRuntimeException("Pop empty stack")

    def getStackSize(self):
        return self.currOpStackSize

    '''
    *   return the maximum size of the operand stack that the method needs to use.
    *   @return an integer that represent the maximum stack size
    '''
    def getMaxOpStackSize(self):
        return self.maxOpStackSize

    '''
    *   check if the operand stack is empty or not.
    *   @throws IllegalRuntimeException if the operand stack is not empty.
    '''
    def checkOpStack(self):
        if self.currOpStackSize != 0:
            raise IllegalRuntimeException("Stack not empty")

    '''
    *   invoked when parsing into a new scope inside a method.<p>
    *   This method will create 2 new labels that represent the starting and ending points of the scope.<p>
    *   Then, these labels are pushed onto corresponding stacks.<p>
    *   These labels can be retrieved by getStartLabel() and getEndLabel().<p>
    *   In addition, this method also saves the current index of local variable.
    '''

    def enterScope(self, isProc):
        #isProc: Boolean
        start = self.getNewLabel()
        end = self.getNewLabel()
        self.startLabel.append(start)
        self.endLabel.append(end)
        self.indexLocal.append(self.currIndex)
        if isProc:
            self.maxOpStackSize = 0
            self.maxIndex = 0

    '''
    *   invoked when parsing out of a scope in a method.<p>
    *   This method will pop the starting and ending labels of this scope
    *   and restore the current index
    '''
    def exitScope(self):
        if not self.startLabel or not self.endLabel or not self.indexLocal:
            raise IllegalRuntimeException("Error when exit scope")
        self.startLabel.pop()
        self.endLabel.pop()
        self.currIndex = self.indexLocal.pop()

    '''
    *   return the starting label of the current scope.
    *   @return an integer representing the starting label
    '''
    def getStartLabel(self):
        if not self.startLabel:
            raise IllegalRuntimeException("None start label")
        return self.startLabel[-1]

    '''
    *   return the ending label of the current scope.
    *   @return an integer representing the ending label
    '''
    def getEndLabel(self):
        if not self.endLabel:
            raise IllegalRuntimeException("None end label")
        return self.endLabel[-1]

    '''
    *   return a new index for a local variable declared in a scope. 
    *   @return an integer that represents the index of the local variable
    '''
    def getNewIndex(self):
        tmp = self.currIndex
        self.currIndex = self.currIndex + 1
        if self.currIndex > self.maxIndex:
            self.maxIndex = self.currIndex
        return tmp

    '''
    *   return the maximum index used in generating code for the current method
    *   @return an integer representing the maximum index
    '''
    def getMaxIndex(self):
        return self.maxIndex

    '''
    *   invoked when parsing into a loop statement.<p>
    *   This method creates 2 new labels that represent the starting and ending label of the loop.<p>
    *   These labels are pushed onto corresponding stacks and are retrieved by getBeginLoopLabel() and getEndLoopLabel().
    '''
    def enterLoop(self):
        con = self.getNewLabel()
        brk = self.getNewLabel()
        self.conLabel.append(con)
        self.brkLabel.append(brk)

    '''
    *   invoked when parsing out of a loop statement.
    *   This method will take 2 labels representing the starting and ending labels of the current loop out of its stacks.
    '''
    def exitLoop(self):
        if not self.conLabel or not self.brkLabel:
            raise IllegalRuntimeException("Error when exit loop")
        self.conLabel.pop()
        self.brkLabel.pop()

    '''
    *   return the label of the innest enclosing loop to which continue statement would jump
    *   @return an integer representing the continue label
    '''
    def getContinueLabel(self):
        if not self.conLabel:
            raise IllegalRuntimeException("None continue label")
        return self.conLabel[-1]

    '''
    *   return the label of the innest enclosing loop to which break statement would jump
    *   @return an integer representing the break label
    '''
    def getBreakLabel(self):
        if not brkLabel:
            raise IllegalRuntimeException("None break label")
        return self.brkLabel[-1]
