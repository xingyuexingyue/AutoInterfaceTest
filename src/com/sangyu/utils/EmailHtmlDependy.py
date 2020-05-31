"""
这里有一些用来拼接Html的方法

主要用到的思想是：将要显示在邮件中HTML的数据像字符串一样拼接起来


user: 2020 by pyp
"""

import time

from com.sangyu.utils.ExcelPublicInformation import ExcelPublicInfomation


def buildHead(date_time, all_case, all_run, error_case, no_run):
    """
    html中的第一部分
    :param date_time:
    :return:
    """
    return """
        <style>
         @charset "utf-8";
    /* CSS Document */
    .tabtop13 {
    	margin-top: 13px;
    }
    .tabtop13 td{
    	background-color:#ffffff;
    	height:25px;
    	line-height:150%;
    }
    .font-center{ text-align:center}
    .btbg{background:#e9faff !important;}
    .btbg1{background:#f2fbfe !important;}
    .btbg2{background:#f3f3f3 !important;}
    .biaoti{
    	font-family: 微软雅黑;
    	font-size: 26px;
    	font-weight: bold;
    	border-bottom:1px dashed #CCCCCC;
    	color: #255e95;
    }
    .titfont {

    	font-family: 微软雅黑;
    	font-size: 16px;
    	font-weight: bold;
    	color: #255e95;
    	background: url(../images/ico3.gif) no-repeat 15px center;
    	background-color:#e9faff;
    }
    .tabtxt2 {
    	font-family: 微软雅黑;
    	font-size: 14px;
    	font-weight: bold;
    	text-align: right;
    	padding-right: 10px;
    	color:#327cd1;
    }
    .tabtxt3 {
    	font-family: 微软雅黑;
    	font-size: 14px;
    	padding-left: 15px;
    	color: #000;
    	margin-top: 10px;
    	margin-bottom: 10px;
    	line-height: 20px;
    }
        </style>

         <table width="100%" border="0" cellspacing="0" cellpadding="0" align="center">
          <tr>
            <td align="center" class="biaoti" height="60">每日接口用例批量执行情况</td>
          </tr>
          <tr>
            <td align="right" height="25">
            
            """ + """ 所有用例数: """ + str(all_case) + """ / """ + """ 执行用例数：""" + str(all_run) + """ / """ + """ 执行失败用例数：""" + str(error_case) + """ /   """ +date_time + """
    </td>
          </tr>
        </table>

        <table width="100%" border="0" cellspacing="1" cellpadding="4" bgcolor="#cccccc" class="tabtop13" align="center">
          <tr>
            <td class="btbg font-center titfont">test_id</td>
            <td class="btbg font-center titfont" >功能模块</td>
            <td class="btbg font-center titfont">url</td>
            <td class="btbg font-center titfont">执行结果</td>
          </tr>  
           """


def buildHtml(list):
    """
    拼接html中的所有部分
    :param list: 要显示在页面的数据
    :return:
    """
    date_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    excel_public_information = ExcelPublicInfomation()
    all_case = excel_public_information.getAllCaseNums()
    all_run = excel_public_information.getAllRunCaseNums()
    error_case = len(list)
    no_run = all_case - all_run
    head = buildHead(date_time, all_case, all_run, error_case, no_run)
    body = buildTable(list)
    tail = buildTail()

    return str(head) + str(body) + str(tail)


def buildTail():
    """
    html中的第三部分
    :return:
    """
    return """
        </table>
        """


def buildTable(list):
    """
    html中的第二部分
    list每个数据表示每行显示的内容
    :param list: 要显示在页面的数据
    :return:
    """
    tr = ''
    for case in list:
        tr += """  
            <tr>
            <td>
            """ + case.getId() + """
            </td>
            <td>
            """ + case.getFeatures() + """
            </td>
            <td>
            """ + case.getUrl() + """
            </td>
            <td>
            """ + case.getResult() + """
            </td>
           </tr>
            """
    return tr
