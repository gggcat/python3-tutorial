
## PIPでエラーになる

``` bash
$pip install onedrivesdk
Collecting onedrivesdk
  Using cached onedrivesdk-2.0.tar.gz (1.1 kB)
    ERROR: Command errored out with exit status 1:
     command: /usr/local/bin/python -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/tmp/pip-install-_mytw9wb/onedrivesdk_f6996c9703ad46e9bbda9e10634e8de4/setup.py'"'"'; __file__='"'"'/tmp/pip-install-_mytw9wb/onedrivesdk_f6996c9703ad46e9bbda9e10634e8de4/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /tmp/pip-pip-egg-info-_lq6hca5
         cwd: /tmp/pip-install-_mytw9wb/onedrivesdk_f6996c9703ad46e9bbda9e10634e8de4/
    Complete output (5 lines):
    Traceback (most recent call last):
      File "<string>", line 1, in <module>
      File "/tmp/pip-install-_mytw9wb/onedrivesdk_f6996c9703ad46e9bbda9e10634e8de4/setup.py", line 9, in <module>
        with open(NOTICE, 'r', encoding='utf-8') as f:
    NotADirectoryError: [Errno 20] Not a directory: '/tmp/pip-install-_mytw9wb/onedrivesdk_f6996c9703ad46e9bbda9e10634e8de4/setup.py/../NOTICE.rst'
    ----------------------------------------
ERROR: Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
```


``` bash
 $pip install https://github.com/OneDrive/onedrive-sdk-python/archive/master.zip
Collecting https://github.com/OneDrive/onedrive-sdk-python/archive/master.zip
  Downloading https://github.com/OneDrive/onedrive-sdk-python/archive/master.zip
     - 223 kB 1.6 MB/s
Collecting requests>=2.6.1
  Downloading requests-2.25.1-py2.py3-none-any.whl (61 kB)
     |████████████████████████████████| 61 kB 4.0 MB/s
Collecting certifi>=2017.4.17
  Downloading certifi-2020.12.5-py2.py3-none-any.whl (147 kB)
     |████████████████████████████████| 147 kB 8.8 MB/s
Collecting chardet<5,>=3.0.2
  Downloading chardet-4.0.0-py2.py3-none-any.whl (178 kB)
     |████████████████████████████████| 178 kB 8.3 MB/s
Collecting idna<3,>=2.5
  Downloading idna-2.10-py2.py3-none-any.whl (58 kB)
     |████████████████████████████████| 58 kB 6.1 MB/s
Collecting urllib3<1.27,>=1.21.1
  Downloading urllib3-1.26.2-py2.py3-none-any.whl (136 kB)
     |████████████████████████████████| 136 kB 9.1 MB/s
Building wheels for collected packages: onedrivesdk
  Building wheel for onedrivesdk (setup.py) ... done
  Created wheel for onedrivesdk: filename=onedrivesdk-1.1.8-py3-none-any.whl size=145779 sha256=541a40d5ffbb892101e3860edbf1c56107de011e5c039fb47b181468170b7e2a
  Stored in directory: /tmp/pip-ephem-wheel-cache-cod74ifm/wheels/f1/5d/90/d36d7311f1985bf4a6e01cf745a39f8e42b13f7e748c381cfe
Successfully built onedrivesdk
Installing collected packages: urllib3, idna, chardet, certifi, requests, onedrivesdk
Successfully installed certifi-2020.12.5 chardet-4.0.0 idna-2.10 onedrivesdk-1.1.8 requests-2.25.1 urllib3-1.26.2
```

## アプリ登録

https://docs.microsoft.com/ja-jp/onedrive/developer/rest-api/getting-started/app-registration?view=odsp-graph-online
https://keathmilligan.net/automate-your-work-with-msgraph-and-python

### redirect uriは？

https://login.microsoftonline.com/common/oauth2/nativeclient

``` bash
$pip install requests
Collecting requests
  Downloading requests-2.25.1-py2.py3-none-any.whl (61 kB)
     |████████████████████████████████| 61 kB 4.3 MB/s
Collecting idna<3,>=2.5
  Downloading idna-2.10-py2.py3-none-any.whl (58 kB)
     |████████████████████████████████| 58 kB 6.9 MB/s
Collecting urllib3<1.27,>=1.21.1
  Downloading urllib3-1.26.2-py2.py3-none-any.whl (136 kB)
     |████████████████████████████████| 136 kB 11.6 MB/s
Collecting chardet<5,>=3.0.2
  Downloading chardet-4.0.0-py2.py3-none-any.whl (178 kB)
     |████████████████████████████████| 178 kB 10.5 MB/s
Collecting certifi>=2017.4.17
  Downloading certifi-2020.12.5-py2.py3-none-any.whl (147 kB)
     |████████████████████████████████| 147 kB 10.6 MB/s
Installing collected packages: idna, urllib3, chardet, certifi, requests
Successfully installed certifi-2020.12.5 chardet-4.0.0 idna-2.10 requests-2.25.1 urllib3-1.26.2
```


