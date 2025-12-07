import time

current_time = time.time()
seconds_per_day = 60 * 60 * 24
days_from_the_epoch_begins = int(current_time // seconds_per_day)
print('Дней с начала эпохи:', days_from_the_epoch_begins)
current_hours = ((current_time % seconds_per_day) // 3600) % 24 + 3  # +3 часа для Москвы так как в Москве время UTC+3
print('Текущий час:', int(current_hours))
current_minutes = (current_time % 3600) // 60
print('Текущие минуты:', int(current_minutes))
current_seconds = current_time % 60
print('Текущие секунды:', int(current_seconds))
