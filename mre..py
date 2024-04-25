import pickle
import streamlit as st
import requests
from streamlit_option_menu import option_menu
from dotenv import load_dotenv
load_dotenv()  # Loading all the environment variables
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro model
# model = genai.GenerativeModel("gemini-pro", "gemini-pro-vision")
model_pro = genai.GenerativeModel("gemini-pro")
model_vision = genai.GenerativeModel("gemini-pro-vision")

# Define custom CSS styles
custom_css = """
<style>

/* Add your custom CSS styles here */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    color: #333;
    margin: 0;
    padding: 0;
}

h1 {
    color: orange;
    border-bottom: 2px solid orange;
    padding-bottom: 5px;
    text-align: center; /* Center-align h1 headings */
}

h2 {
    color: grey; /* Change to grey color */
}

h3 {
    color: #007bff;
}

.container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
    background-color: #fff;
}

.movie-container {
    margin-bottom: 20px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    background-color: #f9f9f9;
}

.movie-title {
    font-size: 20px;
    margin-bottom: 10px;
}

.movie-poster {
    width: 100%;
    height: auto;
    border-radius: 5px;
}

.movie-rating {
    margin-top: 10px;
}

.movie-feedback {
    margin-top: 10px;
}

.sidebar .Select__single-value {
    color: #007bff; /* Color for selected sidebar item */
}

.sidebar. Select__indicator {
    color: #007bff; /* Color for dropdown indicator */
}

.sidebar .Select__indicator:hover {
    color: #0056b3; /* Color for dropdown indicator on hover */
}

.sidebar .Select__indicator:active{
    color:#004080; /* Color of dropdown indicator when clicked */
}

/* Add hover effect to movie containers */
.movie-container:hover {
    box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
}

/* Custom CSS for the Get Recommendations page */

/* Center-align the title */
h1 {
    text-align: center;
    color: orange;
    border-bottom: 2px solid orange;
    padding-bottom: 5px;
}

/* Style the dropdown */
.stSelectbox {
    width: 100%;
    padding: 8px;
    border-radius: 5px;
    border: 1px solid #ccc;
}

/* Style the button */
.stButton {
    background-color: black; 
    color: white;
    border-radius: 5px;
    padding: 10px 20px;
    display: block; 
    margin: 0 auto; /* Center align horizontally */

}

/* Add hover effect to the button */
.stButton:hover {
    background-color: #d3d3d3; /* lighter shades of grey */
}

/* Style the recommendation columns */
.recommendation-column {
    padding: 20px;
}

/* Style the movie title */
.movie-title {
    font-size: 18px;
    font-weight: bold;
    margin-bottom: 5px;
}

/* Style the movie image */
.movie-image {
    width: 100%;
    border-radius: 5px;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
    margin-bottom: 10px;
}

/* Style the movie title */
.movie-title {
    font-size: 18px;
    font-weight: bold;
    margin-bottom: 5px;
}

/* Style the movie description */
.movie-description {
    font-size: 16px;
    margin-bottom: 10px;
}

/* Add margin between recommendations */
.movie-recommendation {
    margin-bottom: 20px;
}

/* CSS for spiderman.jpg */
.spiderman-image {
    max-width: 200px; /* Adjust the max-width to make the image smaller */
    width: 100%; /* Ensure the image retains its aspect ratio */
    border-radius: 10px;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);
}

</style>

"""

# Inject custom CSS
st.markdown(custom_css, unsafe_allow_html=True)


#1
with st.sidebar:
    selected = option_menu(
        menu_title ="RYF",
        options = ["RFY-Recommend For You", "About", "Movie Information","Movie Poster Information", "Get Recommendation", "Future Scope", "Contact Us"]
    )

if selected=="RFY-Recommend For You":
    st.title(f"{selected}")

    # st.image("fifty-shades-darker-2017-movie-4k-4k.jpg", caption="Recommended Movie", use_column_width=True)
    #     # Apply CSS to the image
    # st.markdown("<style>img { border-radius: 10px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5); }</style>", unsafe_allow_html=True)
    # st.image("recommender-system-for-movie-recommendation.jpg")

     # Apply CSS styling to the text
    st.markdown("""
        <div style='text-align: center; padding: 20px;'>
            <h3 style='color: #007bff; font-weight: bold;'>Discover your next favorite movie!</h3>
            <p style='font-size: 18px;'>Get personalized recommendations based on your preferences.</p>
        </div>
    """, unsafe_allow_html=True)

    st.image("Camera.jpg")
    st.markdown("<style>img { border-radius: 10px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5); }</style>", unsafe_allow_html=True)
            


