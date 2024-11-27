import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import requests
from streamlit_lottie import st_lottie
from PIL import Image

df_clean = pd.read_csv("youtube_data_full_clean.csv")
def load_lot2(url):
    r= requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
     
lot_cod2 = load_lot2("https://lottie.host/fe1e5bce-3ea8-40de-90b1-46551981f5d8/prHg1lwMrv.json")    
st_lottie(lot_cod2,height=200,key='o')

# Inject custom CSS to ensure title is centered

# Inject custom CSS to center the title
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@200..1000&display=swap');
        *{
            font-family: "Cairo", sans-serif;
        }
        body {
            direction:rtl;

        }
        .streamlit-expanderHeader {

            font-family: monospace;
        }
        .stTextInput>div>div>input {
            text-align: right;
        }
        h1 {
            text-align: center !important;  /* Ensures title is centered */
            width: 100%;  /* Makes sure it takes up full width */
            display: block; /* Ensures it is a block element */
        }
        .stMarkdown {
            text-align: right;
        }
        .prediction-output {
            font-size: 18px;
            font-weight: bold;
            text-align: right;
            direction: rtl;
        }
        hr{ width:100%;height:10px;background:#000;}       
    </style>
""", unsafe_allow_html=True)

# Title text
st.markdown("""
    <p style="font-size: 40px; text-align:center;font-weight: bold;"> رَائِجْ</p>
""", unsafe_allow_html=True)

st.markdown("""
   <strong style="font-weight: bold;"> مبدع؟ مؤثر؟</strong> وش تنتظر افتح لك قناه بس انتظر شوي خلنا نوضح لك الصوره تخيل ان يوتيوب فيه اكثر من ٢.٥ مليار مشاهد نشط ادري جالس تحسب الارباح لكن لا تطمع فينا خطوه بخطوه و رائج جاي يوضح لك الصوره 😉
""", unsafe_allow_html=True)

# st.markdown("مبدع؟مؤثر؟ وش تنتظر افتح لك قناه بس انتظر شوي خلنا نوضح لك الصوره تخيل ان يوتيوب فيه اكثر من ٢.٥ مليار  مشاهد نشط ادري جالس تحسب الارباح لكن لا تطمع فينا خطوه بخطوه و رائج جاي يوضح لك الصوره 😉",unsafe_allow_html=True)

# videoooooooo
# Display a video from a file
st.markdown("""
    <p style="font-size: 30px; text-align: right;font-weight: bold;">من وين رائج يتفلسف؟</p>
""", unsafe_allow_html=True)
# lot_cod3 = load_lot2("https://lottie.host/10a97fbe-7d43-46e1-b6a2-27fcd4b1b2bf/WnZwrucv10.json")    
# st_lottie(lot_cod3,height=50)
st.markdown("<hr>",unsafe_allow_html=True)

# Define the columns with specific ratios
col0,col1, col2,col6, col3,col4,col7,col5 = st.columns([0.7,2,1,0.7,2,1,0.7, 2])  # Add small columns for vertical lines
with col0:
    st.write('')
# First column
with col1:
    image = Image.open('lastwebimage.png')

        # st.write("youtube.meالموقع:  ")
#     st.markdown("""
#     <p style="font-size: 15px; text-align: center;font-weight: bold;">الموقع youtube.me</p>
# """, unsafe_allow_html=True)
    st.image('youtubeme.png', width=96) 

    # st.image("lastwebimage.png", width=90)
    st.image(image, width=96) 
    # st.write("البيانات تجمعت بتاريخ 27/11/2024")
    # st.write("2016-2024")

# Vertical line after col1
with col2:
    st.markdown(
    """
    <div style="border-left: 2px solid black; height: 130px;text-align: center"></div>
    """,
    unsafe_allow_html=True
)
with col6:
    st.write('')
# First column
# Second column
with col3:
    st.markdown("""
    <p style="font-size: 10px; text-align: center;font-weight: bold;">البيانات تركز على القنوات الاعلى مشاهده في المملكة العربية السعوديه</p>
""", unsafe_allow_html=True)
    st.write("عدد القنوات :3585")
    st.write("")

# Vertical line after col2
with col4:
     st.markdown(
    """
    <div style="border-left: 2px solid black; height: 130px;text-align: center"></div>
    """,
    unsafe_allow_html=True
)
with col7:
    st.write('')

# Third column
with col5:
     st.markdown("""
    <p style="font-size: 16px; text-align: center;font-weight: bold;"> البيانات تجمعت من 2016-2024</p>
""", unsafe_allow_html=True)
     st.markdown("""
    <p style="font-size: 10px; text-align: center; font-weight: bold; color: red;">اخر شهرين من 2024 ما انحسبو </p>
""", unsafe_allow_html=True)












st.markdown("<hr>",unsafe_allow_html=True)
st.markdown("""
    <p style="font-size: 30px; text-align: right;font-weight: bold;"> ثورة اليوتيوب</p>
""", unsafe_allow_html=True)
# st.header("كيف تغير المشاهدات على مر السنوات؟")

st.markdown(""" قبل 2016 كان فيه صعوبه في فتح القنوات بحيث كان صاحب المحتوى عشان يفتح قناه لازم يكون فيه وسيط شركه بينه و بين اليوتيوب تاخذ ارباح بالتالي قل الاهتمام بصناعة المحتوى في 2016 انلغى هذا النهج و صار صاحب المحتوى قادر فتح قناة بدون وسيط و بالتالي يزيد من فرصة صناعة المحتوى و المشاهدات
 """)


mycolumns = df_clean.columns[12:21]
result = pd.DataFrame({
    "Year": mycolumns,  # Years as the column headers
    "Total": df_clean[mycolumns].sum(axis=0)  # Sum across rows (axis=0 means columns)
})
result["Year"]= result["Year"].str.replace("_views", "")
result["Year"] = pd.to_datetime(result["Year"],format="%Y").dt.year

fig = px.line(
    result, 
    x="Year", 
    y="Total", 
    text=['{:.4}B'.format(x / 1000000000) for x in result['Total']],
    markers=True, height=500,width=730
)
fig.update_traces(
    textposition="top center", 
    line=dict(width=3),
    line_color="red",
    marker=dict(size=10, color="red", line=dict(width=2, color="red")),
)
fig.update_layout(
    title=dict(text="مجموع المشاهدات لكل سنه ", font=dict(size=15),x= 0.4),
    xaxis=dict(
        tickmode="linear", 
        title=dict(
            text="السنوات",  
            font=dict(size=15, family="Arial", weight="bold")  
        ),
        linecolor='white',  
        #tickfont=dict(color="black"), 
        showgrid=False, 
        gridcolor="lightgrey"  
    ),
    yaxis=dict(
        title=dict(
            text="مجموع المشاهدات",  
            font=dict(size=15, family="Arial", weight="bold")  
        ),  # Y-axis title in Arabic
        showgrid=True,  # Show gridlines
        gridcolor="lightgrey",  # Set gridline color
        #tickfont=dict(color="black"),
        #standoff=20)
    ),  # تحديد المسافات حول الرسم
    #borderwidth=2, 
    #bordercolor="white"
    #plot_bgcolor="#282828",  # Dark background for the plot
    #paper_bgcolor="#282828",# Dark background for the entire paper
)
# Add a circle at a specific point
specific_year = 2021
specific_value = result.loc[result["Year"] == specific_year, "Total"].values[0]
fig.add_shape(
    type="circle",
    xref="x", yref="y",
    x0=specific_year - 0.2, x1=specific_year + 0.2,
    y0=specific_value - 1000000000, y1=specific_value + 1000000000,  # Adjust radius as needed
    line_color="black",
    line_width=2,
)
specific_year = 2020
specific_value = result.loc[result["Year"] == specific_year, "Total"].values[0]
fig.add_shape(
    type="circle",
    xref="x", yref="y",
    x0=specific_year - 0.2, x1=specific_year + 0.2,
    y0=specific_value - 1000000000, y1=specific_value + 1000000000,  # Adjust radius as needed
    line_color="black",
    line_width=2,
)

fig
st.write('شفت المشاهدات؟ ترا تنقسم الي تصنيفات بناء على نوع المحتوى مثل المحتوى التعليمي,الترفيهي,الخ كل محتوى وله جمهوره')

#  اختيار السنة
option = st.selectbox(
    "حدد السنة وخلنا نشوف الصنيفات المتصدره :",
    (2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024)
)

st.write("السنة المختارة هي:", option)

# تجميع البيانات حسب الفئة للسنة المختارة
df_yearly = df_clean.groupby('category')[f"{option}_views"].sum().reset_index()

# اختيار أعلى 5 تصنيفات
df_top5 = df_yearly.sort_values(by=f"{option}_views", ascending=False).head(5)
youtube_colors = ['#FF0000', '#282828', '#FFFFFF', '#D3D3D3', '#696969']
# إنشاء الرسم الدائري
fig = px.pie(
    df_top5, 
    names='category', 
    values=f"{option}_views", 
    title=f'أعلى 5 تصنيفات مشاهدة في السنة {option}', 
    labels={'category': 'التصنيفات', f"{option}_views": 'مجموع المشاهدات'}, 
    hole=0.3,  # تحويله إلى دونت شارت (اختياري)
    width=750,
    height=500,
    color_discrete_sequence=youtube_colors
)

# تخصيص النصوص والألوان
fig.update_traces(
    textposition="inside", 
    textinfo="percent+label",  # عرض النسبة مع التسمية
    marker=dict(line=dict(color='white', width=2))  # خطوط بيضاء تفصل بين القطاعات
)

# تخصيص التصميم العام
fig.update_layout(
    title=dict(
        text=f"أعلى 5 تصنيفات مشاهدة في السنة {option}",
        font=dict(size=20),
        x=0.309  # جعل العنوان في المنتصف
    ),
    legend=dict(
        title="التصنيفات",
        orientation="h",  # جعل الأسطورة أفقية
        x=0.5, y=-0.1, xanchor="center", yanchor="top"
    )
)

fig

lot_cod3 = load_lot2("https://lottie.host/73189f58-0810-43b7-9552-081aba72fd0c/NCSKRMyuJy.json")

col1, col2 = st.columns([5, 1])  # Adjust the ratio as needed

with col1:
    st.write("")
    st.write("")

    st.markdown("""
        <p style="font-size: 20px; text-align: right;">تصنيفك ما شفته من التصنيفات المتصدره؟ اختاره هنا وخلنا نكتشف السبب</p>
    """, unsafe_allow_html=True)

with col2:
    st_lottie(lot_cod3, height=100)




categories = [
    'Comedy', 'Entertainment', 'Film & Animation', 'Gaming', 'Music',
    'People & Blogs', 'general', 'Sports', 'Education', 'Science & Technology',
    'Pets & Animals', 'Travel & Events', 'Autos & Vehicles', 'Nonprofits & Activism',
    'News & Politics', 'Howto & Style'
]

category_texts = {
    'Comedy': 'لاحظوا أن المشاهدات في 2021 ارتفعت بشكل كبير، والسبب ببساطة هو جائحة كورونا. الناس كانوا يهربون من جو الاكتئاب والحزن اللي سببتها الجائحة، فصاروا يبحثون عن محتوى مسلّي.',
    'Entertainment': 'صدمه! متخيل ان محتوى الترفيهي تزيد مشاهداته كل سنه! هل اغلبهم اطفال؟ يحتاج دراسه اخرى لان لو كان الجواب نعم هذا يعني معظم الاهالي يفضلون طرق مختصره  يشغلون فيه الطفل او يسكتونه عن البكاء؟  وهذي النقطه تأثر على الطفل سلبيا',
    'Film & Animation': 'الأفلام والرسوم المتحركة في 2022 كانت مولعة! ممكن يكون بسبب إن الأفلام الي نزلت في 2022  كانت ترند او مشوقه وفي نفس الوقت متاحة بشكل مجاني',
    'Gaming': 'بدأت قنوات الألعاب تظهر بعد ps4 و Xbox one بثلاث سنوات وكان ارتفاعها بطيء حتى جاتنا العاب البتل رويال في 2018 وسببت ارتفاع عالي لأنه أصحاب الأجهزة المختلفة يقدروا يخشوا في قيم واحد وجات جائحة كورونا ورفعت المشاهدات',
    'Music': 'ما كان في ناس كثير تسمع اغاني فكان الارتفاع فيها شبه منعدم حتى جات جائحة كورونا وقررت الشركات وأولهم ابل فرض مبلغ اشتراك على سماع الموسيقى فالكثيرون راحوا ليوتيوب لأنه مجاني (حتى الان )',
    'People & Blogs': 'مع تطور الجوالات وكاميراتها (مثل ايفون 7 و سامسونج) صار الكل يقدر يصور يومياته ويعدل على الفيديوهات بجواله فقط وزادت المشاهدات مع زيادة صناع المحتوى ويوم  2019 نزل مع مشاكل اليوتيوب ولكن صناع المحتوى قدروا يتغلبوا على ذي الصعوبات ولكن صدمهم الحجر الكلي مع الجائحة وعاد المحتوى للنزول بس هما قدها وبحكم ان توهم طالعين من ماهو اسوا فذي عدوها ولكن للأسف رجع ينزل وهذا التذبذب لازال موجود.',
    'general': 'فئة لصناع المحتوى اللي لازالوا يتخبطوا في بداياتهم للاسف ارتفعت فترة بسيطة ثم هبطت بقوة.',
    'Sports': 'لمتعصبي الاندية والفرق صار لهم فئة خاصة ومباراياتهم جاهزة للعرض ويقدر يصور مقطع تحليلي ينافس عادل التويجري وأحمد الشمراني وبسنة 2018 الى 2020 حصل نزول فظيع وارتفاع مع الحجر لكن نزل مجدداَ ومازال مستمر',
    'Education': 'مع تطور التقنية اكيد الناس تطورت وبدأت تبحث عن مصادر تعلم ولقت اليوتيوب افضل مصدر للمعلم فهو يكسب فلوس والمتعلم يكتسب مهارات ومع الجائحة بدأ التعليم عن بعد وأول من اشتهر قناة عين التعليمية ومن انتهت الجائحة نزلت المشاهدات ثم ظهرت منصات التعليم عن بعد فاستمر التذبذب من بعدها',
    'Science & Technology': 'فئة من 2016 وهي تتذبذب ما بين ارتفاع ونزول لعدم ثبات المحتوى ما بين اصدرات الايفون المتكررة وتجارب العلوم وطارت المشاهدات فوق بعد ما بدأت مراجعات الاجهزة',
    'Pets & Animals': 'عانت من الانخفاض لفترة طويلة ومن ثم بدأت ترتفع مع ظهور الريلز ومحبي الخيول وأسامة الدغيري',
    'Travel & Events': 'الكل بيسافر بس الفلوس والكسل كانت مشكلة ومع تطور الجوالات وكاميراتها (مثل ايفون 7 و سامسونج) صار الكل يقدر يصور ويمنتج بجوال بجيبه والمشاهدين صاروا يقدروا يشوفوا شلالات نياغرا ومدائن صالح من بيوتهم  ',
    'Autos & Vehicles': 'طارت المشاهدات بعد ما صارت فيديوهات المراجعات موجودة واكيد السيارات اهم ما يشتريه المواطن وفيديوهات الميكانيكين حصلت مشاهداتها لكن نزلت مع الجائحة ومع ظهور التك توك تذبذت للان ',
    'Nonprofits & Activism': 'القنوات الدينية والشيوخ اندرجوا تحت ذي الفئة ومازالت تتذبذب ليومنا هذا لانه نفس المحتوى يكون انستا وتيك توك  .',
    'News & Politics': 'الأخبار والسياسة، المشاهدات كلها من الاباء واعمامنا ويحبوا يتابعوها من التلفزيون اكثر من اليوتيوب , ارتفعت المشاهدات بكورنا لانه المحطات قفلت لكن نزلت بعد ماانتهى الحجر .',
    'Howto & Style': ' بتتعلم الطبخ أو الخياطة ؟ محتاج تختصر على نفسك شغل البيت ؟ ذى الفئة تساعد اللي ماله كبير انه ما يطيح بالبير واثبتت فعاليتها اول السنوات ولكن مع ظهور التيك توك وانتهاء جائحة كورونا , ارتفعت شوية لكن الناس تبغا المعلومة بأقل من دقيقة'

}
df_clean =df_clean[df_clean['profile_name'] != 'Fantom Pro']
# Data preparation (replace df_clean with your actual DataFrame)
a = df_clean[['category', '2016_views', '2017_views', '2018_views', '2019_views', 
              '2020_views', '2021_views', '2022_views', '2023_views', '2024_views']]
a = a.groupby(['category']).sum()

data_dict = {category: a[a.index == category].to_numpy()[0] if category in a.index else [0]*9 for category in categories}

dfaa = pd.DataFrame({
    'Year': ['2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024'],
    **data_dict  # Dynamically add all categories as columns
})

# Streamlit user interaction: select a category
selected_category = st.selectbox("اختر التصنيف:", categories)

# Display a message or text for the selected category
# st.write(f"الفئة المختارة: {selected_category}")
st.write(category_texts[selected_category])  # Displaying the specific text for the selected category

# Plotly figure
fig = go.Figure()

# Add trace only for the selected category
fig.add_trace(go.Scatter(
    x=dfaa['Year'], 
    y=data_dict[selected_category], 
    mode='lines+markers',  # Lines with markers
    name=selected_category,
    marker=dict(size=8, color='red'),  # Marker size
    line=dict(width=2, color='red'),# Line width
))

# Customize the layout
fig.update_layout(
    title=dict(
        text=f"مشاهدات الفئة: {selected_category}",  # Title updates dynamically
        font=dict(size=10),
        x=0.5, y=0.9,
        xanchor="center", yanchor="top"
    ),
    xaxis=dict(
        title="السنوات",
        tickmode="linear",
        showgrid=False,
        gridcolor="lightgrey",
        linecolor="black",
        title_font=dict(size=14, family="Arial", weight="bold"),
        tickfont=dict(size=12, family="Arial", weight="bold")
    ),
    yaxis=dict(
        title="مجموع المشاهدات",
        title_standoff=35,
        showgrid=True,
        gridcolor="lightgrey",
        linecolor="black",
        title_font=dict(size=14, family="Arial", weight="bold"),
        tickfont=dict(size=12, family="Arial", weight="bold")
    ),
    legend=dict(
        font=dict(size=12),
        orientation="h",
        x=0.5, y=1, xanchor="center", yanchor="bottom"
    ),
    width=730,
    height=500
)


# Display the figure
st.plotly_chart(fig)
st.markdown("<hr>",unsafe_allow_html=True)



















# df_yearly = df_clean.groupby('category')["2024_views"].sum().reset_index()


# df_top5 = df_yearly.sort_values(by="2024_views", ascending=False).head(5)
# youtube_colors = ['#FF0000', '#282828', '#FFFFFF', '#D3D3D3', '#696969']

# fig = px.pie(
#     df_top5, 
#     names='category', 
#     values="2024_views", 
#     title=f'أعلى 5 تصنيفات مشاهدة في السنة 2024', 
#     labels={'category': 'التصنيفات', "2024_views": 'مجموع المشاهدات'}, 
#     hole=0.3,  # تحويله إلى دونت شارت (اختياري)
#     width=650,
#     height=650,
#     color_discrete_sequence=youtube_colors
# )


# fig.update_traces(
#     textposition="inside", 
#     textinfo="percent+label",  # عرض النسبة مع التسمية
#     marker=dict(line=dict(color='white', width=2))  # خطوط بيضاء تفصل بين القطاعات
# )


# fig.update_layout(
#     title=dict(
#         text=f"أعلى 5 تصنيفات مشاهدة في السنة 2024",
#         font=dict(size=20),
#         x=0.309  # جعل العنوان في المنتصف
#     ),
#     legend=dict(
#         title="التصنيفات",
#         orientation="h", 
#         x=0.5, y=-0.1, xanchor="center", yanchor="top"
#     )
# )

# fig
st.markdown("""
        <p style="font-size: 28px; text-align: right;"> وقف وقف شوي خلنا نرجع للحاضر 
 </p>
    """, unsafe_allow_html=True)

st.markdown("""
           على نفسه اي فرد بيفتح قناة بيكون يعتمد على نفسه او شركه  في صناعة المحتوى من الشركات الي داخله مجال اليوتيوب مثل روتانا في الاغاني و روتانا خليجيه في مسلسلات الخليجيه.  هل هذا الشي يمنعك انك تدخل كفرد في اليوتيوب؟ لا, عندك اكبر مثال بندريتا معتمد على نفسه  
""",unsafe_allow_html=True)

top_10 = df_clean.sort_values(by="2024_views",ascending=False).head(10)
top_10 = top_10.sort_values(by="2024_views", ascending=False)
top_10.loc[164,"profile_name"] = "مسلسل الطائر المبكر"
fig = px.bar(
    top_10,
    x="profile_name",  # Replace with the column identifying the row
    y="2024_views",
    #title=f" {option} الاعلى مشاهدات خلال سنه ",
    text=['{:.4}B'.format(x / 1000000000) for x in top_10[f"2024_views"]],
    height=500,
    width=730,
    #labels={"item": "Items", "2024_views": "Views"}, # Display values on the bars
)

# Update layout for better visuals
fig.update_traces(textposition="outside",   
                  marker_color="red"
)
fig.update_layout(

    xaxis=dict(title="القنوات",title_standoff=40,title_font=dict(weight="bold")),  # عكس المحور الأفقي
    
    yaxis=dict(title="عدد المشاهدات",title_standoff=20,title_font=dict(weight="bold")),
    #showlegend=False,

)

# Show the plot
fig
st.markdown("<hr>",unsafe_allow_html=True)


# top_10_sub = df_clean.sort_values(by=f"2024_subscribers", ascending=False).head(10)
# fig = px.bar(
#     top_10_sub,
#     x="profile_name",  # Replace with the column identifying the row
#     y=f"2024_subscribers",
#     #title="الاعلى نموا خلال سنه 2024",
#     text=['{:.4}M'.format(x / 1000000) for x in top_10_sub[f"2024_subscribers"]],
#     height=500,
#     width=730,
#     #labels={"item": "Items", "2024_views": "Views"}, # Display values on the bars
# )

# # Update layout for better visuals
# fig.update_traces(textposition="outside",   
#                   marker_color="red"
# )
# fig.update_layout(
#     xaxis=dict(title="القنوات",title_standoff=5,title_font=dict(weight="bold")),  # عكس المحور الأفقي
    
#     yaxis=dict(title="عدد الاشتراكات",title_standoff=20,title_font=dict(weight="bold")),
#     showlegend=False,
# )

# # Show the plot
# fig

st.markdown("""
    <p style="font-size: 30px; text-align: right;">رحلة مؤثر</p>
""", unsafe_allow_html=True)
st.image("https://images-ext-1.discordapp.net/external/4w6mptaeC4pU8QiLFbTE2eANlGg4Oxe4QMcedJ_COAo/https/yt3.googleusercontent.com/bxmZuQYwJy5wVAYsT_s9TTQoFymSSyqpgLV8JeilUtpCgqreES-QGLtWvKW4JK3nGX8wXSufog%3Dw1707-fcrop64%3D1%2C00005a57ffffa5a8-k-c0xffffffff-no-nd-rj?format=webp&width=1440&height=238",width=650)

df_bandr = df_clean[df_clean['profile_name'] == "Banderita X"]
col11,col22,col33,col44= st.columns(4,gap="small")
# sub2023 = df_bandr['subscriber'].to_numpy()[0] - df_bandr['2024_subscribers'].to_numpy()[0]

# col11.metric("مجموع المشاهدات", f"{df_bandr['view'].iloc[0] / 1e9:.2f}B",)
col11.metric("ربح الشهري ", f"{df_bandr['min_month_earnings'].iloc[0] / 1e3:.2f}k$",)

col22.metric("إجمالي المشتركين", f"{df_bandr['subscriber'].iloc[0] / 1e6:.2f}M")
col33.metric("تاريخ انشاء القناة", f"{df_bandr['since'].iloc[0]}")
col44.metric("التصنيف", f"{df_bandr['category'].iloc[0]}")

st.markdown("""
            بندريتا من أكثر صناع المحتوى اللي كسب محبت الصغار والكبار. بدا قبل 2016 بس الاحصائيات المجمعه بين 2016-2024 فقط، لكن شهرته الحقيقية طلعت بين 2018 و2019، خصوصًا لما ألعاب مثل فورتنايت انتشرت وصارت تضيف له مشاهدات ضخمة.

في 2021، كان في القمة بعد ما دخل مع فالكون، وهذا زاد شعبيته ورفع أرقامه بشكل كبير. بس، في 2022، واجه مشاكل صحية أثرت عليه وعلى عدد الفيديوهات اللي ينزلها، فالمشاهدات نزلت شوي.

حاليا، بندريتا راجع بقوة وبادي يصعد من جديد 💪
            
            """)
mycolumns = df_clean.columns[12:21]
result = pd.DataFrame({
    "Year": mycolumns,  # Years as the column headers
    "Total": df_bandr[mycolumns].sum(axis=0)  # Sum across rows (axis=0 means columns)
})
result["Year"]= result["Year"].str.replace("_views", "")
result["Year"] = pd.to_datetime(result["Year"],format="%Y").dt.year
fig = px.line(
    result, 
    x="Year", 
    y="Total", 
    text=['{:.4}B'.format(x / 1000000000) for x in result['Total']],
    markers=True, height=500,width=730
)
fig.update_traces(
    textposition="top center", 
    line=dict(width=3),
    line_color="red",
    marker=dict(size=10, color="red", line=dict(width=2, color="red")),
)
fig.update_layout(
    xaxis=dict(
        tickmode="linear", 
        title=dict(
            text="السنوات",  
            font=dict(size=15, family="Arial", weight="bold")  
        ),
        linecolor='white',  
        #tickfont=dict(color="black"), 
        showgrid=False, 
        gridcolor="lightgrey",

    ),
    yaxis=dict(
        title=dict(
            text="مجموع المشاهدات",  
            font=dict(size=15, family="Arial", weight="bold")  
        ),  # Y-axis title in Arabic
        showgrid=True,  # Show gridlines
        gridcolor="lightgrey",  # Set gridline color
        #tickfont=dict(color="black"),
        #standoff=20)
    ),  # تحديد المسافات حول الرسم
    #borderwidth=2, 
    #bordercolor="white"
    #plot_bgcolor="#282828",  # Dark background for the plot
    #paper_bgcolor="#282828",# Dark background for the entire paper
)
fig

def get_profile_views(df, profile_name):
    profile_data = df[df['profile_name'] == profile_name]
    return profile_data[['2016_views', '2017_views', '2018_views', '2019_views', 
                         '2020_views', '2021_views', '2022_views', '2023_views', '2024_views']].to_numpy()[0]

# Extract views for each profile
profiles = ['25esports', 'Powr E Sports | باور', 'Falcons', 'Peaks']
views_data = {profile: get_profile_views(df_clean, profile) for profile in profiles}

# Prepare data for plotting
dfx = pd.DataFrame({
    'Year': ['2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024'],
    **views_data  # Unpack dictionary into DataFrame columns
})

# Define color palette for the lines
colors = {
    '25esports': 'yellow',
    'Powr E Sports | باور': 'red',
    'Falcons': 'green',
    'Peaks': 'skyblue'
}

# Create figure
fig = go.Figure()
st.markdown("<hr>",unsafe_allow_html=True)

# Add each profile's line to the plot
st.markdown("""
    <p style="font-size: 30px; text-align: right;">جاهز للترند الجديد في يوتيوب ؟</p>
""", unsafe_allow_html=True)
st.markdown(""" في اخر سنتين ظهر ترند يسمى بالكلانات او المنظمات بكل بساطه فكرته ان اكثر من صانع محتوى يجتمعون ويبدوا منظمة بحيث ينتجون المحتوى سوا
            و بأسلوب احترافي واعلى درجه من كتابة المحتوى ,تسويق وحتى الرعايات ففي اخر سنتين تقريبا لاحظنا كيف ان اشهر منظمتين في السعودية حققوا نجاحات بشكل سريع 
            وتمكنوا باور و فالكونز من المشاركة في فعاليات موسم القيمرز الى شراكات مع شركات كبيره في السوق , فهل هذا هو الترند الجديد باليوتيوب ؟""")

for profile in profiles:
    fig.add_trace(go.Scatter(x=dfx['Year'], y=dfx[profile], mode='lines', name=profile, 
                             line=dict(color=colors[profile])))

# Update layout for clarity
fig.update_layout(


    xaxis=dict(
        title="السنوات",
        title_font=dict(size=14, family="Arial", weight="bold"),
        tickfont=dict(size=12, family="Arial"),
        linecolor="black",
        showgrid=False,
        gridcolor="lightgrey"
        
    ),
    yaxis=dict(
        title="مجموع المشاهدات",
        title_font=dict(size=14, family="Arial", weight="bold"),
        tickfont=dict(size=12, family="Arial"),
        linecolor="black",
        showgrid=True,
        gridcolor="lightgrey",
        title_standoff=40
    ),
    width=730,  # Width of the chart
    height=500,  # Height of the chart
    legend=dict(
        title="المنظمات",
        font=dict(size=12),
        orientation="h",  # Place legend horizontally
        x=0.5, y=-0.15, xanchor="center", yanchor="top"
    )
)

# Show figure
fig