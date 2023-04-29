"""This file could get an RIS and a bibtex entry for a DOI."""

import requests
import bibtexparser


class Works:
    """This class could get an RIS and a bibtex entry for a DOI."""

    def __init__(self, oaid):
        """Get an RIS and a bibtex entry for a DOI."""
        self.oaid = oaid
        self.req = requests.get(f"https://api.openalex.org/works/{oaid}")
        self.data = self.req.json()

    def get_bibtex(self):
        """Get a bibtex entry for a DOI."""
        h = "application/x-bibtex"
        res = requests.get(self.data["doi"], headers={"Accept": h})
        db = bibtexparser.loads(res.text)
        self.bibtex = db.entries[0]
        return self.bibtex

    def get_RIS(self):
        """Get an RIS for a DOI."""
        fields = []
        if self.data["type"] == "journal-article":
            fields += ["TY  - JOUR"]
        else:
            raise Exception("Unsupported type {self.data['type']}")

        for author in self.data["authorships"]:
            fields += [f'AU  - {author["author"]["display_name"]}']

        fields += [f'PY  - {self.data["publication_year"]}']
        fields += [f'TI  - {self.data["title"]}']
        fields += [f'JO  - {self.data["host_venue"]["display_name"]}']
        fields += [f'VL  - {self.data["biblio"]["volume"]}']

        if self.data["biblio"]["issue"]:
            fields += [f'IS  - {self.data["biblio"]["issue"]}']

        fields += [f'SP  - {self.data["biblio"]["first_page"]}']
        fields += [f'EP  - {self.data["biblio"]["last_page"]}']
        fields += [f'DO  - {self.data["doi"]}']
        fields += ["ER  -"]

        self.ris = fields
        return self.ris
