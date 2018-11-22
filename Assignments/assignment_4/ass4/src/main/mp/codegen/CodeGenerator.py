# Huynh Sam Ha - 1610852

import sys
from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod

# for typing with vscode
from Visitor import BaseVisitor
from AST import *

sys.path.append('../utils')
sys.path.append('../checker')


class StupidUtils:
    @staticmethod
    def isOpForNumberToNumber(operator):
        return str(operator).lower() in ['+', '-', '*', '/', 'div', 'mod']

    @staticmethod
    def isOpForNumberToBoolean(operator):
        return str(operator).lower() in ['<>', '=', '>', '<', '>=', '<=']

    @staticmethod
    def isOpForNumber(operator):
        return StupidUtils.isOpForNumberToNumber(operator) or StupidUtils.isOpForNumberToBoolean(operator)

    @staticmethod
    def mergeNumberType(lType, rType):
        return FloatType() if FloatType in [type(x) for x in [lType, rType]] else IntType()

    @staticmethod
    def retrieveType(originType):
        if type(originType) is ArrayType: return ArrayPointerType(originType.eleType)
        return originType



class CodeGenerator(Utils):
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [
            Symbol("getInt", MType(list(), IntType()), CName(self.libName)),
            Symbol("getFloat", MType(list(), FloatType()), CName(self.libName)),
            Symbol("putInt", MType([IntType()], VoidType()), CName(self.libName)),
            Symbol("putIntLn", MType([IntType()], VoidType()), CName(self.libName)),
            Symbol("putFloat", MType([FloatType()], VoidType()), CName(self.libName)),
            Symbol("putFloatLn", MType([FloatType()], VoidType()), CName(self.libName)),
            Symbol("putBool", MType([BoolType()], VoidType()), CName(self.libName)),
            Symbol("putBoolLn", MType([BoolType()], VoidType()), CName(self.libName)),
            Symbol("putString", MType([StringType()], VoidType()), CName(self.libName)),
            Symbol("putStringLn", MType([StringType()], VoidType()), CName(self.libName)),
            Symbol("putLn", MType([], VoidType()), CName(self.libName))
        ]

    def gen(self, ast, dir_):
        # ast: AST
        # dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)



class ArrayPointerType(Type):
    def __init__(self, ctype):
        # cname: String
        self.eleType = ctype

    def __str__(self):
        return "ArrayPointerType({0})".format(str(self.eleType))

    def accept(self, v, param):
        return None


class ClassType(Type):
    def __init__(self, cname):
        self.cname = cname

    def __str__(self):
        return "Class({0})".format(str(self.cname))

    def accept(self, v, param):
        return None


class SubBody():
    def __init__(self, frame, sym, isGlobal=False):
        # frame: Frame
        # sym: List[Symbol]

        self.frame = frame
        self.sym = sym
        self.isGlobal = isGlobal


class Access():
    def __init__(self, frame, sym, isLeft, isFirst):
        # frame: Frame
        # sym: List[Symbol]
        # isLeft: Boolean
        # isFirst: Boolean

        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst


class Val(ABC):
    pass


class Index(Val):
    def __init__(self, value):
        # value: Int

        self.value = value


class CName(Val):
    def __init__(self, value):
        # value: String

        self.value = value


