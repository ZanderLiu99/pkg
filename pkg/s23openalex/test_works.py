"""This file test the works."""

import pytest
from s23openalex import Works

bib = {
    "journal": "{ACS} Catalysis",
    "title": "Examples of Effective Data Sharing in Scientific Publishing",
    "author": "John R. Kitchin",
    "pages": "3894--3899",
    "number": "6",
    "volume": "5",
    "publisher": "American Chemical Society ({ACS})",
    "month": "may",
    "year": "2015",
    "url": "https://doi.org/10.1021%2Facscatal.5b00538",
    "doi": "10.1021/acscatal.5b00538",
    "ENTRYTYPE": "article",
    "ID": "Kitchin_2015",
}

RIS = [
    "TY  - JOUR",
    "AU  - John R. Kitchin",
    "PY  - 2015",
    "TI  - Examples of Effective Data Sharing in Scientific Publishing",
    "JO  - ACS Catalysis",
    "VL  - 5",
    "IS  - 6",
    "SP  - 3894",
    "EP  - 3899",
    "DO  - https://doi.org/10.1021/acscatal.5b00538",
    "ER  -",
]


@pytest.fixture()
def setup_bib():
    """Get a bibtex entry for a DOI."""
    return bib


class TestBib:
    """Test a bibtex entry for a DOI."""

    def test_Bib(self, setup_bib):
        """Test a bibtex entry for a DOI."""
        w = Works("https://doi.org/10.1021/acscatal.5b00538")
        bib = w.get_bibtex()
        assert bib == setup_bib


@pytest.fixture()
def setup_RIS():
    """Get an RIS for a DOI."""
    return RIS


class TestRIS:
    """Test an RIS for a DOI."""

    def test_RIS(self, setup_RIS):
        """Test an RIS for a DOI."""
        w = Works("https://doi.org/10.1021/acscatal.5b00538")
        RIS = w.get_RIS()
        assert RIS == setup_RIS
