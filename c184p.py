from tkinter import *
import requests
import json

root=Tk()
root.title("News Widget")
root.geometry("600x620")

label_BBC = Label(root, text="BBC News Update", font=("comicsans", 18))
label_BBC.place(relx=0.5, rely=0.01, anchor=N)

news1 = Label(root, font=("bold"), wraplength=500, fg="red")
news1.place(relx=0.12, rely=0.1, anchor=W)

news_desc1 = Label(root, font=("comicsans",10,"bold"), wraplength=500)
news_desc1.place(relx=0.1, rely=0.2, anchor=W)

news2 = Label(root, font=("bold"), wraplength=500, fg="red")
news2.place(relx=0.12, rely=0.3, anchor=W)

news_desc2 = Label(root, font=("comicsans",10,"bold"), wraplength=500)
news_desc2.place(relx=0.1, rely=0.4, anchor=W)

news3 = Label(root, font=("bold"), wraplength=500, fg="red")
news3.place(relx=0.12, rely=0.5, anchor=W)

news_desc3 = Label(root, font=("comicsans",10,"bold"), wraplength=500)
news_desc3.place(relx=0.1, rely=0.6, anchor=W)

news4 = Label(root, font=("bold"), wraplength=500, fg="red")
news4.place(relx=0.12, rely=0.7, anchor=W)

news_desc4 = Label(root, font=("comicsans",10,"bold"), wraplength=500)
news_desc4.place(relx=0.1, rely=0.8, anchor=W)

news5 = Label(root, font=("bold"), wraplength=500, fg="red")
news5.place(relx=0.12, rely=0.9, anchor=W)

news_desc5 = Label(root, font=("comicsans",10,"bold"), wraplength=500)
news_desc5.place(relx=0.1, rely=0.97, anchor=W)

api_requests = requests.get("https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=1549afeab5a5461c9e3a1978ec86106d")
api_output_json = json.loads(api_requests.content)

news1_title_info = api_output_json['articles'][0]['title']
news1_desc_info = api_output_json['articles'][0]['description']

news2_title_info = api_output_json['articles'][1]['title']
news2_desc_info = api_output_json['articles'][1]['description']

news3_title_info = api_output_json['articles'][2]['title']
news3_desc_info = api_output_json['articles'][2]['description']

news4_title_info = api_output_json['articles'][3]['title']
news4_desc_info = api_output_json['articles'][3]['description']

news5_title_info = api_output_json['articles'][4]['title']
news5_desc_info = api_output_json['articles'][4]['description']

news1['text'] = "Title 1: " + news1_title_info
news_desc1['text'] = "desc 1: " + news1_desc_info

news2['text'] = "Title 2: " + news2_title_info
news_desc2['text'] = "desc 2: " + news2_desc_info

news3['text'] = "Title 3: " + news3_title_info
news_desc3['text'] = "desc 3: " + news3_desc_info

news4['text'] = "Title 4: " + news4_title_info
news_desc4['text'] = "desc 4: " + news4_desc_info

news5['text'] = "Title 5: " + news5_title_info
news_desc5['text'] = "desc 5: " + news5_desc_info

root.mainloop()