class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, dir_):
        # astTree: AST
        # env: List[Symbol]
        # dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "MPClass"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")

        self.listGlobalArray = [] # list(VarDecl: array declare global)


    def visitProgram(self, ast: Program, c):
        # c: Any

        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        
        staticDecl = self.env
        for x in ast.decl:
            if type(x) is FuncDecl:
                partype = [i.varType for i in x.param]
                staticDecl = [Symbol(x.name.name, MType(partype, x.returnType), CName(self.className))] + staticDecl
            else:
                newSym = self.visit(x, SubBody(None, None, isGlobal=True))
                staticDecl = [newSym] + staticDecl
        
        e = SubBody(None, staticDecl)
        [self.visit(x, e) for x in ast.decl if type(x) is FuncDecl]

        # generate default constructor
        self.genMETHOD(FuncDecl(Id("<init>"), list(), list(), list(), None), c, Frame("<init>", VoidType))
        self.emit.emitEPILOG()
        return c



    def visitFuncDecl(self, ast: FuncDecl, o: SubBody):
        subctxt = o
        frame = Frame(ast.name.name, ast.returnType)
        self.genMETHOD(ast, subctxt.sym, frame)


    def visitVarDecl(self, ast: VarDecl, o: SubBody):
        subctxt = o
        frame = o.frame
        isGlobal = o.isGlobal
        varName = ast.variable.name
        varType = ast.varType
        if isGlobal:
            self.emit.printout(self.emit.emitATTRIBUTE(varName, StupidUtils.retrieveType(varType), False, ""))
            if type(ast.varType) is ArrayType: 
                self.listGlobalArray.append(ast)
            return Symbol(varName, varType)
        # params
        idx = frame.getNewIndex()
        self.emit.printout(self.emit.emitVAR(idx, varName, StupidUtils.retrieveType(varType), frame.getStartLabel(), frame.getEndLabel(), frame))
        return SubBody(frame, [Symbol(varName, varType, Index(idx))] + subctxt.sym)



    def genMETHOD(self, decl: FuncDecl, o, frame: Frame):
        # o: Any

        glenv = o

        isInit = decl.returnType is None
        isMain = decl.name.name == "main" and len(decl.param) == 0 and type(decl.returnType) is VoidType
        returnType = VoidType() if isInit else decl.returnType
        isProc = type(returnType) is VoidType
        methodName = "<init>" if isInit else decl.name.name
        intype = [ArrayPointerType(StringType())] if isMain else [StupidUtils.retrieveType(x.varType) for x in decl.param]
        mtype = MType(intype, returnType)

        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit, frame))

        frame.enterScope(isProc)

        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayPointerType(
                StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))

        listLocalArray = [] # list(Symbol(name, mtype, value: Index(idx)))
        varList = SubBody(frame, glenv)
        for x in decl.param + decl.local:
            varList = self.visit(x, varList)
            if type(x.varType) is ArrayType:
                listLocalArray.append(varList.sym[0])

        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
            # Init global array declare
            for x in self.listGlobalArray:
                size = x.varType.upper - x.varType.lower + 1
                self.emit.printout(self.emit.emitInitNewStaticArray(self.className + "/" + x.variable.name, size, x.varType.eleType, frame))
        
        # Init local array declare
        for sym in listLocalArray:
            index = sym.value.value
            varType = sym.mtype
            size = varType.upper - varType.lower + 1
            self.emit.printout(self.emit.emitInitNewLocalArray(index, size, varType.eleType, frame))

        list(map(lambda x: self.visit(x, varList), decl.body))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if isProc:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()




