h, m = map(int, input().split())

alert = h * 60 + m - 45

if alert < 0:
    alert += (23 * 60 + 60)

alert_hour = alert // 60
alert_minute = alert % 60

print(f'{alert_hour} {alert_minute}')

