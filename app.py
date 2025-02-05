import streamlit as st
import requests

'''
# Fake news detector
'''

'''
### Welcome to our app! Here, you will be able to input an article and receive a prediction on whether or not it contains fake information.
'''

'''
##### Team members:
'''

columns = st.columns(4)
columns[0].write('Kathrin Bank')
columns[1].write('Filipe Figueiredo')
columns[2].write('Christopher W.')
columns[3].write('Caspar Zizka')

text = st.text_area('Article', 'Please paste your article here', height=300)

url = 'https://fakenewsdocker-973308060059.europe-west1.run.app/predict'

if st.checkbox('I understand that the following prediction should not be taken into account as definitive proof.'):

    params = {'text': text
            }

    response = requests.get(
        url=url,
        params=params,
    ).json()

    st.write(f"Based on our state-of-the-art algorithm, we predict that this article contains {list(response.values())[0].lower()} information.")
