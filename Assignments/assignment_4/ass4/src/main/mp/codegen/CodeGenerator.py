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


class ExpUtils:
    @staticmethod
    def isOpForNumberToNumber(operator):
        return str(operator).lower() in ['+', '-', '*', '/', 'div', 'mod']

    @staticmethod
    def isOpForNumberToBoolean(operator):
        return str(operator).lower() in ['<>', '=', '>', '<', '>=', '<=']

    @staticmethod
    def isOpForNumber(operator):
        return ExpUtils.isOpForNumberToNumber(operator) or ExpUtils.isOpForNumberToBoolean(operator)

    @staticmethod
    def mergeNumberType(lType, rType):
        return FloatType() if FloatType in [type(x) for x in [lType, rType]] else IntType()


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

# class StringType(Type):

#     def __str__(self):
#         return "StringType"

#     def accept(self, v, param):
#         return None

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
    def __init__(self, frame, sym):
        # frame: Frame
        # sym: List[Symbol]

        self.frame = frame
        self.sym = sym

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

    def visitProgram(self, ast, c):
        # ast: Program
        # c: Any

        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        e = SubBody(None, self.env)
        for x in ast.decl:
            e = self.visit(x, e)
        # generate default constructor
        self.genMETHOD(FuncDecl(Id("<init>"), list(), list(), list(), None), c, Frame("<init>", VoidType))
        self.emit.emitEPILOG()
        return c

    def genMETHOD(self, consdecl, o, frame):
        # consdecl: FuncDecl
        # o: Any
        # frame: Frame

        isInit = consdecl.returnType is None
        isMain = consdecl.name.name == "main" and len(consdecl.param) == 0 and type(consdecl.returnType) is VoidType
        returnType = VoidType() if isInit else consdecl.returnType
        methodName = "<init>" if isInit else consdecl.name.name
        intype = [ArrayPointerType(StringType())] if isMain else list()
        mtype = MType(intype, returnType)

        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit, frame))

        frame.enterScope(True)

        glenv = o

        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayPointerType(
                StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))

        body = consdecl.body
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        list(map(lambda x: self.visit(x, SubBody(frame, glenv)), body))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(returnType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    def visitFuncDecl(self, ast, o):
        # ast: FuncDecl
        # o: Any

        subctxt = o
        frame = Frame(ast.name, ast.returnType)
        self.genMETHOD(ast, subctxt.sym, frame)
        return SubBody(None, [Symbol(ast.name, MType(list(), ast.returnType), CName(self.className))] + subctxt.sym)

    def visitCallStmt(self, ast, o):
        # ast: CallStmt
        # o: Any

        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = self.lookup(ast.method.name.lower(), nenv, lambda x: x.name.lower())
        cname = sym.value.value

        ctype = sym.mtype

        in_ = ("", list())
        for x in ast.param:
            str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
            in_ = (in_[0] + str1, in_[1].append(typ1))
        self.emit.printout(in_[0])
        self.emit.printout(self.emit.emitINVOKESTATIC(cname + "/" + sym.name, ctype, frame))

    def visitIntLiteral(self, ast, o):
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

    def visitBinaryOp(self, ast: BinaryOp, o: Access):
        ctxt = o
        frame = ctxt.frame
        op = str(ast.op).lower()
        lCode, lType = self.visit(ast.left, ctxt)
        rCode, rType = self.visit(ast.right, ctxt)
        if ExpUtils.isOpForNumber(op): # for number type
            mType = ExpUtils.mergeNumberType(lType, rType)
            if op == '/': mType = FloatType() # mergeType >= lType, rType
            lCode, rCode = (c if type(t) == type(mType) else c+self.emit.emitI2F(frame) \
                            for c,t in [(lCode, lType), (rCode, rType)])
            if ExpUtils.isOpForNumberToNumber(op):
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