from pycite.pycite import PyCite

def generate_citation():
    my_citations = PyCite(input_file="testlinks.txt", output_file="citations.txt")
    my_citations.cite()
generate_citation()