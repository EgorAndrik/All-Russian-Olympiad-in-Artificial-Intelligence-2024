# Анализ вакансий

Ежедневно работодатели публикуют тысячи вакансий в самых разных сферах деятельности. Тот факт, что зарплата часто не указывается в тексте вакансии, усложняет процесс размещения вакансий для самих же работодателей, т.к. им в итоге сложно оценить обстановку на рынке и предоставить соискателям интересное предложение. При этом, если заработная плата указана, работодателям проще и рекомендовать вакансию заинтересованным людям, и подбирать подходящих кандидатов. 

В рамках данной задачи Вам предлагается построить модель, которая будет прогнозировать предлагаемую работодателем заработную плату на основе описания вакансии.

# Данные

Для построения модели Вам будут доступны данные о размещенных вакансиях, включая род деятельности компаний, требования к кандидатам и предлагаемые условия. Целевая переменная представляет собой среднюю заработную плату, указанную в вакансии.

Вам необходимо сделать прогнозы для всех объектов, которые находятся в файле с тестовыми данными. 
https://cloud.mail.ru/public/eysK/ZhPFgeiYe

# Метрика

Качество решения MAPE определяется по следующей формуле:

![1-5](https://github.com/user-attachments/assets/bcc6f17f-c7fc-4f98-b715-8fb6a35f91b2)


- N – общее количество объектов,
- y_true – реальное значение целевой переменной,
- y_pred – спрогнозированное значение целевой переменной.

Расчет балла
Промежуточный балл, отображаемый в таблице результатов до момента завершения раунда, рассчитывается по формуле: ``` Score = - MAPE ```  где MAPE – значение метрики, рассчитанное по указанной выше формуле.


Таким образом, промежуточный балл строится по принципу "чем больше абсолютная величина ошибки, тем меньше результат". Максимально возможный промежуточный балл равен 0.

Окончательный балл рассчитывается после завершения раунда по следующей формуле:
```
Points = 200 * percentileofscore(MAPEs, MAPE)
```

percentileofscore – функция, вычисляющая percentile rank,

MAPEs – значения метрик MAPE всех участников, меньшие, чем метрика MAPE за “базовое решение” (опубликованный пример файла решения). То есть участники, загрузившие на проверку только пример решения и не улучшившие этот результат, получат 0 баллов,

MAPE – значение метрики MAPE данного участника.