import streamlit as st
import base64
from PIL import Image
import io

# 페이지 설정
st.set_page_config(page_title="구글 스타일 포털", layout="centered")

# CSS 스타일
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700&display=swap');
    
    body {
        font-family: 'Noto Sans KR', sans-serif;
        background: linear-gradient(135deg, #4285f4, #34a853, #fbbc05);
        height: 100vh;
        margin: 0;
        background-attachment: fixed;
    }
    .stApp {
        background: none;
    }
    .logo {
        font-size: 72px;
        font-weight: bold;
        color: white;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        text-align: center;
        margin-bottom: 20px;
        animation: float 3s ease-in-out infinite;
    }
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }
    .welcome-message {
        font-size: 24px;
        color: white;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
        text-align: center;
        margin-bottom: 30px;
        animation: fadeIn 1.5s ease-out forwards;
    }
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    .stButton>button {
        background-color: #4285f4;
        color: white;
        border: none;
        border-radius: 24px;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #3367d6;
    }
    .stTextInput>div>div>input {
        border-radius: 24px;
    }
</style>
""", unsafe_allow_html=True)

# 로고
st.markdown('<p class="logo">구글</p>', unsafe_allow_html=True)

# 환영 메시지
st.markdown('<p class="welcome-message">환영합니다!</p>', unsafe_allow_html=True)

# 검색 기능
search_term = st.text_input("", placeholder="검색어를 입력하세요")

# JavaScript 함수 정의
js_code = """
<script>
function performSearch() {
    var searchTerm = document.getElementById('searchInput').value;
    if (searchTerm) {
        var searchUrl = "https://www.google.com/search?q=" + encodeURIComponent(searchTerm);
        window.open(searchUrl, '_blank');
    } else {
        alert("검색어를 입력해주세요.");
    }
}
</script>
"""

# 검색 버튼과 JavaScript 실행
if st.button("검색"):
    st.components.v1.html(js_code + f"""
    <script>
    var searchTerm = "{search_term}";
    if (searchTerm) {{
        var searchUrl = "https://www.google.com/search?q=" + encodeURIComponent(searchTerm);
        window.open(searchUrl, '_blank');
    }} else {{
        alert("검색어를 입력해주세요.");
    }}
    </script>
    """, height=0)

# 배경 애니메이션 (SVG 대신 간단한 이미지로 대체)
def create_gradient_image():
    width, height = 400, 300
    image = Image.new('RGB', (width, height))
    for x in range(width):
        for y in range(height):
            r = int(255 * (1 - x / width) * (1 - y / height))
            g = int(255 * (x / width) * (1 - y / height))
            b = int(255 * (y / height))
            image.putpixel((x, y), (r, g, b))
    return image

gradient_img = create_gradient_image()
img_byte_arr = io.BytesIO()
gradient_img.save(img_byte_arr, format='PNG')
img_byte_arr = img_byte_arr.getvalue()

data_url = base64.b64encode(img_byte_arr).decode()

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{data_url}");
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
)
