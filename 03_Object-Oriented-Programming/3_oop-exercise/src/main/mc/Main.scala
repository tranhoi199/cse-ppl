

/**
 * @author nhphung
 */
package exercise

object Exercise {
  def main(args: Array[String]): Unit = print("a")
}
class Rational(n:Int, d:Int){
    require(d != 0)
    
    private val g = gcd(n.abs, d.abs)
    private def gcd(a: Int, b: Int): Int = 
                  if (b == 0) a else gcd(b, a % b) 
    val numer = n / g
    val denom = d / g
    
    def this(n: Int) = this(n, 1)
    
    def + (that: Rational): Rational =
        new Rational(
             numer * that.denom + that.numer * denom,
             denom * that.denom
        )
    
    override def toString = numer +"/"+ denom
}