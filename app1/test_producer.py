import json

from kafka import KafkaProducer

if __name__ == '__main__':
    producer = KafkaProducer(
        acks=0,
        compression_type='gzip',
        bootstrap_servers=['localhost:9092'],
        value_serializer=lambda value: json.dumps(value).encode('utf-8'),
        key_serializer=lambda key: json.dumps(key).encode('utf-8'),
    )
    print('1')
    producer.send('shop', key='shop_create', value='create!')
    producer.flush()
    print('2')
    producer.send('shop', key='shop_delete', value='delete!')
    producer.flush()
    print('3')
    producer.send('shop', key='undefined key', value='undefined!')
    producer.flush()
    print('4')