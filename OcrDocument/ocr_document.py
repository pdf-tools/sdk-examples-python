"""
File: ocr_document.py
Usage: python ./ocr_document.py <ocr_engine_name> <language> <input_path> <output_path>
Author: PDF Tools AG
Copyright: Copyright (C) 2024 PDF Tools AG, Switzerland

OCR a PDF document

"""

import io
from pdftools_sdk.pdf import Document
from pdftools_sdk.ocr import Engine, Processor, OcrOptions
from pdftools_sdk.ocr.image_processing_mode import ImageProcessingMode
from pdftools_sdk.ocr.text_processing_mode import TextProcessingMode
from pdftools_sdk.ocr.text_skip_mode import TextSkipMode
from pdftools_sdk.ocr.unicode_source import UnicodeSource
from pdftools_sdk.ocr.page_processing_mode import PageProcessingMode
from pdftools_sdk.ocr.tagging_mode import TaggingMode

import argparse, io

def warning_handler(message: str, category, page_no: int, context: str):
    if page_no > 0:
        print(f"- {category.name}: {message} ({context} page {page_no})")
    else:
        print(f"- {category.name}: {message} ({context})")


def ocr_document(ocr_engine_name: str, language: str, input_path: str, output_path: str):
    # Create the OCR engine
    with Engine.create(ocr_engine_name) as engine:
        # Set the language(s) for OCR recognition (e.g. "German,English")
        engine.languages = language
        # Open input document
        with io.FileIO(input_path, 'rb') as in_stream:
            with Document.open(in_stream) as input_document:
                # Configure OCR options
                options = OcrOptions()
                # Configure image OCR: recognize text from scanned images
                options.image_options.mode = ImageProcessingMode.UPDATE_TEXT
                options.image_options.remove_only_invisible_ocr_text = True
                options.image_options.deskew_scan = True
                options.image_options.rotate_scan = True
                # Configure text OCR: update non-extractable text with correct Unicode
                options.text_options.mode = TextProcessingMode.UPDATE
                options.text_options.skip_mode = TextSkipMode.KNOWN_SYMBOLIC
                options.text_options.unicode_source = UnicodeSource.INSTALLED_FONT
                # Configure page OCR: process all pages and add tagging for accessibility
                options.page_options.mode = PageProcessingMode.ALL
                options.page_options.tagging = TaggingMode.AUTO
                # Create the OCR processor and add a warning handler
                processor = Processor()
                processor.add_warning_handler(warning_handler)
                # Create stream for output file
                with io.FileIO(output_path, 'wb+') as output_stream:
                    # Process the document with OCR
                    processor.process(input_document, engine, output_stream, options)



if __name__ == "__main__":
    # Create the parser
    parser = argparse.ArgumentParser(description="Apply OCR to a PDF document to make scanned content searchable. Text is recognized from images, existing text is updated with correct Unicode, and tagging is added for accessibility.", usage="python ./ocr_document.py <ocr_engine_name> <language> <input_path> <output_path>")

    # Add arguments
    parser.add_argument("ocr_engine_name", type=str)
    parser.add_argument("language", type=str)
    parser.add_argument("input_path", type=str)
    parser.add_argument("output_path", type=str)

    # Parse the arguments
    args = parser.parse_args()

    ocr_engine_name = args.ocr_engine_name
    language = args.language
    input_path = args.input_path
    output_path = args.output_path

    try:
        # By default, a test license key is active. In this case, a watermark is added to the output. 
        # If you have a license key, please uncomment the following call and set the license key.
        # from pdftools_sdk.sdk import Sdk
        # Sdk.initialize("<-- insert license key -->")

        ocr_document(ocr_engine_name, language, input_path, output_path)

        print(f"Successfully created file {output_path}")

        exit(0)
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)