
# TODO LIST
# ◎テストメソッドを呼び出す
# ◎SetUp を最初に呼び出す
# ◎tearDownを後で呼び出す
# ・テストメソッドが失敗したとしても tearDown を呼び出す
# ・複数のテストを走らせる
# ・収集したテスト結果を出力する
# ◎WasRunで文字列をログに記録する

from pkg_resources import cleanup_resources


class TestCase:
    def __init__( self, name ):
        self.name = name

    def setUp( self ):
        pass

    def run( self ):
        self.setUp()
        method = getattr( self, self.name )
        method()
        self.tearDown()
        return TestResult()

    def tearDown( self ):
        pass


class TestResult:
    def __init__( self ):
        self.runCount = 1

    def summary( self ):
        return "%d run, 0 failed" % self.runCount

class WasRun( TestCase ):
    def setUp( self ):
        self.log = "setUp "
    
    def testMethod( self ):
        self.log = self.log + "testMethod "

    def tearDown( self ):
        self.log = self.log + "tearDown "


class TestCaseTest( TestCase ):
    def testTemplateMethod( self ):
        test = WasRun( "testMethod" )
        test.run()
        assert( "setUp testMethod tearDown " == test.log )
    
    def testResult( self ):
        test = WasRun( "testMethod" )
        result = test.run()
        assert( "1 run, 0 failed" == result.summary() )


TestCaseTest("testTemplateMethod").run()
TestCaseTest("testResult").run()
