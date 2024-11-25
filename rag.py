import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go


df_clean = pd.read_csv("youtube_data_full_clean.csv")


st.markdown("""
    <style>
        body {
            direction: rtl;
            text-align: right;
        }
        .streamlit-expanderHeader {
            text-align: right;
        }
        .stTextInput>div>div>input {
            text-align: right;
        }
        h1{
            text-align: center;
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
    </style>
""", unsafe_allow_html=True)
st.title("رائج")
st.markdown("مبدع؟مؤثر؟ وش تنتظر افتح لك قناه بس انتظر شوي خلنا نوضح لك الصوره تخيل ان يوتيوب فيه اكثر من ٢.٥ مليار  مشاهد نشط ادري جالس تحسب الارباح لكن لا تطمع فينا خطوه بخطوه و رائج جاي يوضح لك الصوره 😉",unsafe_allow_html=True)
st.markdown("""خلنا نبدا الرحله من عام 2016 لاحظ معنا كيف المشاهدات جالسه ترتفع بشكل مهول الى عام 2021 ولكن في عام 2022 انخفضت المشاهدت بسبب انتهاء
            جائحة كورونا ورجع ارتفع خلال فتره 2023 وبس في 2024 حصل نزول والسبب اننا لم ندخل اخر شهرين في الحسبه فهل راح تتجازو السنة الي قبلها؟🤔""")
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
    markers=True, height=600,width=1000
)
fig.update_traces(
    textposition="top center", 
    line=dict(width=3),
    line_color="red",
    marker=dict(size=10, color="red", line=dict(width=2, color="red")),
)
fig.update_layout(
    title=dict(text="مجموع المشاهدات لكل سنه ", font=dict(size=20,weight="bold"),x= 0.4),
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
fig


a = df_clean[['category', '2016_views', '2017_views', '2018_views', '2019_views', '2020_views', '2021_views', '2022_views', '2023_views', '2024_views']]

a = a.groupby(['category']).sum()

co = a[a.index == 'Comedy'].to_numpy()[0]
en = a[a.index == 'Entertainment'].to_numpy()[0]
fa = a[a.index == 'Film & Animation'].to_numpy()[0]
ga = a[a.index == 'Gaming'].to_numpy()[0]
mu = a[a.index == 'Music'].to_numpy()[0]
pb = a[a.index == 'People & Blogs'].to_numpy()[0]
ge = a[a.index == 'general'].to_numpy()[0]

dfaa = pd.DataFrame({
    'Year': ['2016', '2017','2018', '2019', '2020', '2021', '2022','2023', '2024'],
    'Comedy' : co,
    'Entertainment' : en,
    'Film & Animation' : fa,
    'Gaming' : ga,
    'Music' : mu,
    'People & Blogs' : pb,
    'general' : ge
})


# إنشاء الشكل
fig = go.Figure()

# إضافة البيانات كخطوط
categories = {
    'Comedy': co,
    'Entertainment': en,
    'Film & Animation': fa,
    'Gaming': ga,
    'Music': mu,
    'People & Blogs': pb,
}

# استخدام حلقة لإضافة الفئات
for category, data in categories.items():
    fig.add_trace(go.Scatter(
        x=dfaa['Year'], 
        y=data, 
        mode='lines+markers',  # خطوط مع نقاط
        name=category,  # اسم الفئة
        marker=dict(size=8),  # حجم النقاط
        line=dict(width=2)  # عرض الخط
    ))

# تخصيص التصميم
fig.update_layout(
    title=dict(
        text="مجموع المشاهدات حسب التصنيفات عبر السنوات",
        font=dict(size=20),
        x=0.5  # محاذاة العنوان في المنتصف
    ),
    xaxis=dict(
        title="السنوات",
        tickmode="linear",
        showgrid=False,  # إظهار الشبكة
        gridcolor="lightgrey",  # لون الشبكة
        linecolor="black",  # لون خط المحور
        title_font=dict(size=14, family="Arial",weight="bold"),
        tickfont=dict(size=12, family="Arial", weight="bold")
    ),
    yaxis=dict(
        title="مجموع المشاهدات",
        showgrid=True,
        gridcolor="lightgrey",
        linecolor="black",
        title_font=dict(size=14, family="Arial", weight="bold"),
        tickfont=dict(size=12, family="Arial", weight="bold")
    ),
    legend=dict(
        title="التصنيفات",
        font=dict(size=12),
        orientation="h",  # وضع الأسطورة أفقياً
        x=0.5, y=-0.2, xanchor="center", yanchor="top"  # وضع الأسطورة أسفل الرسم
    ),
    #plot_bgcolor="skyblue",  # لون خلفية الرسم
    width=1000,  # عرض الرسم
    height=600   # ارتفاع الرسم
)

fig




df_earing = pd.read_csv("youtube_data_earing.csv")
df_earing.rename(columns={'profile_name': 'اسم القناة', 'min_month_earnings': 'اقل ربح شهري متوقع', 'max_month_earnings': 'اعلى ربح شهري متوقع'},inplace=True)
st.dataframe(df_earing[['اسم القناة','اقل ربح شهري متوقع','اعلى ربح شهري متوقع']],width=800,hide_index=True)













# اختيار السنة
option = st.selectbox(
    "حدد السنة التي ترغب في استعراض البيانات لها:",
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
    width=800,
    height=700,
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




top_10 = df_clean.sort_values(by=f"{option}_views",ascending=False).head(10)

top_10 = top_10.sort_values(by=f"{option}_views", ascending=False)
fig = px.bar(
    top_10,
    x="profile_name",  # Replace with the column identifying the row
    y=f"{option}_views",
    #title=f" {option} الاعلى مشاهدات خلال سنه ",
    text=['{:.4}B'.format(x / 1000000000) for x in top_10[f"{option}_views"]],
    height=700,
    width=1000,
    #labels={"item": "Items", "2024_views": "Views"}, # Display values on the bars
)

# Update layout for better visuals
fig.update_traces(textposition="outside",   
                  marker_color="red"
)
fig.update_layout(
    title=dict(text=f"{option} الاعلى مشاهدات خلال سنه", font=dict(size=20,weight="bold"),x= 0.4),
    xaxis=dict(title="القنوات"),  # عكس المحور الأفقي
    
    yaxis=dict(title="عدد المشاهدات"),
    #showlegend=False,

)

# Show the plot
fig




top_10_sub = df_clean.sort_values(by=f"{option}_subscribers", ascending=False).head(10)
fig = px.bar(
    top_10_sub,
    x="profile_name",  # Replace with the column identifying the row
    y=f"{option}_subscribers",
    #title="الاعلى نموا خلال سنه 2024",
    text=['{:.4}M'.format(x / 1000000) for x in top_10_sub[f"{option}_subscribers"]],
    height=700,
    width=1100,
    #labels={"item": "Items", "2024_views": "Views"}, # Display values on the bars
)

# Update layout for better visuals
fig.update_traces(textposition="outside",   
                  marker_color="red"
)
fig.update_layout(
    title=dict(text=f"{option} الاعلى نموا خلال سنه", font=dict(size=20,weight="bold"),x= 0.4),
    xaxis=dict(title="القنوات"),  # عكس المحور الأفقي
    
    yaxis=dict(title="عدد الاشتراكات"),
    showlegend=False,
)

# Show the plot
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

# Add each profile's line to the plot
for profile in profiles:
    fig.add_trace(go.Scatter(x=dfx['Year'], y=dfx[profile], mode='lines', name=profile, 
                             line=dict(color=colors[profile])))

# Update layout for clarity
fig.update_layout(

    title=dict(text="مجموع المشاهدات لاشهر المنظمات في المملكه العربيه السعوديه", font=dict(size=20,weight="bold"),x= 0.2),

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
        gridcolor="lightgrey"
    ),
    width=1000,  # Width of the chart
    height=800,  # Height of the chart
    legend=dict(
        title="المنظمات",
        font=dict(size=12),
        orientation="h",  # Place legend horizontally
        x=0.5, y=-0.15, xanchor="center", yanchor="top"
    )
)

# Show figure
fig