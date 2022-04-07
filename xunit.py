
# TODO LIST
# ・テストメソッドを呼び出す
# ・SetUp を最初に呼び出す
# ・tearDownを後で呼び出す
# ・テストメソッドが失敗したとしても tearDown を呼び出す
# ・複数のテストを走らせる
# ・収集したテスト結果を出力する
# ・

class TestCase:
    def __init__( self, name ):
        self.name = name

    def run( self ):
        method = getattr( self, self.name )
        method()


class WasRun( TestCase ):
    def __init__( self, name):
        self.wasRun = None
        super().__init__( name )
    
    def testMethod( self ):
        self.wasRun = 1



test = WasRun( "testMethod" )

print( test.wasRun )

test.run()

print( test.wasRun )


