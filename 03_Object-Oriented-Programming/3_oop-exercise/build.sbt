
scalaVersion := "2.12.3"

name := "exercise"

version := "1.0"

lazy val scalatest = "org.scalatest" %% "scalatest" % "3.0.1"

libraryDependencies += scalatest % Test

testOptions in Test += Tests.Argument(TestFrameworks.ScalaTest ,"-fW", "result.txt","-eNDXELO")

scalaSource in Compile := baseDirectory.value / "src" / "main"

