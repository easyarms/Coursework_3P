from utils import get_data, get_filtered_data, get_last_values, get_formated_data

def main():
    COUNT_VALUES = 5
    FILTERED_EMPTY_DATE = True
    FILTERED_EMPTY_FROM = True

    data = get_data()
    new_data = get_filtered_data(data, FILTERED_EMPTY_DATE, FILTERED_EMPTY_FROM)
    new_data = (get_last_values(new_data, COUNT_VALUES))
    new_data = get_formated_data(new_data)

    for row in new_data:
        print(row, end='\n')


if __name__ == '__main__':
    main()
