import time
from data_collector import *
import paho.mqtt.client as mqtt

amount_of_records = 120  # Число записей

# Класс сборщика данных
# Параметр - номер чемодана
pr8dc = Collector(13, {
    '/devices/wb-msw-v3_21/controls/Sound Level': 'sound',
    '/devices/wb-ms_11/controls/Illuminance': 'illuminance',
    '/devices/wb-adc/controls/Vin': 'Vin'
})

# Параметры подключения к MQTT-брокеру
HOST = "192.168.1.13"  # IP чемодана
PORT = 1883  # Стандартный порт подключения для Mosquitto
KEEPALIVE = 60  # Время ожидания доставки сообщения, если при отправке оно будет прeвышено, брокер будет считаться недоступным


def on_connect(client, userdata, flags, rc):
    """ Функция, вызываемая при подключении к брокеру

    Arguments:
    client - Экземпляр класса Client, управляющий подключением к брокеру
    userdata - Приватные данные пользователя, передаваемые при подключениии
    flags - Флаги ответа, возвращаемые брокером
    rc - Результат подключения, если 0, всё хорошо, в противном случае идем в документацию
    """
    print("Connected with result code " + str(rc))

    # Подключение ко всем заданным выше топикам
    for topic in pr8dc.sub_topics.keys():
        client.subscribe(topic)


def on_message(client, userdata, msg):
    """ Функция, вызываемая при получении сообщения от брокера по одному из отслеживаемых топиков

    Arguments:
    client - Экземпляр класса Client, управляющий подключением к брокеру
    userdata - Приватные данные пользователя, передаваемые при подключениии
    msg - Сообщение, приходящее от брокера, со всей информацией
    """
    payload = msg.payload.decode()  # Основное значение, приходящее в сообщение, например, показатель температуры
    topic = msg.topic  # Топик, из которого пришло сообщение, поскольку функция обрабатывает сообщения из всех топиков

    print(topic + " " + payload)

    pr8dc.update_dict(payload, topic)


def main():
    # Создание и настройка экземпляра класса Client для подключения в Mosquitto
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(HOST, PORT, KEEPALIVE)

    client.loop_start()
    current_records = 0  # Число сделанных записей
    previous_time = time.time()  # Время последней записи
    while current_records < amount_of_records:
        if time.time() - previous_time > 5.0:
            pr8dc.update_list()  # Обновление списка записей
            pr8dc.write_json('data_for_plots.json')  # Запсиь в json файл
            pr8dc.write_xml('data_for_plots.xml')  # Запсиь в xml файл
            current_records += 1
            previous_time = time.time()
            print("Выполнена запись " + str(current_records))
    client.loop_stop()


if __name__ == "__main__":
    main()



