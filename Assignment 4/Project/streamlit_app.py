#streamlit_app.py
import streamlit as st
import requests

st.title("Business Idea Evaluation")

st.markdown("""
Enter details about your business idea, including its vision and budget. The AI system will analyze it based on economic, strategic, and marketing perspectives.
""")

#Inputs
business_idea = st.text_area("Describe your business idea:")
company_vision = st.text_area("What is the company vision?")
budget = st.number_input("Enter your budget ($)", min_value=0, value=100000, step=5000)

if st.button("Evaluate Business Idea"):
    if business_idea and company_vision and budget:
        with st.spinner("Running evaluation..."):
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/evaluate_business",
                    json={
                        "business_idea": business_idea,
                        "company_vision": company_vision,
                        "budget": budget
                    }
                )
                if response.status_code == 200:
                    result = response.json()
                    st.success("Evaluation Complete!")

                
                    st.subheader("Research Results")
                    st.text_area("", result["Research Results"], height=200)

                    st.subheader("Economic Analysis")
                    st.text_area("", result["Economic Analysis"], height=200)

                    st.subheader("Marketing Analysis")
                    st.text_area("", result["Marketing Analysis"], height=200)

                    st.subheader("Strategic Analysis")
                    st.text_area("", result["Strategic Analysis"], height=200)

                  
                    st.subheader("Final Business Evaluation")
                    st.text_area("", result["Final Evaluation"], height=400)

                else:
                    st.error(f"Error: {response.status_code} - {response.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"Connection error: {e}")
    else:
        st.warning("Please fill in all fields.")
