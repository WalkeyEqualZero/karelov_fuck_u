from telebot import TeleBot

app = TeleBot(__name__)
msg = "Погнали"

app.send_message('@Walkey37', msg)

a = 25
b = 3800
c = 4
d = 2
y = 1500
lst = {}
for e in range(17001, 10000000):
    for x in range(1500, 1000000):
        if a * b == x * c + y * d * a + y * d * c + e:
            lst[f'e{e}'] = e
            lst[f'x{x}'] = x
            app.send_message('@Walkey37', f'e = {e}, x = {x}')

if __name__ == '__main__':
    app.config['api_key'] = '1718942686:AAF9LdrdzD4wbdAWKt4OLh4ss9nmaBDbZvs'
    app.poll(debug=True)

