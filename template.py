def refine_content(text):
    # Находим первый тег и его позицию
    first_tag_match = text.find("<")
    if first_tag_match != -1:
        # Обрезаем текст от последнего символа ">"
        refined_text = text[first_tag_match: - 1]
    else:
        # Если символ ">" не найден, оставляем текст как есть
        refined_text = text
    # Находим последний тег и его позицию
    last_gt_position = refined_text.rfind(">")
    if last_gt_position != -1:
        # Обрезаем текст от последнего символа ">"
        refined_text = refined_text[:last_gt_position + 1]
    else:
        # Если символ ">" не найден, оставляем текст как есть
        refined_text = refined_text

    return refined_text


def template (sender,mail, subject, date, content):

    refined_content = refine_content(content)

    p_style = 'margin-left: 10px; font-size: 18px; font-family: sans-serif;'
    div_style='margin: 0 auto; padding: 10px; width: 800px; color:#eceef2 ;background-color:linear-gradient(180deg, rgba(240,238,238,1) 0%, rgba(255,255,255,1) 100%); border-radius: 20px;  box-shadow: 0 1px 4px rgba(0, 0, 0, .3), -23px 0 20px -23px rgba(0, 0, 0, .8), 23px 0 20px -23px rgba(0, 0, 0, .8), 0 0 40px rgba(0, 0, 0, .1) inset; overflow-wrap: break-word;'

    template_htm = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Вам письмо от den.fstack@yandex.ru</title>
        </head>
        <body style="margin: 0; padding: 0; box-sizing: border-box;">
            <div style="background-color: #1a1a1a; padding-bottom: 10px;">
                <div style="display: flex; margin: 0 auto; width: 800px; font-family: sans-serif; justify-content: end; align-items: center; color:#a8b4b4">
                    <p>🛠️ accomplished by
                        <a href="https://my-3d-cv.vercel.app/" target="_blank" style="cursor: pointer; text-decoration: none; color:#915eff;"><b> DEN &nbsp;</b>
                        </a>
                    </p>
                    <p>|
                        <a href="https://github.com/alsam2009" target="_blank" style="color:#915eff;">GitHub</a>
                    </p>
            </div>
            <div style='{div_style}'>
                <p style='{p_style}'><b>From:</b> {sender}</p>
                <p style='{p_style}'><b>To:</b> {mail}</p>
                <p style='{p_style}'><b>Subject:</b> {subject} </p>
                <p style='{p_style}'><b>Date:</b> {date}</p>
                <p style='{p_style}'><b>Текст сообщения:</b> 👇 </p>
                <hr>
                <div>
                    {refined_content}
                </div>
            </div>
        </body>
        </html>
    """
    return template_htm