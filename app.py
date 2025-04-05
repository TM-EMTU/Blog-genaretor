import streamlit as st
from google import genai
import os
from dotenv import load_dotenv

# Must be the first Streamlit command
st.set_page_config(
    layout="wide",
    page_title="AI Blog Generator",
    page_icon="📝",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    /* Main container styling */
    .stApp {
        background-color: var(--background-color);
        color: var(--text-color);
        font-family: 'Helvetica Neue', Arial, sans-serif;
    }
    
    /* Header styling */
    .stHeader {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        color: white;
        text-align: center;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background-color: var(--background-color);
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    /* Sidebar title styling */
    .sidebar-title {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    
    /* Sidebar sections */
    .sidebar-section {
        background: rgba(102, 126, 234, 0.05);
        padding: 15px;
        border-radius: 8px;
        margin: 10px 0;
    }
    
    /* Sidebar links */
    .sidebar-link {
        color: #667eea;
        text-decoration: none;
        transition: color 0.3s ease;
    }
    
    .sidebar-link:hover {
        color: #764ba2;
    }
    
    /* Disclaimer box */
    .sidebar-disclaimer {
        background: rgba(255, 152, 0, 0.1);
        border-left: 4px solid #ff9800;
        padding: 10px;
        margin: 15px 0;
        border-radius: 4px;
    }
    
    /* Input fields styling */
    .stTextInput>div>div>input, .stTextArea>div>textarea {
        border-radius: 5px;
        border: 1px solid #e0e0e0;
        padding: 10px;
        background-color: var(--background-color);
        color: var(--text-color);
    }
    
    /* Button styling */
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 25px;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    
    /* Generated blog styling */
    .generated-blog {
        background: var(--background-color);
        color: var(--text-color);
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        line-height: 1.6;
        margin-top: 1rem;
    }
    
    /* Slider styling */
    .stSlider {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    
    /* Dark blog container styling */
    .dark-blog-container {
        background-color: #1E1E1E;
        color: #E0E0E0;
        padding: 2.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        margin: 2rem 0;
        font-family: 'Helvetica Neue', Arial, sans-serif;
        line-height: 1.8;
    }
    
    .dark-blog-container h1, 
    .dark-blog-container h2, 
    .dark-blog-container h3 {
        color: #667eea;
        margin-bottom: 1rem;
    }
    
    .dark-blog-container p {
        margin-bottom: 1.2rem;
    }
</style>
""", unsafe_allow_html=True)

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if api_key is None:
    raise ValueError("GEMINI_API_KEY not found in environment variables.")

client = genai.Client(api_key=api_key)


#header

st.header("📝✍️Write your blog with AI with a Human accent")
st.markdown('</div>', unsafe_allow_html=True)

#sider bar for user input
with st.sidebar:
    st.markdown('<h1 class="sidebar-title">✨ Create Your Blog</h1>', unsafe_allow_html=True)
    
    with st.container():
        blog_title = st.text_input("🎯 Blog Title", placeholder="Enter an engaging title...")
        keyword = st.text_area("🔑 Keywords", placeholder="Enter relevant keywords separated by commas...")
        size = st.slider("📝 Word Count", min_value=100, max_value=1000, value=300, step=50)
        submit = st.button("✨ Generate Magic!")
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.divider()
    
    # About section
    st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
    st.markdown("### 🤖 About AI Blog Generator")
    st.markdown("""
    Transform your ideas into engaging blog posts with the power of Google Gemini AI. 
    Perfect for content creators, bloggers, and writers looking for inspiration.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Disclaimer
    st.markdown('<div class="sidebar-disclaimer">', unsafe_allow_html=True)
    st.markdown("### ⚠️ Disclaimer")
    st.markdown("""
    The generated content is AI-assisted and should be reviewed for:
    - Accuracy
    - Relevance
    - Factual correctness
    - Personal touch
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Contact & Author
    st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
    st.markdown("### 📫 Connect With Us")
    st.markdown("""
    - 📧 [Email](mailto:emtu561@gmail.com)
    - 💻 [GitHub](https://github.com/TM-EMTU/)
    - 🌐 [Portfolio](https:Notfound802322222.com)
    """)
    st.markdown("### 👨‍💻 Created By")
    st.markdown("""
    **Tanjil Mahmud Emtu**  
    *Ai Enthusiast & Devoloper*
    """)
    st.markdown('</div>', unsafe_allow_html=True)

if submit:
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=["""Write a blog in human tone about {} with the keyword {}. Format it in Markdown with:
        - Title in **bold** at the top
        - Important points and key concepts in **bold**
        - A length of approximately {} words
        - Natural paragraph breaks
        Begin with '# **{title}**' and make sure to emphasize key ideas by wrapping them in **asterisks**.""".format(blog_title, keyword, size, title=blog_title)],
    )
    # Display the response in the Streamlit app
    st.subheader("Generated Blog: ")
    st.markdown(f'<div class="dark-blog-container">{response.text}</div>', unsafe_allow_html=True)
