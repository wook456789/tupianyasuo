import requests
from bs4 import BeautifulSoup
import pandas as pd

# 目标网页URL
url = 'https://ling017.github.io/Python-coursework/'

# 发送HTTP请求获取网页内容
response = requests.get(url)
response.encoding = 'utf-8'  # 设置编码
html_content = response.text

# 使用BeautifulSoup解析网页内容
soup = BeautifulSoup(html_content, 'html.parser')

# 假设书籍信息在特定的HTML标签中，例如<div class="book-item">
books = soup.find_all('div', class_='book-item')

# 创建一个列表来存储书籍信息
book_list = []

# 遍历每个书籍元素，提取信息
for book in books:
    title = book.find('h2').text.strip()  # 假设书名在<h2>标签中
    author = book.find('p', class_='author').text.strip()  # 假设作者在<p class="author">标签中
    price = float(book.find('span', class_='price').text.strip('¥'))  # 假设价格在<span class="price">标签中
    sales = int(book.find('span', class_='sales').text.strip('销售: '))  # 假设销售情况在<span class="sales">标签中
    
    # 将书籍信息添加到列表中
    book_list.append({
        'Title': title,
        'Author': author,
        'Price': price,
        'Sales': sales
    })

# 将列表转换为DataFrame
df = pd.DataFrame(book_list)

# 根据销售情况排序
df_sorted = df.sort_values(by='Sales', ascending=False)

# 将排序后的结果保存到本地CSV文件
df_sorted.to_csv('sorted_books.csv', index=False, encoding='utf-8')

print("书籍信息已成功抓取并排序，结果已保存到 sorted_books.csv 文件中。")