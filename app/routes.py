from flask import Flask, render_template_string, request
from app import app
from app.fake_data import FAKE_REAL_ESTATE_DATA

@app.route('/api/real-estate', methods=['GET'])
def get_real_estate():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    start = (page - 1) * per_page
    end = start + per_page

    real_estates = FAKE_REAL_ESTATE_DATA[start:end]

    # Создание HTML-таблицы
    table_rows = []
    for item in real_estates:
        row = f"<tr><td>{item['id']}</td><td>{item['name']}</td><td>{item['developer']}</td><td>{item['address']}</td><td>{item['price']}</td><td>{item['area']}</td></tr>"
        table_rows.append(row)

    html_table = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Данные о новостройках</title>
            <style>
                table {{
                    border-collapse: collapse;
                    width: 100%;
                }}
                th, td {{
                    border: 1px solid black;
                    padding: 8px;
                    text-align: left;
                }}
            </style>
        </head>
        <body>
            <h1>Список новостроек</h1>
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Название</th>
                        <th>Застройщик</th>
                        <th>Адрес</th>
                        <th>Цена</th>
                        <th>Площадь</th>
                    </tr>
                </thead>
                <tbody>
                    {''.join(table_rows)}
                </tbody>
            </table>
        </body>
        </html>
    """
    return html_table