#!/usr/bin/env python3
"""
로컬 환경 테스트 스크립트
"""

import requests
import json
import time
import sys

# 테스트 설정
BASE_URL = "http://localhost:8000"
API_ENDPOINTS = [
    "/",
    "/health",
    "/debug/db",
    "/api/festivals",
    "/api/places",
    "/api/courses",
    "/api/search?q=세종"
]

def test_endpoint(endpoint):
    """개별 엔드포인트 테스트"""
    try:
        url = f"{BASE_URL}{endpoint}"
        print(f"🔍 테스트 중: {url}")
        
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            print(f"✅ 성공: {response.status_code}")
            if response.headers.get('content-type', '').startswith('application/json'):
                data = response.json()
                if isinstance(data, list):
                    print(f"   📊 데이터 개수: {len(data)}")
                elif isinstance(data, dict):
                    print(f"   📊 응답 키: {list(data.keys())}")
        else:
            print(f"❌ 실패: {response.status_code}")
            
    except requests.exceptions.ConnectionError:
        print(f"❌ 연결 실패: 서버가 실행 중인지 확인하세요")
    except requests.exceptions.Timeout:
        print(f"❌ 타임아웃: {endpoint}")
    except Exception as e:
        print(f"❌ 오류: {e}")

def test_api_functionality():
    """API 기능 테스트"""
    print("\n🧪 API 기능 테스트")
    
    # 축제 생성 테스트
    try:
        festival_data = {
            "name": "테스트 축제",
            "date": "2025.01.01 ~ 2025.01.05",
            "time": "10:00 ~ 18:00",
            "location": "테스트 장소",
            "description": "테스트용 축제입니다"
        }
        
        response = requests.post(
            f"{BASE_URL}/api/festivals/",
            json=festival_data,
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            print("✅ 축제 생성 성공")
        else:
            print(f"❌ 축제 생성 실패: {response.status_code}")
            
    except Exception as e:
        print(f"❌ 축제 생성 테스트 오류: {e}")

def main():
    """메인 테스트 함수"""
    print("🚀 로컬 환경 테스트 시작")
    print(f"📍 테스트 URL: {BASE_URL}")
    
    # 1. 기본 엔드포인트 테스트
    print("\n📋 기본 엔드포인트 테스트")
    for endpoint in API_ENDPOINTS:
        test_endpoint(endpoint)
        time.sleep(0.5)  # 요청 간격
    
    # 2. API 기능 테스트
    test_api_functionality()
    
    print("\n🎉 테스트 완료!")
    print("\n💡 다음 단계:")
    print("1. Railway에 배포")
    print("2. GitHub Pages에 프론트엔드 배포")
    print("3. 전체 시스템 통합 테스트")

if __name__ == "__main__":
    main() 