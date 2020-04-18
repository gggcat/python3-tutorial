import keyring

keyring.set_password('test', 'testuser', 'passpasstest')
print(keyring.get_password('test', 'testuser'))

keyring.delete_password('test', 'testuser')
print(keyring.get_password('test', 'testuser'))
