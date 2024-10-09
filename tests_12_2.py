import unittest                                                          # Импортируем библиотеку unittest
from runner_and_tournament import Runner, Tournament                     # Импортируем из модуля runner_and_tournament
                                                                         # классы Runner и Tournament

class TournamentTest(unittest.TestCase):     # Определяем класс TournamentTest, наследованный от unittest.TestCase

    @classmethod

    def setUpClass(cls):        # Метод, который будет запускаться перед запуском тестов, где создается и очищается
                                  # пустой словарь
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн", 10)     # Создаем объект Usein класса Runner
                                                            # (из модуля runner_and_tournament)
        self.andrei = Runner("Андрей", 9)    # Создаем объект Andrei класса Runner
                                                            # (из модуля runner_and_tournament)
        self.nik = Runner("Ник", 3)          # Создаем объект Nik класса Runner
                                                            # (из модуля runner_and_tournament)
    @classmethod
    def tearDownClass(cls):                              # Метод tearDownClass, который будет выполняться один раз
                                                            # после завершения всех тестов
        for results in cls.all_results.values():         # Цикл по всем значениям словаря cls.all_results, где
                                                            # каждое значение представляет собой словарь с
                                                            # местом (результат) и именем бегуна
            formated_results = {place:str(runner) for place, runner in results.items()}   # Форматируем результаты в
                                                                                            # читаемый вид
            print(formated_results)                       # Выводим в консоль

    def test_usain_nik(self):      # Определяем первый тест, чтобы протестировать забег между Усэйном и Ником
        tournament = Tournament(90, self.usain, self.nik)   # Создаем объект класса Tournament с
                                                                                  # дистанцией девяносто и участниками
                                                                                  # self.usain и self.nik
        results = tournament.start()                   # Запускаем метод start и
        TournamentTest.all_results[1] = results        # сохраняем его в словарь
        self.assertEqual("Ник", results[2].name)  # Проверяем, что имя последнего бегуна равно Ник

    def test_andrei_nik(self):      # Определяем первый тест, чтобы протестировать забег между Андреем и Ником
        tournament = Tournament(90, self.andrei, self.nik)   # Создаем объект класса Tournament с
                                                                                   # дистанцией девяносто и участниками
                                                                                   # self.andrei и self.nik
        results = tournament.start()                   # Запускаем метод start и
        TournamentTest.all_results[2] = results        # сохраняем его в словарь
        self.assertEqual("Ник", results[2].name)  # Проверяем, что имя последнего бегуна равно Ник

    def test_usain_andrei_nik(self):  # Определяем первый тест, чтобы протестировать забег между Усэйном, Андреем и Ником
        tournament = Tournament(90, self.usain, self.andrei, self.nik)  # Создаем объект класса
                                                                                   # Tournament с
                                                                                   # дистанцией девяносто и участниками
                                                                                   # self.usain, self.andrei и self.nik
        results = tournament.start()                   # Запускаем метод start и
        TournamentTest.all_results[3] = results        # сохраняем его в словарь
        self.assertEqual("Ник", results[3].name)  # Проверяем, что имя последнего бегуна равно Ник

if __name__ == "__main__":                       # Для запуска используем юнит-тест "main"
    unittest.main()









