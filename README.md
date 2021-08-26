# Bad-word-filter

<p>
    <img alt="Typescript" src="https://img.shields.io/badge/-Typescript-blue?logo=Typescript&logoColor=white"/>
    <img alt="React" src="https://img.shields.io/badge/-React-45b8d8?logo=react&logoColor=white"/>
    <img alt="Keras" src="https://img.shields.io/badge/-Keras-CB3837?logo=Keras&logoColor=white"/>
    <img alt="python" src="https://img.shields.io/badge/-Python-blue?logo=python&logoColor=white"/>
    <img alt="Django" src="https://img.shields.io/badge/-Django-darkgreen?logo=Django&logoColor=white"/>
</p>

## 📚 Introduction

영상의 오디오를 추출하여 필터링 후, 영상 소스에 다시 합쳐 출력하는 기능을 수행하는 개인 프로젝트입니다.

## 🛠️ Tech Stack

![newStack](https://user-images.githubusercontent.com/38010141/121794496-98997100-cc43-11eb-8b2d-3052932188f7.PNG)

## 🌈 Process

<img width="800" src="https://user-images.githubusercontent.com/38010141/116698374-42f46680-a9ff-11eb-9983-24983948522e.PNG"/>

<img width="800" src="https://user-images.githubusercontent.com/38010141/116698376-44259380-a9ff-11eb-9d38-ce80f6ec0dab.PNG"/>

## 🔥 Results

### - Core `NLP - CharCNN`

<img width="800" alt="스크린샷 2020-12-03 오후 9 17 45 2" src="https://user-images.githubusercontent.com/38010141/101239495-45da7c00-372b-11eb-819c-6aee1f3b00ff.png">
<img width="800" alt="스크린샷 2020-12-03 오후 9 17 45 4" src="https://user-images.githubusercontent.com/38010141/101239506-4ffc7a80-372b-11eb-96c7-ac9c16739662.png">
<img width="800" alt="스크린샷 2020-12-05 오후 6 54 53" src="https://user-images.githubusercontent.com/38010141/101239520-5ee32d00-372b-11eb-91ad-5addc6d74d2b.png">

---

### - Client

![client](https://user-images.githubusercontent.com/38010141/121794417-c92cdb00-cc42-11eb-916c-f82107be964e.PNG)

![storybook](https://user-images.githubusercontent.com/38010141/121794463-3e001500-cc43-11eb-9adf-b9aee746c6d6.PNG)

### 🔥 Demo & How to start?

- Client

```zsh
cd client
yarn install
yarn start
```

- Server

**Django (~1.1.0) `Deprecated`**

```zsh
cd server
pip install -r requirements.txt
python manage.py runserver
```

**Express (^2.0.0)**

> 2.0.0 개발 중..

```zsh
// .env
NODE_ENV=development
PORT=8000
CLIENT_URL_DEVELOPMENT=http://localhost:3000
SERVER_URL_DEVELOPMENT=http://localhost:8000
CLIENT_URL_PRODUCTION=
SERVER_URL_PRODUCTION=
DB_TYPE=sqlite
DB_HOST=localhost
DB_USERNAME=test
DB_PASSWORD=test
DB_DATABASE=db.sqlite

// deep/etri.json
{
  "service_type": "ETRI Recognition",
  "private_key": ""
}

// deep/google.json
GCP SpeechToText API에서 받은 json파일로 대체하십시오.
(파일명은 google.json으로)

{
  "type": "",
  "project_id": "",
  "private_key_id": "",
  "private_key": "",
  "client_email": "",
  "client_id": "",
  "auth_uri": "",
  "token_uri": "",
  "auth_provider_x509_cert_url": "",
  "client_x509_cert_url": ""
}

// deep/model.h5
학습된 h5 파일을 파일명 model.h5 으로 수정한 후 넣어주십시오.
```

```zsh
// Express > "v2.0.0 ~"
cd server
yarn install
yarn dev / yarn start
```
