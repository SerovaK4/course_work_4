from classes import HeadHunter, SuperJob, Connector


def main():
    vacancies_json = []
    #keyword = input("Введите ключевое слово для поиска: ")
    keyword = "Python"

    hh = HeadHunter(keyword)
    sj = SuperJob(keyword)
    for api in (hh, sj):
        api.get_vacancies(pages_count=10)
        vacancies_json.extend(api.get_formatted_vacancies())

        connector = Connector(keyword=keyword, vacancies_json=vacancies_json)

        while True:
            command = input(
                "1 - Вывести ссписок вакансий;\n"
                "2 - Сортировка по минимальной зарплате;\n"
                "3 - Сортировка по минимальной зарплате (DESC);\n"
                "4 - Сортировка по максимальной зарплате (DESC);\n"
                "exit - для выхода.\n"
            )
            if command == "exit":
                break
            elif command == "1":
                vacancies = connector.select()
            elif command == "2":
                vacancies = connector.sorted_vacancies_by_salary_from_asc()
            elif command == "3":
                vacancies = connector.sorted_vacancies_by_salary_from_desc()
            elif command == "4":
                vacancies = connector.sorted_vacancies_by_salary_to_asc()

            for vacancy in vacancies:
                print(vacancy, end="\n\n")


if __name__ == "__main__":
    main()