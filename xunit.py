
# TODO LIST
# ・テストメソッドを呼び出す
# ・SetUp を最初に呼び出す
# ・tearDownを後で呼び出す
# ・テストメソッドが失敗したとしても tearDown を呼び出す
# ・複数のテストを走らせる
# ・収集したテスト結果を出力する
# ・

class WasRun:
    pass

test = WasRun( "testMethod" )

print( test.wasRun )

test.testMethod()

print( test.wasRun )


