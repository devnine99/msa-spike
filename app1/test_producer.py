import json

from kafka import KafkaProducer

if __name__ == '__main__':
    producer = KafkaProducer(
        acks=0,
        compression_type='gzip',
        bootstrap_servers=['127.0.0.1:9092'],
        value_serializer=lambda value: json.dumps(value).encode('utf-8'),
        key_serializer=lambda key: json.dumps(key).encode('utf-8'),
    )
    print('start')
    producer.send('shop', key='shop_create', value={'test': 'test'})
    producer.flush()
    print('end')
