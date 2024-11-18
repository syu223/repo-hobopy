from chalice import Chalice
from chalicelib import database
# BadRequestError を追加
from chalice import BadRequestError, Chalice,NotFoundError


# NotFoundError の import を追加
from chalice import Chalice, NotFoundError

app = Chalice(app_name='hobopy-backend')

# 1 すべてのToDo を取得する
@app.route('/todos', methods=['GET'],cors=True)
def get_all_todos():
    return database.get_all_todos()

# 2 指定された IDのToDo を取得する
#@app.route('/todos/{todo_id}',
#methods= ['GET'] )
#def get_todo(todo_id) :
#    return database.get_todo(todo_id)

@app.route('/todos/{todo_id}', methods=['GET'],cors=True)
def get_todo(todo_id):
    todo = database.get_todo(todo_id)
    if todo:
        return todo
    else:
        raise NotFoundError ( 'Todo not found.')
# 404 を返す

@app.route('/todos', methods=['POST'],cors=True)
def create_todo():
    # 1 リクエストメッセージボディを取得する
    todo = app.current_request.json_body

    # 2 必須項目をチェックする
    for key in ['title','memo','priority']:
        if key not in todo:
            raise BadRequestError(f"{key} is required. ")

    # 3 データを登録する
    return database.create_todo(todo)

@app.route('/todos/{todo_id}',methods=['PUT'],cors=True)
def update_todo(todo_id):
    changes = app.current_request.json_body
    # 1 データを更新する
    return database.update_todo(todo_id,changes)

@app.route('/todos/{todo_id}',methods=['DELETE'],cors=True )
def delete_todo(todo_id):
    # 1 データを削除する
    return database.delete_todo(todo_id)