if selected=="About":
    # st.title(f" {selected}")
    # st.header("About Recommendation Systems")
    st.title("About Recommendation Systems")

    st.markdown("""
    In the fast-evolving landscape of digital commerce, Recommendation Systems have become indispensable tools that elevate user experience and drive business success. A Recommendation System is a sophisticated software application or algorithm meticulously designed to deliver personalized suggestions, offering users a curated selection of items tailored to their preferences and needs.

    Diversifying into different methodologies, recommendation systems contribute significantly to user engagement and satisfaction. Key types include:

    - **Content-based Recommendation Systems:** Leveraging intricate analyses of item characteristics such as genre, actors, and plot, these systems suggest items with similar features to the user.

    - **Collaborative Filtering Systems:** Capitalizing on user behavior and preferences, these systems generate recommendations based on the collective wisdom of the user community.

    - **Hybrid Approaches:** Merging the strengths of both content-based and collaborative filtering techniques, hybrid recommendation systems provide nuanced and accurate suggestions.

    Across industries such as e-commerce, entertainment, social media, and advertising, recommendation systems play a pivotal role in enhancing user engagement, boosting sales, and fostering user satisfaction.

    **Our Product:**
    In our context, we specialize in content-based recommendation systems tailored for the dynamic landscape of the entertainment industry. Focused on movies, our product meticulously analyzes the intricate features of each film – from genre to actors and plot – to provide users with personalized and relevant recommendations.

    While content-based systems excel in certain areas, they do come with limitations. Our approach acknowledges the dynamic nature of user preferences and addresses these limitations through hybrid recommendation systems. By combining the strengths of both content-based and collaborative filtering approaches, we strive to offer a comprehensive and tailored recommendation experience that transcends the confines of individual user preferences.

    As the industry continues to evolve, so do our recommendation systems, ensuring that users receive not just what they want, but what they didn't even know they needed.
    """)


if selected == "Movie Information":
    st.title("Movie Information")
    def get_gimini_response(question):
        response = model_pro.generate_content(question)
        return response.text

# ## Initialize Our Streamlit Application
# st.set_page_config(page_title="Q and A Demo")
# st.header("Gemini LLM Application")

    input_text = st.text_input("Input:", key="input")
    submit = st.button("Ask me any question related to movies")
    ## When submit is clicked
    if submit:
        response = get_gimini_response(input_text)
        st.subheader("The Response is")
        st.write(response)


if selected == "Movie Poster Information":
    st.title("Get Information About the Movie Poster")
    def get_gimini_response(image):
        response = model_vision.generate_content(image)
        return response.text

    # input_text = st.text_input("Input:", key="input")

    uploaded_file = st.file_uploader("Choose a image...", type=["jpg", "jpeg", "png"])
    image = ""
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

    submit = st.button("Tell me about the Movie Poster")

    # If submit is clicked 
    if submit:
        response = get_gimini_response(image)
        st.subheader("The Response is: ")
        st.write(response)




