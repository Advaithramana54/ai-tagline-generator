import streamlit as st
from groq import Groq

# 1. Page Configuration
st.set_page_config(page_title="AI Tagline Generator", layout="centered")
st.title("🚀 Custom Indian Business Tagline Generator")
st.write("Enter your business details below to generate a marketing tagline instantly using Llama 3.")

# 2. Setup Client
client = Groq(api_key="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")


# 3. User Inputs
business_name = st.text_input("Business Name", placeholder="e.g., Chai Point")
business_type = st.text_input("What do you sell / do?", placeholder="e.g., Premium Masala Chai and snacks")

# 4. Action Button
if st.button("Generate Taglines ✨"):
    if business_name and business_type:
        with st.spinner("AI is thinking..."):
            completion = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "user",
                        "content": f"Write 3 punchy marketing taglines for a business named '{business_name}' that does: {business_type}."
                    }
                ],
                temperature=0.7,
            )
            
            st.success("Here are your custom taglines:")
            st.write(completion.choices[0].message.content)
    else:
        st.warning("Please fill out both fields first!")
