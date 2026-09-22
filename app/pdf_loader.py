import fitz


class PDFLoader:

    def load(self, file_path):
        document = fitz.open(file_path)

        pages = []

        for page in document:
            text = page.get_text()
            pages.append(text)

        document.close()

        return "\n".join(pages)