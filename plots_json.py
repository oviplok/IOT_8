from datetime import datetime

import matplotlib.pyplot as plt
import json


# Функция получения данных из json-файла
def get_data_from_json(filename):
    with open(filename, 'r') as file:
        file_data = json.load(file)

    return file_data


def create_plots(plots_data_lists):
    # Создание графиков для отрисовки данных
    fig, axs = plt.subplots(1, 3, figsize=(15, 6))  # Получим окно с 1 колонкой и 3 столбцами графиков

    # fig - окно, в котором будут отрисовываться графики
    # axs содержит в себе список графиков для отрисовки на них значений

    # Задание набора точек для отрисовки
    # Первый аргумент - список значений по оси X, второй аргумент - по оси Y
    axs[0].plot(plots_data_lists['sound'])
    axs[1].plot(plots_data_lists['illuminance'])
    axs[2].plot(plots_data_lists['Vin'])

    # Задание лейблов для осей и графика
    axs[0].set_xlabel('Time')
    axs[0].set_ylabel('sound level')
    axs[0].set_title('level')

    # Задание лейблов для осей и графика
    axs[1].set_xlabel('Time')
    axs[1].set_ylabel('ill level')
    axs[1].set_title('Illuminance')

    # Задание лейблов для осей и графика
    axs[2].set_xlabel('Time')
    axs[2].set_ylabel('Vin')
    axs[2].set_title('Vin')







    return fig, axs


def main():
    plots_data_lists = {
        'sound': [],
        'illuminance': [],
        'Vin': []
    }

    json_data = get_data_from_json("data_for_plots.json")

    # Заполнение списков с данными, с преобразованием типов
    for json_dict in json_data:
        plots_data_lists['sound'].append(float(json_dict.get('sound')))
        plots_data_lists['illuminance'].append(float(json_dict.get('illuminance')))
        plots_data_lists['Vin'].append(float(json_dict.get('Vin')))


    fig, axs = create_plots(plots_data_lists)

    plt.show()



if __name__ == "__main__":
    main()
