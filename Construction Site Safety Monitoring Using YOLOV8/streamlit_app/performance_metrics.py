import streamlit as st

def run():
    st.title("Model Peformance Evaluation")
    st.divider()
    st.subheader('Class Instances')
    st.image('final_dataset\Training_Result\ppe_model\lables_instances.png')
    st.divider()
    st.subheader('Confusion Matrix')
    st.image('final_dataset\Training_Result\ppe_model\confusion_matrix.png')
    st.divider()
    st.subheader('Precision Confidence Curve')
    st.image('final_dataset\Training_Result\ppe_model\P_curve.png')
    st.divider()
    st.subheader('Recall Confidence Curve')
    st.image('final_dataset\Training_Result\ppe_model\R_curve.png')
    st.divider()
    st.subheader('Precision Recall Curve')
    st.image('final_dataset\Training_Result\ppe_model\PR_curve.png')
    st.divider()
    st.subheader('F1 Confidence Curve')
    st.image('final_dataset\Training_Result\ppe_model\F1_curve.png')
    
    