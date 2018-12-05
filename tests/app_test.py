def test_app(test_client):
	response = test_client.get('/')
	assert response.status_code == 200
	assert b 'Hello Andela Code Camp' in response.data

def test_home(test_client):
	response = test_client.get('/home', follow_redirects=True)
	assert response.status_code == 200
	assert b 'Hello Andela Code Camp' in response.data