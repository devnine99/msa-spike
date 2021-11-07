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

## ConsumerFramework 사용 방법
- app1/config/events.py 참고 (celery를 참고하여 제작)
- app.event(topic='topic', key='key', schema=Schema)
- 실행: `consumer -A config.events:app`


## TODO
- [X] consumer framework를 bin으로 실행 (as celery)
- [X] 재사용 가능한 kafka consumer 패키지 제작(consumer framework)
- [ ] Event 클래스를 기반으로 auto generated documentation 작업(topic, key, schema)
- [X] multi topic 지원여부 결정(지원)
- [X] some_app naming: consumer-framework
