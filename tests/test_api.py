import pytest

from packages.api import get_user_from_api

class TestApi:
    # 正常系
    @pytest.fixture
    def test_get_user_from_api(self,mocker):
        # レスポンスをモックする
        mock_response = mocker.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"id": 1, "name": "Leanne Graham", "email": "Sincere@april.biz"}

        # requests.getをモックする
        mocker.patch('requests.get', return_value=mock_response)

        # ユーザー情報を取得する
        user = get_user_from_api(1)
        assert user == {"id": 1, "name": "Leanne Graham", "email": "Sincere@april.biz"}

    # 異常系
    @pytest.fixture
    def test_get_user_from_api_400_error(self,mocker):
        # レスポンスをモックする
        mock_response = mocker.Mock()
        mock_response.status_code = 400

        # requests.getをモックする
        mocker.patch('requests.get', return_value=mock_response)

        # 400エラーの場合はValueErrorが発生する
        with pytest.raises(ValueError) as e:
            get_user_from_api(1)
        assert str(e.value) == "400エラーが発生しました"

    @pytest.fixture
    def test_get_user_from_api_404_error(self,mocker):
        # レスポンスをモックする
        mock_response = mocker.Mock()
        mock_response.status_code = 404

        # requests.getをモックする
        mocker.patch('requests.get', return_value=mock_response)

        # 404エラーの場合はValueErrorが発生する
        with pytest.raises(ValueError) as e:
            get_user_from_api(1)
        assert str(e.value) == "404エラーが発生しました"

    @pytest.fixture
    def test_get_user_from_api_500_error(self,mocker):
        # レスポンスをモックする
        mock_response = mocker.Mock()
        mock_response.status_code = 500

        # requests.getをモックする
        mocker.patch('requests.get', return_value=mock_response)

        # 500エラーの場合はExceptionが発生する
        with pytest.raises(Exception) as e:
            get_user_from_api(1)
        assert str(e.value) == "500エラーが発生しました"

    @pytest.fixture
    def test_get_user_from_api_other_error(self,mocker):
        # レスポンスをモックする
        mock_response = mocker.Mock()
        mock_response.status_code = 503

        # requests.getをモックする
        mocker.patch('requests.get', return_value=mock_response)

        # 503エラーの場合はExceptionが発生する
        with pytest.raises(Exception) as e:
            get_user_from_api(1)
        assert str(e.value) == "想定外のエラーが発生しました"
    
