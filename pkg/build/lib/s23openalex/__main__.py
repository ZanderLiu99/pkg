"""This file use cmd line to get an RIS and a bibtex entry for a DOI."""

import argparse
from s23openalex import Works


def main():
    """Get an RIS and a bibtex entry for a DOI."""
    parser = argparse.ArgumentParser(description="Get RIS or bibtex entry.")
    parser.add_argument("doi", help="Input the DOI.")
    parser.add_argument("--RIS", help="Get the RIS.", action="store_true")
    parser.add_argument("--bib", help="Get the bibtex.", action="store_true")

    args = parser.parse_args()
    ww = Works(args.doi)
    if args.RIS:
        print(ww.get_RIS())
    elif args.bib:
        print(ww.get_bibtex())
    else:
        print("Please select an option (--RIS or --bibtex).")


if __name__ == "__main__":
    main()
