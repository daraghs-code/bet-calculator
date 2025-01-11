import telegram_bot_api as tb_api
import telebot
import time

TOKEN = tb_api.token
bot = telebot.TeleBot(TOKEN)

def arb_bet_sizer_equal(odds1, odds1_type, odds2, odds2_type):
    
    if '/' in odds1:
        numerator, denominator = odds1.split('/')
        odds1 = float(numerator)/float(denominator)
        
    if '/' in odds2:
        numerator, denominator = odds2.split('/')
        odds2 = float(numerator)/float(denominator)
    
    odds1 = float(odds1)
    odds2 = float(odds2)
    
    if odds1_type == 'american':
        
        if odds1 > 0:
            odds1 = odds1/100
        elif odds1 < 0:
            odds1 = odds1*-1
            odds1 = 100/odds1
            
    if odds2_type == 'american':
        
        if odds2 > 0:
            odds2 = odds2/100
        elif odds2 < 0:
            odds2 = odds2*-1
            odds2 = 100/odds2
        
    profitability = 'undefined'
            
    if odds1*odds2 <= 1:
        profitability = 'be/loss'
    elif odds1*odds2 > 1:
        profitability = 'win'
        
    if odds1 <= odds2:
        
        bet1 = 1
        bet2 = ((bet1*(odds1 + 1))/(odds2 + 1))
        
    elif odds2 < odds1:
        
        bet2 = 1
        bet1 = ((bet2*(odds2 + 1))/(odds1 + 1))
        
    gain = (bet1*odds1 + bet1)/(bet1 + bet2)
        
    return bet1, bet2, profitability, gain

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'active')
    
@bot.message_handler(func = lambda message: True)
def handle_message(message):
    words = [word.strip() for word in message.text.split(',')]
    
    odds1, odds1_type, odds2, odds2_type = words
    
    bet1, bet2, profitability, gain = arb_bet_sizer_equal(odds1, odds1_type, odds2, odds2_type)
    
    response = f'profitability: {profitability}, bet1: {bet1}, bet2: {bet2}, gain: {gain}'
    
    bot.reply_to(message, response)
    
    
while True:
    try:
        bot.polling()
    
    except Exception:
        
        time.sleep(3)



