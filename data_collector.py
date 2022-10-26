import xml.etree.ElementTree as ET
import json
from datetime import datetime


class Collector:
    def __init__(self, _wb_id, _topics):
        # Словарь с топиками и собираемыми из них параметрами
        self.sub_topics = _topics
        # Список собранных данных
        self.json_list = []
        # Создание словаря для хранения данных JSON
        self.json_dict = {}
        for value in self.sub_topics.values():
            self.json_dict[value] = 0
        self.json_dict['time'] = 0
        self.json_dict['id'] = _wb_id

    # Обновление словаря с замерами
    def update_dict(self, _payload, _topic):
        param_name = self.sub_topics[_topic]
        self.json_dict[param_name] = _payload
        self.json_dict['time'] = str(datetime.now())

    # Обновление списка с данными
    def update_list(self):
        self.json_list.append(self.json_dict.copy())

    # Запись данных в json файл
    def write_json(self, _json_filename):
        with open(_json_filename, 'w') as file:
            json_string = json.dumps(self.json_list)  # Формирование строки JSON из списка
            file.write(json_string)

    # Запись данных в xml файл
    def write_xml(self, _xml_filename):
        with open(_xml_filename, 'w') as file:
            root = ET.Element('data')  # Корень xml-дерева
            # Разбор сообщений
            for _message in self.json_list:
                message = ET.SubElement(root, 'message')
                # Разбор замеров
                for _measure_key in _message.keys():
                    ET.SubElement(message, _measure_key).text = str(_message[_measure_key])
            # Запись xml-дерева в файл
            tree = ET.ElementTree(root)
            tree.write(_xml_filename)