# ================   Visit Statements   =================
# Param:    o: SubBody(frame, sym)


    def visitCallStmt(self, ast: CallStmt, o: SubBody):
        ctxt = o
        frame = ctxt.frame
        symbols = ctxt.sym
        self.handleCall(ast, frame, symbols, isStmt=True)



    def handleCall(self, ast, frame, symbols, isStmt=False):
        # ast: CallStmt | CallExpr

        sym = self.lookup(ast.method.name.lower(), symbols, lambda x: x.name.lower())
        cname = sym.value.value
        ctype = sym.mtype
        paramTypes = ctype.partype

        paramsCode = ""
        idx = 0
        for x in ast.param:
            pCode, pType = self.visit(x, Access(frame, symbols, False, True))
            if type(paramTypes[idx]) is FloatType and type(pType) is IntType:
                pCode = pCode + self.emit.emitI2F(frame)
            paramsCode = paramsCode + pCode
            idx = idx + 1

        code = paramsCode + self.emit.emitINVOKESTATIC(cname + "/" + sym.name, ctype, frame) 
        if isStmt: self.emit.printout(code)
        else: return code, ctype.rettype



    def visitReturn(self, ast: Return, o: SubBody):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        retType = frame.returnType
        if not type(retType) is VoidType:
            expCode, expType = self.visit(ast.expr, Access(frame, nenv, False, True))
            if type(retType) is FloatType and type(expType) is IntType:
                expCode = expCode + self.emit.emitI2F(frame)
            self.emit.printout(expCode)
        self.emit.printout(self.emit.emitRETURN(retType, frame))




    def visitIf(self, ast: If, o: SubBody):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        expCode, expType = self.visit(ast.expr, Access(frame, nenv, False, True))
        self.emit.printout(expCode)

        labelT = frame.getNewLabel() # eval is true
        labelE = frame.getNewLabel() # label end

        self.emit.printout(self.emit.emitIFTRUE(labelT, frame)) # false
        # False
        [self.visit(x, o) for x in ast.elseStmt]
        self.emit.printout(self.emit.emitGOTO(labelE, frame)) # go to end
        # True
        self.emit.printout(self.emit.emitLABEL(labelT, frame))
        [self.visit(x, o) for x in ast.thenStmt]
        # End
        self.emit.printout(self.emit.emitLABEL(labelE, frame))



    def visitWhile(self, ast: While, o: SubBody):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        expCode, expType = self.visit(ast.exp, Access(frame, nenv, False, True))
        
        labelS = frame.getNewLabel() # label start
        labelE = frame.getNewLabel() # label end
        frame.enterLoop()
        self.emit.printout(self.emit.emitLABEL(labelS, frame))
        self.emit.printout(expCode)
        self.emit.printout(self.emit.emitIFFALSE(labelE, frame))
        [self.visit(x, o) for x in ast.sl]
        self.emit.printout(self.emit.emitLABEL(frame.getContinueLabel(), frame))
        self.emit.printout(self.emit.emitGOTO(labelS, frame)) # loop
        self.emit.printout(self.emit.emitLABEL(labelE, frame))
        self.emit.printout(self.emit.emitLABEL(frame.getBreakLabel(), frame))
        frame.exitLoop()


    def visitFor(self, ast: For, o: SubBody):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym

        exp1Code, _ = self.visit(ast.expr1, Access(frame, nenv, False, True))
        exp2Code, _ = self.visit(ast.expr2, Access(frame, nenv, False, True))
        lhsWCode, _ = self.visit(ast.id, Access(frame, nenv, True, True)) # Write code
        lhsRCode, _ = self.visit(ast.id, Access(frame, nenv, False, False)) # Read code
        
        labelS = frame.getNewLabel() # label start
        labelE = frame.getNewLabel() # label end

        # Init value
        self.emit.printout(exp1Code)
        self.emit.printout(lhsWCode)
        frame.enterLoop()
        # Loop
        self.emit.printout(self.emit.emitLABEL(labelS, frame))
        # 1. Condition
        self.emit.printout(lhsRCode)
        self.emit.printout(exp2Code)
        if ast.up:
            self.emit.printout(self.emit.emitIFICMPGT(labelE, frame))
        else:
            self.emit.printout(self.emit.emitIFICMPLT(labelE, frame))
        # 2. Statements
        [self.visit(x, o) for x in ast.loop]
        self.emit.printout(self.emit.emitLABEL(frame.getContinueLabel(), frame))
        # 3. Update index
        self.emit.printout(lhsRCode)
        self.emit.printout(self.emit.emitPUSHICONST(1, frame))
        self.emit.printout(self.emit.emitADDOP('+' if ast.up else '-', IntType(), frame))
        self.emit.printout(lhsWCode)

        self.emit.printout(self.emit.emitGOTO(labelS, frame)) # loop
        self.emit.printout(self.emit.emitLABEL(labelE, frame))
        self.emit.printout(self.emit.emitLABEL(frame.getBreakLabel(), frame))
        frame.exitLoop()



    def visitWith(self, ast: With, o: SubBody):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        retType = frame.returnType
        isProc = type(retType) is VoidType

        frame.enterScope(isProc)

        varList = SubBody(frame, nenv)
        for x in ast.decl:
            varList = self.visit(x, varList)

        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        list(map(lambda x: self.visit(x, varList), ast.stmt))
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        frame.exitScope()






    def visitBreak(self, ast: Break, o: SubBody):
        ctxt = o
        frame = ctxt.frame
        self.emit.printout(self.emit.emitGOTO(frame.getBreakLabel(), frame))

    def visitContinue(self, ast: Continue, o: SubBody):
        ctxt = o
        frame = ctxt.frame
        self.emit.printout(self.emit.emitGOTO(frame.getContinueLabel(), frame))




    def visitAssign(self, ast: Assign, o: SubBody):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        # Visit LHS: Id || ArrayCell
        expCode, expType = self.visit(ast.exp, Access(frame, nenv, False, True))
        lhsCode, lhsType = self.visit(ast.lhs, Access(frame, nenv, True, True))
        if type(lhsType) is FloatType and type(expType) is IntType:
            expCode = expCode + self.emit.emitI2F(frame)
        self.emit.printout(expCode)
        self.emit.printout(lhsCode)