if selected=="Get Recommendation":
    def fetch_poster(movie_id):
        url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(
            movie_id)
        data = requests.get(url)
        data = data.json()
        poster_path = data['poster_path']
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
        return full_path


    def recommend(movie):
        index = movies[movies['title'] == movie].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        recommended_movie_names = []
        recommended_movie_posters = []
        for i in distances[1:6]:
            # fetch the movie poster
            movie_id = movies.iloc[i[0]].movie_id
            recommended_movie_posters.append(fetch_poster(movie_id))
            recommended_movie_names.append(movies.iloc[i[0]].title)

        return recommended_movie_names, recommended_movie_posters


    st.markdown("<h1 style='font-family: Arial, sans-serif; color: orange;'>Get Recommendations</h1>", unsafe_allow_html=True)
    # st.image("fifty-shades-darker-2017-movie-4k-4k.jpg")
    # st.image("fifty-shades-darker-2017-movie-4k-4k.jpg", use_column_width=True)
    st.image("spiderman.jpg", use_column_width=True)

    # Apply CSS to the image
    # st.markdown("<style>img { border-radius: 10px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5); }</style>", unsafe_allow_html=True)
    movies = pickle.load(open('movie_list.pkl', 'rb'))
    similarity = pickle.load(open('similarity.pkl', 'rb'))

    movie_list = movies['title'].values
    selected_movie = st.selectbox(
        "Type or select a movie from the dropdown",
        movie_list
    )

    if st.button('Show Recommendation'):
        recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.text(recommended_movie_names[0])
            st.image(recommended_movie_posters[0])
        with col2:
            st.text(recommended_movie_names[1])
            st.image(recommended_movie_posters[1])

        with col3:
            st.text(recommended_movie_names[2])
            st.image(recommended_movie_posters[2])
        with col4:
            st.text(recommended_movie_names[3])
            st.image(recommended_movie_posters[3])
        with col5:
            st.text(recommended_movie_names[4])
            st.image(recommended_movie_posters[4])
        

 # Apply CSS styling to the "Show Recommendation" button
    button_style = """
        <style>
        .button-container {
            text-align: center;
        }
        .stButton>button {
            padding: 10px 20px;
            background-color: #007bff;
            color: white;
            border-radius: 5px;
            text-decoration: none;
        }
        .stButton>button:hover {
            background-color: #0056b3;
        }
        </style>
    """
    st.markdown(button_style, unsafe_allow_html=True)

    

if selected=="Future Scope":
    st.title(f"{selected}")
    # st.header("Future Scope for Recommender Systems")

    st.markdown("""
    The future scope for recommender systems is vast and exciting, as these systems continue to evolve and improve, driven by advances in artificial intelligence and machine learning. Here are some potential areas for growth and development in the field of recommender systems:

    1. **Personalization:** Recommender systems will become even more personalized, taking into account not only a user's past behavior but also their current context, preferences, and goals.

    2. **Explainability:** There will be a greater emphasis on explainability and transparency in recommender systems, allowing users to understand how recommendations are generated and why they are relevant.

    3. **Multi-modal recommendations:** Recommender systems will incorporate multiple types of data, including images, videos, and audio, to provide more diverse and engaging recommendations.

    4. **Cross-domain recommendations:** Recommender systems will extend beyond a single domain and provide recommendations across different domains, such as books, movies, and music.

    5. **Group recommendations:** Recommender systems will provide group recommendations that take into account the preferences and needs of multiple users, such as families or teams.

    6. **Reinforcement learning:** Reinforcement learning algorithms will be used to optimize recommendations over time, allowing the system to adapt and improve based on user feedback.
    """)



if selected=="Contact Us":
    st.title(f"{selected}")

    # st.markdown("<span style='font-family: Arial, sans-serif; color: #007bff;'>SANIDHYA RAJGURU</span> 😊", unsafe_allow_html=True)
    # st.markdown("<span style='font-family: Arial, sans-serif; color: #007bff;'>LAKSHYARAJ SINGH RATHORE</span> 😎", unsafe_allow_html=True)
    # st.title("Contact Us")

    # st.write("""
    # Have questions, feedback, or suggestions? We'd love to hear from you! Reach out to us via the following channels:

    # - **Email:** support@example.com
    # - **Phone:** +1 (123) 456-7890
    # - **Social Media:** Follow us on [Twitter](https://twitter.com/example) and [Facebook](https://www.facebook.com/example) for updates and announcements.
    # """)

    # Display contact information
    st.write("""
       Have questions, feedback, or suggestions? We'd love to hear from you! Reach out to us via the following channels:

    - **Email:** support@example.com
    - **Phone:** +1 (123) 456-7890
    - **Social Media:** Follow us on [Twitter](https://twitter.com/example) and [Facebook](https://www.facebook.com/example) for updates and announcements
\
    """)

            # Add a button-like link to give feedback
    # if st.button("Click here to Give Feedback"):
    #     st.markdown("[Click here to Give Feedback](https://forms.gle/Ny3ZeQKzztKQhtui6)")

        # Add a button-like link to give feedback
    st.markdown("""
    <div style="text-align:center;">
        <button style="padding: 10px 20px; background-color: #007bff; color: white; border-radius: 5px;">
            <a href="https://forms.gle/Ny3ZeQKzztKQhtui6" style="text-decoration:none; color:white;">Click here to Give Feedback</a>
        </button>
    </div>
    """, unsafe_allow_html=True)







