

/**
 * @author nhphung
 */
package exercise

trait FP {

// Q1
  def recLstSquare(n:Int)= null
  def recHelpLstSquare(n1:Int,n2:Int):List[Int] = null
  
  def higLstSquare(n:Int)= null
// Q2
  def recPow(x:Double,n:Int):Double = 0
  def higPow(x:Double,n:Int) = null
// Q3
  def recAppend(a:List[Int],b:List[Int]):List[Int] = null
  def recReverse(a:List[Int]):List[Int] = null
  def higAppend(a:List[Int],b:List[Int]) = null
  def higReverse(a:List[Int]):List[Int] = null
// Q4
  def recLessThan(n:Int,lst:List[Int]):List[Int] = null
  def higLessThan(n:Int,lst:List[Int]) = null

// Q5
  case class A(n:String,v:Int)
  case class B(x:Int,y:A)
  def lookup[T](n:String,lst:List[T],f:T=>String):Option[T] = null
}