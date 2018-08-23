import org.scalatest.FunSuite
import exercise._
/**
  * Created by nhphung on 4/28/17.
  */
class FPSuite extends FunSuite with FP {

  test("test list square with 5 using high order function") {
    val x = higLstSquare(5)
    val y = List(1,4,9,16,25)
    assert(x.sameElements(y))
  }
    
  test("test lookup on list A ") {
  	assert(lookup("m",List(A("n",3),A("m",5)),(x:A)=>x.n)==Some(A("m",5)))
  }
  
}