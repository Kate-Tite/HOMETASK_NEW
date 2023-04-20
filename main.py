from utils import load_data, filter_sort, formatted_data # импорт функций

JSON_FILE = 'operations.json'

def main():

    data = load_data(JSON_FILE)
    data = filter_sort(data)

    for i in range(5):
        print(formatted_data(data[i]))

if __name__ == '__main__':
    main()