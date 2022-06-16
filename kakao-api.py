import requests
import pandas as pd

headers = {
    'Authorization': 'KakaoAK 39f9c46707570ad9e1f79fe4b594508d'
}
parameters = {
    'query': '계란말이'
}
res = requests.get('https://dapi.kakao.com/v2/search/blog', headers=headers, params=parameters)

result_documents = []
for document in res.json().get('documents'):
    result_documents.append(
        [
            document.get('blogname'),
            document.get('contents'),
            document.get('datetime'),
            document.get('thumbnail'),
        ]
    )

df = pd.DataFrame(result_documents)
df.to_excel('kakao_result.xlsx')

print('ok..')
