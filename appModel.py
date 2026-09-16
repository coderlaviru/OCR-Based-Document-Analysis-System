import streamlit as st

from utils.file_handler import (
    save_uploaded_file,
    get_file_extension
)

from preprocessing.image_preprocess import (
    preprocess_image
)

from preprocessing.pdf_converter import (
    convert_pdf_to_images
)

from preprocessing.docx_reader import (
    read_docx
)

from ocr_engine.paddle_ocr import (
    run_ocr
)

from ocr_engine.text_extractor import (
    save_text
)


st.title(
    "Deep Learning OCR Document Analysis System"
)

uploaded_file = st.file_uploader(
    "Upload File",
    type=["pdf", "jpg", "png", "jpeg", "docx"]
)


if uploaded_file is not None:

    file_path = save_uploaded_file(uploaded_file)

    extension = get_file_extension(file_path)

    extracted_text = ""

    # IMAGE FILES
    if extension in ["jpg", "png", "jpeg"]:

        processed_image = preprocess_image(file_path)

        extracted_text = run_ocr(processed_image)

    # PDF FILES
    elif extension == "pdf":

        image_paths = convert_pdf_to_images(file_path)

        for image_path in image_paths:

            processed_image = preprocess_image(image_path)

            extracted_text += run_ocr(processed_image)

    # DOCX FILES
    elif extension == "docx":

        extracted_text = read_docx(file_path)

    st.subheader("Extracted Text")

    st.text_area(
        "OCR Output",
        extracted_text,
        height=300
    )

    saved_file = save_text(extracted_text)

    st.success(
        f"Text saved successfully: {saved_file}"
    )

