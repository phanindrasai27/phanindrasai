import streamlit as st
from PIL import Image
import base64

with open("style.css") as f:
  st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

st.write('''# Phanindra Sai,    Integrated M.Tceh in specialization of Business Analytics.
#### *Resume*
''')

image_path = "Arty_me.png"
st.image(image_path, width=250)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Recently graduated from vellore institute of technology, chennai with integrated M.tech with specialization in Business analytics.
- Strong problem solving skills, flexible with varies Jobroles.
- Versatile AI enthusiast, Passionate about data science & ML, looking for exciting technical jobroles.
''')


st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="" target="_blank">Phanindra Sai</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#Projects">Projects</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Education
''')

txt('**Vellore Institute of Technology, Chennai',
'2019-2024')
st.markdown('''
- GPA: `7.90`
- Graduated with M.Tech Integrated degree in specilization of Business Analytics.
''')

txt('**Narayana junior college, vijayawada',
'2017-2019')
st.markdown('''
- GPA: `9.44`
- completed my Higher School`.
''')

txt('**Viswabharthi school, gudiwada andhrapradesh',
'2016-2017')
st.markdown('''
- GPA: `9.8`
- Completed my Junior School.
''')


st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `R`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`, `altair`, `ggplot2`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Deep Learning', '`TensorFlow`')
txt3('Web development', '`Flask`, `HTML`, `CSS`')
txt3('Model deployment', '`streamlit`, `gradio`,`Heroku`, `AWS`')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/phanindra-sai-886ba0190/')
txt2('EmailId', 'bollarapuphanindra1375645@gmail.com')
txt2('GitHub', 'https://github.com/phanindrasai27')

st.markdown('''
## Projects
''')
txt2('amazon-food-recommendation-system', 'https://github.com/phanindrasai27/Amazon-food-recommendation-system')
txt2('fake-news-analysis-prediction', 'https://github.com/phanindrasai27/fake-news-analysis')
txt2('comment-toxicity-prediction', 'https://github.com/phanindrasai27/comment_toxicity_prediction')
txt2('pneumonia-and-covid-detction-using-x-rays', 'https://github.com/phanindrasai27/pneumonia-and-covid-detction-using-x-rays')