``` bash
 $pip install msal
Collecting msal
  Downloading msal-1.8.0-py2.py3-none-any.whl (58 kB)
     |████████████████████████████████| 58 kB 4.0 MB/s
Requirement already satisfied: requests<3,>=2.0.0 in /usr/local/lib/python3.8/site-packages (from msal) (2.25.1)
Collecting cryptography<4,>=0.6
  Downloading cryptography-3.3.1-cp36-abi3-manylinux2010_x86_64.whl (2.6 MB)
     |████████████████████████████████| 2.6 MB 8.6 MB/s
Requirement already satisfied: six>=1.4.1 in /usr/local/lib/python3.8/site-packages (from cryptography<4,>=0.6->msal) (1.14.0)
Collecting cffi>=1.12
  Downloading cffi-1.14.4-cp38-cp38-manylinux1_x86_64.whl (411 kB)
     |████████████████████████████████| 411 kB 10.5 MB/s
Collecting PyJWT[crypto]<2,>=1.0.0
  Downloading PyJWT-1.7.1-py2.py3-none-any.whl (18 kB)
Requirement already satisfied: chardet<5,>=3.0.2 in /usr/local/lib/python3.8/site-packages (from requests<3,>=2.0.0->msal) (4.0.0)
Requirement already satisfied: idna<3,>=2.5 in /usr/local/lib/python3.8/site-packages (from requests<3,>=2.0.0->msal) (2.10)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in /usr/local/lib/python3.8/site-packages (from requests<3,>=2.0.0->msal) (1.26.2)
Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.8/site-packages (from requests<3,>=2.0.0->msal) (2020.12.5)
Collecting pycparser
  Downloading pycparser-2.20-py2.py3-none-any.whl (112 kB)
     |████████████████████████████████| 112 kB 10.9 MB/s
Installing collected packages: pycparser, cffi, PyJWT, cryptography, msal
Successfully installed PyJWT-1.7.1 cffi-1.14.4 cryptography-3.3.1 msal-1.8.0 pycparser-2.20
```

## トークンが取れない？

https://eventmarketing.blob.core.windows.net/decode2018-after/decode2018_PDF_AD33.pdf

https://github.com/AzureAD/microsoft-authentication-library-for-python/issues/223

https://docs.microsoft.com/en-us/samples/officedev/pnp-officeaddins/get-onedrive-data-using-microsoft-graph-and-msalnet-in-an-office-add-in/

マルチテナント＋個人を選択する必要がある


## ログイン

``` bash
$python onedrive.py
To sign in, use a web browser to open the page https://microsoft.com/devicelogin and enter the code HM97CDYE9 to authenticate.
Traceback (most recent call last):
  File "onedrive.py", line 50, in <module>
    raise Exception('no access token in result')
Exception: no access token in result
```

``` json
{'error': 'invalid_client', 'error_description': "AADSTS7000218: The request body must contain the following parameter: 'client_assertion' or 'client_secret'.\r\nTrace ID: eabf4412-9481-4772-b5ac-2af65c0cef00\r\nCorrelation ID: 02143dbd-ada1-44ff-a990-a04bac9225ba\r\nTimestamp: 2021-01-18 09:08:22Z", 'error_codes': [7000218], 'timestamp': '2021-01-18 09:08:22Z', 'trace_id': 'eabf4412-9481-4772-b5ac-2af65c0cef00', 
'correlation_id': '02143dbd-ada1-44ff-a990-a04bac9225ba', 'error_uri': 'https://login.microsoftonline.com/error?code=7000218'}
```

→デバイスコードフローを有効にする


## アクセスできない・・・・・

{'error': {'code': 'BadRequest', 'message': 'Tenant does not have a SPO license.', 'innerError': {'date': '2021-01-18T09:32:35', 'request-id': '806528d6-2f76-4e14-80bf-2e3b1621a38b', 'client-request-id': '806528d6-2f76-4e14-80bf-2e3b1621a38b'}}}

https://stackoverflow.com/questions/46802055/tenant-does-not-have-a-spo-license


https://www.366service.com/jp/qa/41a85b1269de68af80cb8e4d4f61ae73




https://docs.microsoft.com/ja-jp/onedrive/developer/rest-api/api/drive_get?view=odsp-graph-online


## ENDPOINTが違う？

https://docs.microsoft.com/ja-jp/onedrive/developer/rest-api/concepts/direct-endpoint-differences?view=odsp-graph-online


## 認証もだめ

{'error': {'code': 'unauthenticated', 'message': "Must be authenticated to use '/drive' syntax."}}

https://stackoverflow.com/questions/50036233/onedrive-api-unauthenticated-must-be-authenticated-to-use-drive-syntax

https://cmatskas.com/working-with-onedrive-data-with-ms-graph-and-net-core/

https://github.com/microsoftgraph/python-sample-auth

