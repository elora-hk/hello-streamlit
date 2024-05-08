# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
import time
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

def generate_story(parent_input):
  story = """

# The Sweetest Surprise
> A colorful candy shop overflowing with lollipops, gummies, and chocolates, with a bright pink and white striped awning and a sign that reads "Mrs. Sweet's Candy Kingdom".

In the heart of the Candy Kingdom, Mrs. Sweet's shop was famous for its endless varieties of sweets. One day, a curious little rabbit named Rosie hopped into the shop, her eyes wide with wonder. She had never seen so many candies in her life!

> Rosie, a little rabbit with fluffy white ears and a twitching nose, standing in front of a towering shelf of jars filled with colorful candies, her paws grasping a small basket.

As she wandered down the aisles, Rosie's basket began to fill with all sorts of treats. There were gummy bears, sour candies, and chocolates shaped like animals. But as she reached for a particularly tantalizing lollipop, the shop's shelves began to shake and rattle.

> The candy shop's shelves, once neatly stacked, now overflowing with candies spilling onto the floor, with Rosie looking up in surprise as Mrs. Sweet rushes to grab a broom.

Mrs. Sweet, the kind shop owner, rushed to Rosie's side. "Oh dear, it seems we have a bit of a sweet situation on our hands!" she exclaimed. Together, they worked to clean up the mess, but not before Rosie learned a valuable lesson about moderation and the importance of sharing.

> Rosie and Mrs. Sweet, surrounded by the cleaned-up shop, sitting at a small table with a plate of candies and a sign that reads "Sharing is Caring".

### Questions
1. What happened when Rosie took too many candies from the shelves?
2. What did Rosie learn from her adventure in the Candy Kingdom?
3. What is the name of the kind shop owner who helped Rosie clean up the mess?
"""
  for char in story:
    time.sleep(0.01)
    yield(char)

def run():
    st.set_page_config(page_title="✨ Dreamweaver - Bedtime Stories for Kids ✨", page_icon=":crescent_moon:")
    st.title("✨ Dreamweaver ✨")
    st.markdown("""
🌙 Create enchanting bedtime stories to delight your little ones! 👨‍👩‍👧‍👦
📚 Unleash your imagination and craft personalized tales that will send your kids off to sweet dreams. 💤
""")

    # Add an input field for the parent's initial story idea
    parent_input = st.text_input("🌟 Enter your initial story idea for your child:")

    # Display the parent's input
    if parent_input:      
      st.write_stream(generate_story(parent_input))

if __name__ == "__main__":
    run()
