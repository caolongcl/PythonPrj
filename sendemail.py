# -*- coding: utf-8 -*-#
"""
docstring
"""

#解析excel
import xlrd
from xlutils.copy import copy

#发送邮件
import smtplib
from email.header import Header
from email.utils import parseaddr,formataddr
from email.mime.text import MIMEText


class sendemail:
    def __init__(self,senduser, mailuser,mailpass,file,mailhost,mailport):
        self.senduser = senduser
        self.mail_host = mailhost
        self.mail_user = mailuser
        self.mail_pass = mailpass
        self.mail_port = mailport
        self.file = file
        #
        self.mailf_index = "索引"
        self.mailf_recv = "接收者"
        self.mailf_emailaddr = "邮箱"
        self.mailf_subject = "邮件标题"
        self.mailf_content = "邮件正文"
        self.mailf_senttime = "发送时间"
        self.mailf_succeed = "发送成功"

    def open_excelr(self):
        """open excel for read"""
        try:
            data = xlrd.open_workbook(self.file)
            return data
        except Exception as e:
            print(str(e))
            return None

    def excel_table_byindex(self):
        """execl"""
        data = self.open_excelr()
        table = data.sheets()[0]
        nrows = table.nrows  # 行数
        colnames = table.row_values(0)  # 某一行数据,表头
        lists = []
        for rownum in range(1, nrows):
            row = table.row_values(rownum)
            if row:
                if row[0]:
                    content = {}
                    content[self.mailf_index] = rownum + 1
                    for i in range(len(colnames)):
                        content[colnames[i]] = row[i]
                    lists.append(content)
        return lists

    # 设置execl单元格的值
    def execl_writecell(self, mailvalue):
        rdata = self.open_excelr()
        wdata = copy(rdata)
        wtable = wdata.get_sheet(0)

        if mailvalue:
            for index in range(len(mailvalue)):
                if mailvalue[index][self.mailf_succeed] == 1:
                    wtable.write(mailvalue[index][self.mailf_index] - 1, 5, 1)
                else:
                    pass
            wdata.save(self.file)
        else:
            pass



    # 发送邮件
    def format_addr(self,s):
        """
        :param s: name<xxx@xx.com>
        :return:
        """
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    # 准备发送
    def send_begin(self):
        try:
            server = smtplib.SMTP()
            #server.set_debuglevel(True)
            server.connect(self.mail_host, self.mail_port)
            server.starttls()
            server.login(self.mail_user, self.mail_pass)
            print("send_begin...")
            return True, server
        except Exception as e:
            print("error!!! send_begin failed : " + str(e))
            return False, None

    def send_end(self,state):
        if state[0]:
            state[1].quit()
        else:
            pass

    # 一次性发送全部
    def send_all_mail(self,mailvalue):
        """
        :param mailvalue:
        :return:
        """
        sendaddr = self.mail_user
        fromaddr = self.senduser + "<" + sendaddr + ">"
        state = self.send_begin()
        if state[0]:
            try:
                # 发送数据
                for index in range(len(mailvalue)):
                    #print(index)
                    if not mailvalue[index][self.mailf_succeed]:
                        msg = MIMEText(mailvalue[index][self.mailf_content],
                                       _subtype='html', _charset='utf-8')
                        msg['Subject'] = Header(mailvalue[index][self.mailf_subject],
                                                'utf-8').encode()
                        msg['From'] = self.format_addr(fromaddr)
                        msgto = mailvalue[index][self.mailf_recv] + "<" + \
                                mailvalue[index][self.mailf_emailaddr] + ">"
                        msg["To"] = self.format_addr(msgto)
                        recvaddr = mailvalue[index][self.mailf_emailaddr]
                        #print(msgto)
                        state[1].sendmail(sendaddr, recvaddr, msg.as_string())

                        # 标记发送是否成功
                        mailvalue[index][self.mailf_succeed] = 1
                self.send_end(state)
                return True
            except Exception as e:
                print("send failed : " + str(e))
                return False

    def send(self):
        tables_values = self.excel_table_byindex()

        if self.send_all_mail(tables_values):
            self.execl_writecell(tables_values)
            return True
        else:
            return False
