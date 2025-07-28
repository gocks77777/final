# 🚀 배포 가이드

## 📋 개요

- **백엔드**: FastAPI + PostgreSQL (Railway 배포)
- **프론트엔드**: HTML/CSS/JS (GitHub Pages 배포)
- **데이터베이스**: Railway PostgreSQL

## 🔧 백엔드 배포 (Railway)

### 1단계: Railway 계정 설정

1. [Railway](https://railway.app) 가입
2. GitHub 계정 연동

### 2단계: 프로젝트 배포

1. Railway 대시보드에서 "New Project" 클릭
2. "Deploy from GitHub repo" 선택
3. `back/backend` 폴더 선택
4. 배포 시작

### 3단계: 환경변수 설정

Railway 대시보드 → Settings → Variables에서 설정:

```env
DATABASE_URL=postgresql://username:password@host:port/database
KAKAO_API_KEY=a5cc7b65ae5d251113eff578a56cd8f1
CORS_ORIGINS=https://kaia-coder.github.io,https://*.github.io
```

### 4단계: 데이터베이스 설정

1. Railway에서 PostgreSQL 데이터베이스 생성
2. `DATABASE_URL` 환경변수 자동 설정 확인
3. 배포 후 초기 데이터 자동 로드 확인

### 5단계: 배포 확인

- API 엔드포인트: `https://your-app-name.railway.app`
- Swagger 문서: `https://your-app-name.railway.app/docs`
- 헬스체크: `https://your-app-name.railway.app/health`

## 🌐 프론트엔드 배포 (GitHub Pages)

### 1단계: GitHub 저장소 설정

1. GitHub에 프로젝트 푸시
2. Settings → Pages 설정
3. Source: "Deploy from a branch" 선택
4. Branch: `main` 선택
5. Folder: `/ (root)` 선택

### 2단계: API URL 업데이트

`front/main.js`와 `front/festival.html`에서 API URL이 자동으로 설정됩니다:

- 로컬: `http://localhost:8000`
- GitHub Pages: `https://sejong-festival-api.onrender.com`

### 3단계: 배포 확인

- 사이트 URL: `https://kaia-coder.github.io/your-repo-name`
- CORS 설정 확인

## 🔍 문제 해결

### 백엔드 문제

1. **데이터베이스 연결 실패**

   ```bash
   # 로컬에서 테스트
   cd back/backend
   python init_db.py
   ```

2. **CORS 오류**

   - Railway 환경변수에서 `CORS_ORIGINS` 확인
   - 프론트엔드 도메인 추가

3. **API 응답 없음**
   - Railway 로그 확인
   - 포트 설정 확인

### 프론트엔드 문제

1. **API 호출 실패**

   - 브라우저 개발자 도구에서 네트워크 탭 확인
   - CORS 오류 확인

2. **이미지 로드 실패**
   - 상대 경로 확인
   - GitHub Pages 경로 설정 확인

## 📊 모니터링

### Railway 모니터링

- 대시보드에서 로그 확인
- 메트릭스 모니터링
- 오류 알림 설정

### GitHub Pages 모니터링

- Actions 탭에서 배포 상태 확인
- 브라우저 개발자 도구에서 오류 확인

## 🔄 업데이트 프로세스

### 백엔드 업데이트

1. 코드 수정
2. GitHub에 푸시
3. Railway 자동 배포 확인

### 프론트엔드 업데이트

1. 코드 수정
2. GitHub에 푸시
3. GitHub Pages 자동 배포 확인

## 📝 체크리스트

### 배포 전

- [ ] 환경변수 설정 완료
- [ ] 데이터베이스 연결 테스트
- [ ] API 엔드포인트 테스트
- [ ] CORS 설정 확인

### 배포 후

- [ ] 헬스체크 엔드포인트 확인
- [ ] 초기 데이터 로드 확인
- [ ] 프론트엔드 API 연동 확인
- [ ] 전체 기능 테스트

## 🆘 지원

문제 발생 시:

1. Railway 로그 확인
2. 브라우저 개발자 도구 확인
3. API 엔드포인트 직접 테스트
4. 환경변수 재확인
