def generate_html(w, base64s, data, is_landscape):
    signed_by_html = "".join([
        f"<tr>"
        f"<td style='padding:0px 5px;'>"
        f"&nbsp;&nbsp;- "
        f"{approver.fullname if approver.fullname else 'N/A'} "
        f"<b>[{approver.status if approver.status else 'N/A'}]</b> "
        f"{approver.timestamp if approver.timestamp else 'N/A'} "
        f"</td>"
        f"</tr>"
        for approver in data.detailApprover
    ])

    if is_landscape:
        html_string = f"""
        <html>
            <head>
                <style>
                    * {{
                        font-size: 20px;
                        font-family: 'Verdana', sans-serif;
                    }}
                    table {{
                        margin-left: 10px;
                        width: 1200px;
                    }}
                    .signature-img {{
                        width: 150px;
                    }}
                </style>
            </head>
            <body style="width: {w};">
                <div style="overflow:hidden;position: absolute;bottom:0;right:0;line-height:1.5;">
                    <table>
                        <tr>
                            <td style="margin-left:12px;margin-bottom:25px;">
                                <b>Signed by:</b><br/>
                            </td>
                        </tr>
                        {signed_by_html}
                    </table>
                    <table width="100%">
                        <tr>
                            <td width="150">
                                <img src="data:image/jpeg;base64,{base64s}" class="signature-img"/>
                            </td>
                            <td>
                                Title: {data.title}<br/>
                                Document ID: <b>{data.documentId}</b><br/>
                                Status: 
                                {data.status}
                                <br/>
                                Document signed digitally using Approval Management System (AnyFlow) on {data.information}
                            </td>
                        </tr>
                    </table>
                </div>
            </body>
        </html>
        """
    else:
        html_string = f"""
        <html>
            <head>
                <style>
                    * {{
                        font-size: 20px;
                        font-family: 'Verdana', sans-serif;
                    }}
                    table {{
                        margin-left: 10px;
                        width: 1200px;
                    }}
                    .signature-img {{
                        width: 150px;
                    }}
                </style>
            </head>
            <body style="width: {w};">
                <div style="overflow:hidden;position: absolute;bottom:0;">
                    <table>
                        <tr>
                            <td style="margin-left:12px;margin-bottom:25px;">
                                <b>Signed by:</b><br/>
                            </td>
                        </tr>
                        {signed_by_html}
                    </table>
                    <table style="margin-top: 20px" width="100%">
                        <tr>
                            <td width="150">
                                <img src="data:image/jpeg;base64,{base64s}" class="signature-img"/>
                            </td>
                            <td style="padding-left: 10px">
                                Title: {data.title}<br/>
                                Document ID: <b>{data.documentId}</b><br/>
                                Status: 
                                {data.status}
                                <br/>
                                Document signed digitally using Approval Management System (AnyFlow) on {data.information}
                            </td>
                        </tr>
                    </table>
                </div>
            </body>
        </html>
        """
    return html_string
