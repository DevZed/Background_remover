import streamlit as st
from rembg import remove
from PIL import Image
import io

# Set the title of the app
st.title("Background Remover App")

# Upload an image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Load the uploaded image
    input_image = Image.open(uploaded_file)

    # Remove the background
    output_image = remove(input_image)

    # Display the result
    st.image(output_image, caption="Background Removed", use_column_width=True)

    # Download button
    buf = io.BytesIO()
    output_image.save(buf, format="PNG")
    byte_im = buf.getvalue()
    st.download_button(
        label="Download Image",
        data=byte_im,
        file_name="output.png",
        mime="image/png",
    )
