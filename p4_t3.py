f = float(input())
l = float(input())
print('1 - Собирающая линза, 0 - Рассеивающая линза')
a = int(input())

def linza():
  if a == 1:
    if f > l:
      print('Изображение мнимое, прямое, увеличенное')
    if f == l:
      print('Изображение отсутсвует')
    if f > l and 2 * f > l:
      print('Изображение действительное, перевёрнутое, увеличенное')
    if l == 2 * f:
      print('Изображение действительное, перевёрнутое, равно')
    if l > 2 * f:
      print('Изображение действительное, перевёрнутое, уменьшенное')
    if a == 0:
      print('Изображение мнимое, прямое, уменьшенное')

print(linza())  