
# Table of Contents

1.  [Задание](#org1078ed9)
    1.  [Разработать профиль нагрузки для системы](#org1aa4837)
        1.  [Сценарий 1 - Получение текущей погоды](#org419d2e1)
        2.  [Cценарий 2 - Параллельные запросы](#org1fc7519)
        3.  [Сценарий 3 - Случайные запросы](#orgbdd833d)
        4.  [Сценарий 4 - Тестирование ошибок](#orgc424b1b)
        5.  [Сценарий 5 - Постепенное увеличение нагрузки](#org01f5854)
    2.  [Реализовать профиль на любом инструменте НТ](#org3f0151f)
    3.  [Задать нефункциональные требования по производительности (SLA/SLO)](#org703e5b7)
    4.  [Максимальная производительность](#org0874326)
    5.  [Вывод](#orgd2e6ae1)



<a id="org1078ed9"></a>

# Задание


<a id="org1aa4837"></a>

## Разработать профиль нагрузки для системы


<a id="org419d2e1"></a>

### Сценарий 1 - Получение текущей погоды

1.  Описание: Пользователь запрашивает текущую погоду

2.  Частота: 50 запросов в минуту

3.  Данные: Запрос содержит параметр \`city\`


<a id="org1fc7519"></a>

### Cценарий 2 - Параллельные запросы


<a id="orgbdd833d"></a>

### Сценарий 3 - Случайные запросы

1.  Описание: Пользователи отправляют случайные запросы о текущей погоде в различных городах

2.  Частота: 15 запросов в минуту

3.  Данные: Случайные значения параметра \`city\`


<a id="orgc424b1b"></a>

### Сценарий 4 - Тестирование ошибок

1.  Описание: Пользователи отправляют запросы с неверными параметрами для проверки обработки ошибок

2.  Частота: 10 запросов в минуту

3.  Данные: Запросы содержат неверные значения параметра city или отсутстовать


<a id="org01f5854"></a>

### Сценарий 5 - Постепенное увеличение нагрузки

1.  Описание: Нагрузка постепенно увеличивается в течение определенного периода времени для проверки устойчивости

2.  Частота: С 10 запросов в минуту до 100 запросов в секунду в течение 30 минут


<a id="org3f0151f"></a>

## Реализовать профиль на любом инструменте НТ


<a id="org703e5b7"></a>

## Задать нефункциональные требования по производительности (SLA/SLO)

-   Процентиль времени отклика (95% запросов должны быть обработаны за Х миллисекунд)
-   Пропускная способность (RPS)
-   Время обработки запроса на сервере (максимальное/среднее)


<a id="org0874326"></a>

## Максимальная производительность


<a id="orgd2e6ae1"></a>

## Вывод
