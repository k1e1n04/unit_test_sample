import requests

def get_user_from_api(user_id: int):
    """
    ユーザー情報を取得する
    :param user_id: ユーザーID
    :return: ユーザー情報
    """
    # user_idが数値でない場合はエラー
    if not isinstance(user_id, int):
        raise TypeError("引数は数値である必要があります")
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    if response.status_code == 400:
        raise ValueError("400エラーが発生しました")
    elif response.status_code == 404:
        raise ValueError("404エラーが発生しました")
    elif response.status_code == 500:
        raise Exception("500エラーが発生しました")
    elif response.status_code != 200:
        raise Exception("想定外のエラーが発生しました")
    return response.json()