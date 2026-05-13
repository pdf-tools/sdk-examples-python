About this kit
==============

This kit contains the MultipleImg2Pdf sample for Pdftools SDK for Python. Pdftools SDK is a development library that lets you integrate PDF processing into your applications. For more information, review the Pdftools [documentation portal](https://www.pdf-tools.com/docs/).

By downloading and using this kit, you accept the Pdftools [license agreement](https://www.pdf-tools.com/license-agreement/) and [privacy policy](https://www.pdf-tools.com/privacy-policy/), and you allow Pdftools to track your usage data.

## Quick start

Follow these steps to install the required packages and run the sample.

### Prerequisites

- Python 3.7 or higher
- On some Linux-based systems, only Python 3 is installed and `python` isn't aliased. On these systems, run `python3` instead.

### Installation

We recommend installing into a virtual environment. On some Linux distributions (for example Ubuntu 23.04 and later), the system Python is externally managed and `pip install` will fail outside a venv.

Create and activate a virtual environment, then install the pinned dependencies from `requirements.txt`:

```bash
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

This installs Pdftools SDK at the version this sample was tested against.

### Usage

To run the sample:

```bash
python ./multiple_img2_pdf.py <input_path> [<input_path2> ...] <output_path>
```

To get help:

```bash
python ./multiple_img2_pdf.py -h
```

### Cross-platform compatibility

This sample works on Linux, macOS, and Windows.

## Licensing

- **Pdftools SDK** doesn't require a license key for evaluation. Without a license key, the SDK adds a watermark to output files.
- **Toolbox add-on** requires a trial or full license key to run. Without a valid license key, processing fails.

**Important:** Toolbox add-on processing fails without a valid license key.

To get a trial license key, create a user account at the [Pdftools portal](https://portal.pdf-tools.com/). For more information, refer to [Trial license overview](https://www.pdf-tools.com/docs/licenses/products/pdf-tools-sdk-license/#trial-license-overview).

## Technical support

Do you need technical support or want to report an issue?
Open a ticket through the [support form](https://www.pdf-tools.com/docs/support/).