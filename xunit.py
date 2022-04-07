
# TODO LIST
# ◎テストメソッドを呼び出す
# ・SetUp を最初に呼び出す
# ・tearDownを後で呼び出す
# ・テストメソッドが失敗したとしても tearDown を呼び出す
# ・複数のテストを走らせる
# ・収集したテスト結果を出力する
# ・

class TestCase:
    def __init__( self, name ):
        self.name = name

    def setUp( self ):
        pass

    def run( self ):
        self.setUp()
        method = getattr( self, self.name )
        method()


class WasRun( TestCase ):
    def setUp( self ):
        self.wasRun = None
        self.wasSetUp = 1
    
    def testMethod( self ):
        self.wasRun = 1



# test = WasRun( "testMethod" )
# print( test.wasRun )
# test.run()
# print( test.wasRun )


class TestCaseTest( TestCase ):
    def testRunning( self ):
        test = WasRun("testMethod")
        assert( not test.wasRun )
        test.run()
        assert( test.wasRun )

    def testSetUp( self ):
        test = WasRun( "testMethod" )
        test.run()
        assert( test.wasSetUp )


TestCaseTest("testRunning").run()
TestCaseTest("testSetUp").run()