# ================   Visit Expression   =================
# Param:    o: Access(frame, sym, isLeft, isFirst)
# Return:   (code, type)

    def visitId(self, ast: Id, o: Access):
        # Return (name, type, index)
        ctxt = o
        frame = ctxt.frame
        symbols = ctxt.sym
        isLeft = ctxt.isLeft
        isFirst = ctxt.isFirst
        sym = self.lookup(ast.name.lower(), symbols, lambda x: x.name.lower())

        # recover status of stack in frame
        if not isFirst and isLeft: frame.push()
        elif not isFirst and not isLeft: frame.pop()
        
        emitType = StupidUtils.retrieveType(sym.mtype)
        isArrayType = type(sym.mtype) is ArrayType
        if sym.value is None: # not index -> global var - static field
            if isLeft and not isArrayType: retCode = self.emit.emitPUTSTATIC(self.className + "/" + sym.name, emitType, frame)
            else: retCode = self.emit.emitGETSTATIC(self.className + "/" + sym.name, emitType, frame)
        else:
            if isLeft and not isArrayType: retCode = self.emit.emitWRITEVAR(sym.name, emitType, sym.value.value, frame)
            else: retCode = self.emit.emitREADVAR(sym.name, emitType, sym.value.value, frame)

        return retCode, sym.mtype


    def visitArrayCell(self, ast: ArrayCell, o: Access):
        ctxt = o
        frame = ctxt.frame
        symbols = ctxt.sym
        isLeft = ctxt.isLeft
        isFirst = ctxt.isFirst
        arrCode, arrType = self.visit(ast.arr, o)
        idxCode, idxType = self.visit(ast.idx, o)
        # aload(address) -> iconst(index) -> iaload
        if isLeft: return arrCode + idxCode + self.emit.emitASTORE(IntType(), frame), arrType
        return arrCode + idxCode + self.emit.emitALOAD(IntType(), frame), arrType


    def visitCallExpr(self, ast: CallExpr, o: Access):
        ctxt = o
        frame = ctxt.frame
        symbols = ctxt.sym
        return self.handleCall(ast, frame, symbols, isStmt=False)



    def visitBinaryOp(self, ast: BinaryOp, o: Access):
        ctxt = o
        frame = ctxt.frame
        op = str(ast.op).lower()
        lCode, lType = self.visit(ast.left, ctxt)
        rCode, rType = self.visit(ast.right, ctxt)
        if StupidUtils.isOpForNumber(op): # for number type
            mType = StupidUtils.mergeNumberType(lType, rType)
            if op == '/': mType = FloatType() # mergeType >= lType, rType
            lCode, rCode = (c if type(t) == type(mType) else c+self.emit.emitI2F(frame) \
                            for c,t in [(lCode, lType), (rCode, rType)])
            if StupidUtils.isOpForNumberToNumber(op):
                if op in ['+', '-']:
                    return lCode + rCode + self.emit.emitADDOP(op, mType, frame), mType
                if op in ['*', '/']:
                    return lCode + rCode + self.emit.emitMULOP(op, mType, frame), mType
                if op == 'div':
                    return lCode + rCode + self.emit.emitDIV(frame), mType
                if op == 'mod':
                    return lCode + rCode + self.emit.emitMOD(frame), mType
            else: # op to boolean: > <= = <>, ...
                return lCode + rCode + self.emit.emitREOP(op, mType, frame), BoolType()
        else: # for boolean type
            mType = BoolType()
            if op == 'or': return lCode + rCode + self.emit.emitOROP(frame), mType
            if op == 'and': return lCode + rCode + self.emit.emitANDOP(frame), mType
            if op == 'orelse': return self.emit.emitORELSE(frame, lCode, rCode), mType
            if op == 'andthen': return self.emit.emitANDTHEN(frame, lCode, rCode), mType



    def visitUnaryOp(self, ast: UnaryOp, o: Access):
        ctxt = o
        frame = ctxt.frame
        op = str(ast.op).lower()
        bCode, bType = self.visit(ast.body, ctxt)
        if op == '-': return bCode + self.emit.emitNEGOP(bType, frame), bType
        if op == 'not': return bCode + self.emit.emitNOT(bType, frame), bType



    def visitIntLiteral(self, ast: IntLiteral, o: Access):
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(ast.value, frame), IntType()

    def visitFloatLiteral(self, ast: FloatLiteral, o: Access):
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHFCONST(str(ast.value), frame), FloatType()

    def visitBooleanLiteral(self, ast: BooleanLiteral, o: Access):
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(str(ast.value).lower(), frame), BoolType()

    def visitStringLiteral(self, ast: StringLiteral, o: Access):
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHCONST(ast.value, StringType(), frame), StringType()