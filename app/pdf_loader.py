import pymupdf


class PDFLoader:

    def load(self, file_path):
        document = pymupdf.open(file_path)

        pages = []

        for page_number, page in enumerate(document, start=1):
            text = page.get_text()
            pages.append({
                "text": text,
                "page":page_number
                })

        document.close()

        return pages