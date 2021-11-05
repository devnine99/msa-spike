# MSA SPIKE

## Goal  
- MSA에서 서비스간 data sync를 위한 kafka 통신 공부
- 재사용 가능한 kafka consumer 패키지 제작(consumer-framework)

## 프로젝트 구조
```
app1
- django
- shop service

app2
- flask
- product service
```

## SomeApp 사용 방법
- app1/config/events.py 참고 (celery를 참고하여 제작)
- 앱단에서 Event 클래스를 상속받아 `key 설정` 및 `comsume 메서드` 구현
- 실행: `consumer -A config.events:app`


## TODO
- [X] some_app을 bin으로 실행 (as celery)
- [X] 재사용 가능한 kafka consumer 패키지 제작(some_app)
- [ ] Event 클래스를 기반으로 auto generated documentation 작업(topic, key, value)
- [ ] multi topic 지원여부 결정
- [X] some_app naming: consumer-framework