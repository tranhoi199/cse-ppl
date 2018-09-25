

object Main extends App {

    trait ExpAST
case class Plus(e1:ExpAST,e2:ExpAST) extends ExpAST
case class Mul(e1:ExpAST,e2:ExpAST) extends ExpAST
case class Ident(s:String) extends ExpAST
case class Intlit(p: Int) extends ExpAST

    print(Intlit(15))

    // def mem(x:Int,lst:List[Int]):Boolean = lst match {
    //     case List() => false
    //     case head :: tail => if (x == head) true else mem(x,tail)
    // }

    // print(mem(5, List(1,2,3,4,5)))

    // def mathTest(x : Int): String = x match {
    //     case 1 => "one"
    //     case 2 => "two"
    //     case _ => "many"
    // }
    // print(mathTest(5))

    // def fact(x:Int):Int =
    //     if (x == 0) 1 else x * fact(x - 1)

    // val s = for (x <- 1 to 25 if x*x > 50) yield 2*x
    // print(s)

    // def plus(x:Int)(y:Int) = x + y
    // plus(1)(3)
    // val inc1 = plus(1)_
    // print(inc1(3))

    // def power(exp:Double) = (x:Double) => math.pow(x,exp)
    // val square = power(2)
    // print(square(4)) //yield 16.0
    // val cube = power(3)
    // print(cube(3)) //yield 27.0

    // val a = List(1,2,3).foldLeft("0")((a, b) => a + b)
    // println(a)

    // val a = List(1,2,3).forall( _ % 2 == 0)
    // val b = List(1,2,3).forall( x => x % 2 == 0)
    // println(a)
    // println(b)

    // val c = List(1,2,3).exists( _ % 2 == 0)
    // val d = List(1,2,3).exists( x => x % 2 == 0)
    // println(c)
    // println(d)

    // val f = (x:Double) => x + 2
    // val g = (x:Double) => x * x

    // val h = f compose g
    // println(h(3))

    // val k = f andThen g
    // println(k(3))


    // val a = List(2,3,4).map( _+1 )
    // println(a)

}