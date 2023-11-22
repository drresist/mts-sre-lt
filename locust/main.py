from locust import HttpUser, task, between


class MyUser(HttpUser):
    wait_time = between(1, 3)  # Время ожидания между запросами
    
    def on_start(self):
        # Вызывается при старте пользователя. Вы можете здесь устанавливать начальные параметры.
        pass

    @task(1)
    def get_weather_forecast(self):
        headers = {'Host': 'sre-course-102'}
        self.client.get("/weatherforecast", headers=headers)

    @task(2)
    def get_city_weather(self):
        headers = {'Host': 'sre-course-102'}
        city_id = 1
        self.client.get(f"/cities/{city_id}", headers=headers)

    
    @task(3)
    def get_cities(self):
        headers = {'Host': 'sre-course-102'}
        self.client.get("/cities", headers=headers)


