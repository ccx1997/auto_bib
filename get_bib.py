from scholarly import scholarly
import bibtexparser
import json
import string


def get_bibtex_citation(paper_title):
    # 搜索论文
    search_query = scholarly.search_pubs(paper_title)
    
    # 获取第一个搜索结果
    paper = next(search_query)
    
    # 获取论文的 BibTeX 格式引用
    bibtex = scholarly.bibtex(paper)
    
    # 返回去掉 abstract 的结果
    bibtex = bibtex.split("\n")  # 按行分割
    valid_parts = []
    for line in bibtex:
        line = line.strip()
        if line.startswith(("abstract", "venue")):
            continue
        if line.startswith("pub_year"):
            line = line.replace("pub_year", "year")
        if len(line) > 0 and line[0] in string.ascii_letters:
            line = "  " + line
        valid_parts.append(line)
    ret = "\n".join(valid_parts)
    ret = ret.strip() + "\n"

    return ret


def extract_keys_and_titles_from_bib(bib_file_path):
    with open(bib_file_path) as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)
    
    keys_and_titles = [
        [entry['ID'], entry['title']] 
        for entry in bib_database.entries if 'title' in entry
    ]
    return keys_and_titles


if __name__ == "__main__":
    bib_file_path = "egbib.bib"
    references_path = "references.json"
    
    with open(references_path, "r") as f:
        references = json.load(f)
    f_bib = open(bib_file_path, "a")
    for ref in references:
        if len(ref[0]) == 0 and len(ref[1].strip()) > 0:
            title = ref[1]
            print(f"getting bib of {title}")
            bibtex_str = get_bibtex_citation(title)
            bib_id = bibtexparser.loads(bibtex_str).entries[0]['ID']
            ref[0] = bib_id
            f_bib.writelines(bibtex_str)

    f_bib.close()
    with open(references_path, "w") as f:
        json.dump(references, f, indent=4, ensure_ascii=False)
