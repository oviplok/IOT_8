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

    # Формирование гистограммы
    #axs[3].hist(plots_data_lists['sound'])
    #axs[4].hist(plots_data_lists['illuminance'])
    #axs[5].hist(plots_data_lists['Vin'])

    # Формирование кругов
    #axs[6].pie(plots_data_lists['humidity'])
    #axs[7].pie(plots_data_lists['temperature'])
    #axs[8].pie(plots_data_lists['voltage'])

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

    # Задание лейблов для осей и графика
    #axs[3].set_xlabel('Time')
    #axs[3].set_ylabel('Sound lvl')
    #axs[3].set_title('Sound')

    # Задание лейблов для осей и графика
    #axs[4].set_xlabel('Time')
    #axs[4].set_ylabel('ill level')
    #axs[4].set_title('Illuminance')

    # Задание лейблов для осей и графика
   # axs[5].set_xlabel('Time')
   # axs[5].set_ylabel('Vin')
   # axs[5].set_title('Vin')







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

    labels1 = '45-49', '50-52', '53-55'
    labels2 = '500-519', '520-529', '530-540'
    labels3 = '23.78-23.79', '23.80-23.81', '23.82-23.83'
    sizes1 = [15, 62, 23]
    sizes2 = [8, 70, 22]
    sizes3 = [12, 78, 10]

    fig1, ax = plt.subplots(1, 3, figsize=(15, 6))
    explode1 = (0, 0.1, 0)
    explode = (0, 0.1, 0, 0)
    ax[0].pie(sizes1, explode=explode1, labels=labels1, autopct='%1.1f%%', shadow=True, startangle=90)
    ax[1].pie(sizes2, explode=explode1, labels=labels2, autopct='%1.1f%%', shadow=True, startangle=90)
    ax[2].pie(sizes3, explode=explode1, labels=labels3, autopct='%1.1f%%', shadow=True, startangle=90)

    ax[0].set_title('Sound')
    ax[1].set_title('Illuminance')
    ax[2].set_title('Vin')

   # plt.show()



if __name__ == "__main__":
    main()
