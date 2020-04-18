import os
import smtplib
import email.utils
from email.mime.text import MIMEText

# 環境変数
mail_from = os.environ['MAIL_FROM']
rcpt_to = os.environ['RCPT_TO']
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_user = os.environ['SMTP_USER']
smtp_password = os.environ['SMTP_PASSWORD']

# Body
msg = MIMEText('テストメッセージ\n' + '送信テスト\n')
msg['To'] = email.utils.formataddr(('テスト宛先', mail_from))
msg['From'] = email.utils.formataddr(('テスト送信元', rcpt_to))
msg['Subject'] = 'テストメール'

# smtplib を使ったメール送信
server = smtplib.SMTP(smtp_server, smtp_port)
server.set_debuglevel(True)
try:
    server.ehlo()
    server.starttls()
    server.login(smtp_user, smtp_password)
    server.sendmail(mail_from, rcpt_to, msg.as_string())
finally:
    server.quit()