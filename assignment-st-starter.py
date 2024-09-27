# import packages
import streamlit as st 

# show the title
st.title('Titanic app by Jeremy Fu')

# read csv and show the dataframe
import pandas as pd
df_train=pd.read_csv('train.csv')

# create a figure with three subplots, size should be (15, 5)
# show the box plot for ticket price with different classes
# you need to set the x labels and y labels
# a sample diagram is shown below
import streamlit as st  
import pandas as pd  
import matplotlib.pyplot as plt  
import seaborn as sns  
  
# 假设你有一个DataFrame，名为df，其中包含至少两列：'class'（表示不同类别）和'ticket_price'（表示票价）  
# 这里我们创建一个示例DataFrame  
data = {  
    'class': ['Economy', 'Business', 'Economy', 'First', 'Business', 'Economy', 'First', 'Business', 'First', 'Economy'],  
    'ticket_price': [100, 500, 120, 1000, 600, 110, 1200, 700, 1500, 90]  
}  
df = pd.DataFrame(data)  
  
# 创建一个画布和子图  
fig, axes = plt.subplots(1, 3, figsize=(15, 5))  # 1行3列的子图  
  
# 这里我们只使用一个子图来展示箱线图，其他两个子图可以留空或用于其他图表  
sns.boxplot(x='class', y='ticket_price', data=df, ax=axes[0])  
axes[0].set_xlabel('Class')  
axes[0].set_ylabel('Ticket Price')  
axes[0].set_title('Box Plot of Ticket Prices by Class')  
