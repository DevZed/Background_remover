import streamlit as st
import cv2
import numpy as np
from PIL import Image
import io

# Set the title of the app
st.title("Background Remover App")

# Upload an image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Load the uploaded image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    input_image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    # Convert to grayscale
    gray = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

    # Apply a threshold to create a mask
    _, mask = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)

    # Invert the mask
    mask = cv2.bitwise_not(mask)

    # Apply the mask to the original image
    output_image = cv2.bitwise_and(input_image, input_image, mask=mask)

    # Convert the result to PIL format for display
    output_image = cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB)
    output_image = Image.fromarray(output_image)

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
