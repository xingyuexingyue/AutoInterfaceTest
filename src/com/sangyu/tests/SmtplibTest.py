import time
from email.mime.text import MIMEText
import smtplib

# 接受：收件人，主题，内容
# 返回：邮件发送结果
from email.utils import formataddr

from com.sangyu.core.DealWithTestCase import DealWithTestCase
from com.sangyu.utils.EmailHtmlDependy import buildHtml


def send_mail():
    """

    :param mail_title: 邮件标题
    :param mail_content: 邮件内容
    :return:
    """
    mail_title = "关中大侠的测试邮件" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    deal_with_test_case = DealWithTestCase()
    after_test_case_list = deal_with_test_case.afterTest()
    mail_msg = buildHtml(after_test_case_list)
    ret = True  # 用来标识邮件是否发送成功
    try:
        from_mail = "935789914@qq.com"  # 发件人
        my_pass = 'pwflovsgocvobead'  # 发件人邮件授权码

        msg = MIMEText(mail_msg, 'html', 'utf-8')  # 邮件内容
        '''
        下面的代码中可以添加收件人组
        '''
        msg['from'] = formataddr(["FromPanPan", from_mail])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号  # 对应发件人邮箱昵称、发件人邮箱账号
        msg['to'] = formataddr(["春风十里不如你", "2305639952@qq.com"])  # 对应收件人邮箱昵称、收件人邮箱账号
        msg['to'] = formataddr(["春风十里不如", "364214799@qq.com"])  # 对应收件人邮箱昵称、收件人邮箱账号
        msg['to'] = formataddr(["春风十里不", "935789914@qq.com"])  # 对应收件人邮箱昵称、收件人邮箱账号

        msg['subject'] = mail_title  # 邮件的主题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25  # qq邮箱服务器
        server.login(from_mail, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码

        '''
        如果只将收件人添加到这个，在邮件中不会显示收件人组
        '''
        server.sendmail(from_mail, ["2305639952@qq.com", "364214799@qq.com", "935789914@qq.com"],
                        msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接

        # txt = email.mime.text.MIMEText(mail_content)
        # msg.attach(txt)

    except Exception:
        ret = False

    if ret:
        return "success"
    else:
        return "error"


if __name__ == '__main__':
    send_mail()
