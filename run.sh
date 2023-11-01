#pytest -s -v -m "sanity" --html=/home/mohammedsalahudeen/PycharmProjects/nopcommerceApp/Reports/reports.html --browser chrome
#pytest -s -v -m "sanity or regression" --html=/home/mohammedsalahudeen/PycharmProjects/nopcommerceApp/Reports/reports.html --browser chrome
pytest -s -v -m "sanity and regression" --html=/home/mohammedsalahudeen/PycharmProjects/nopcommerceApp/Reports/reports.html --browser chrome
pytest -s -v -m "sanity and regression" --html=/home/mohammedsalahudeen/PycharmProjects/nopcommerceApp/Reports/reports.html --browser firefox

#pytest -s -v -m "regression" --html=/home/mohammedsalahudeen/PycharmProjects/nopcommerceApp/Reports/reports.html --browser chrome

