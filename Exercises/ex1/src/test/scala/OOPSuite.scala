import org.scalatest.FunSuite
import exercise._
/**
  * Created by nhphung on 4/28/17.
  */
class OOPSuite extends FunSuite {

  test("a simple identifier") {
    val x = new Rational(2,1)
    val y = new Rational(3,1)
    assert((x + y).toString == "5/1" )
  }
 

}