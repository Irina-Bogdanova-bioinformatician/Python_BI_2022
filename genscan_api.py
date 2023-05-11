"""
В данном задании вам потребуется сделать Python API для сервиса http://hollywood.mit.edu/GENSCAN.html

Он способен находить и вырезать интроны в переданной нуклеотидной последовательности.
Делает он это не очень хорошо, но это лучше, чем ничего. К тому же, у него действительно нет публичного API.

Реализуйте следующую функцию:
run_genscan(sequence=None, sequence_file=None, organism="Vertebrate", exon_cutoff=1.00, sequence_name="") —
выполняет запрос аналогичный заполнению формы на сайте. Принимает на вход все параметры, которые можно указать на сайте
(кроме Print options). sequence — последовательность в виде строки или любого удобного вам типа данных,
sequence_file — путь к файлу с последовательностью, который может быть загружен и использован вместо sequence.
Функция должна будет возвращать объект типа GenscanOutput. Про него дальше.

Реализуйте датакласс GenscanOutput, у него должны быть следующие поля:

status — статус запроса
cds_list — список предсказанных белковых последовательностей с учётом сплайсинга (в самом конце результатов с сайта)
intron_list — список найденных интронов. Один интрон можно представить любым типом данных, но он должен хранить
информацию о его порядковом номере, его начале и конце. Информацию о интронах можно получить из первой таблицы
в результатах на сайте.
exon_list — всё аналогично интронам, но только с экзонами.
По желанию можно добавить любые данные, которые вы найдёте в результатах.
"""

from dataclasses import dataclass
from typing import List
import requests
from bs4 import BeautifulSoup
from collections import namedtuple
import re
import argparse
from pathlib import Path


ExonInfo = namedtuple("ExonInfo", ["gene_exon_number", "start", "stop", "type"])
IntronInfo = namedtuple("IntronInfo", ["gene_intron_number", "start", "stop"])
CDSInfo = namedtuple("CDSInfo", ["id", "sequence"])
ProteinInfo = namedtuple("ProteinInfo", ["id", "sequence"])


@dataclass
class GenscanOutput:
    status: int
    gc_content: str = None
    genscan_version: int = None
    cds_list: List[CDSInfo] = None
    peptides_list: List[ProteinInfo] = None
    intron_list: List[IntronInfo] = None
    exon_list: List[ExonInfo] = None


def run_genscan(sequence=None, sequence_file=None, organism="Vertebrate", exon_cutoff=1.00, sequence_name=""):
    if sequence is None and sequence_file is None:
        print("Either path to file with sequence or string with sequence must be indicated")
        out = None
    else:
        if sequence is not None and sequence_file is not None:
            print("As both path to file with sequence and string with sequence are indicated, "
                  "the second parameter will be used")
            sequence_file = None

        site_url = "http://hollywood.mit.edu/cgi-bin/genscanw_py.cgi"
        if sequence_file:
            form_data = {
                "-o": (None, organism),
                "-e": (None, str(exon_cutoff)),
                "-n": (None, sequence_name),
                "-p": (None, "Predicted CDS and peptides "),
                "-u": (None, open(sequence_file, "rb")),
                "-s": (None, sequence)
            }
        else:
            form_data = {
                "-o": (None, organism),
                "-e": (None, str(exon_cutoff)),
                "-n": (None, sequence_name),
                "-p": (None, "Predicted CDS and peptides "),
                "-u": (None, sequence_file),
                "-s": (None, sequence)
            }
        response = requests.post(site_url + "/submit-form", files=form_data)

        out = GenscanOutput(status=response.status_code)
        if out.status == 200:
            soup = BeautifulSoup(response.content, "lxml")
            info = soup.find("pre").contents[0]
            out.genscan_version = re.findall(r"GENSCAN \d+\.\d+", info)[0].split(" ")[1]
            out.gc_content = re.findall(r"\d+\.?\d*% C\+G", info)[0].split(" ")[0]

            cds = re.findall(r"GENSCAN_predicted_CDS_\d+\|\d+_bp[agctn-]+", info.replace("\n", ""))
            cds_list = []
            for el in cds:
                n, seq = el.split(re.findall(r"\|\d+_bp", el)[0])
                cds_list.append(CDSInfo(n, seq))
            out.cds_list = cds_list

            proteins = re.findall(r"GENSCAN_predicted_peptide_\d+\|\d+_aa[A-Z]+", info.replace("\n", ""))
            protein_list = []
            for el in proteins:
                n, seq = el.split(re.findall(r"\|\d+_aa", el)[0])
                protein_list.append(ProteinInfo(n, seq))
            out.peptides_list = protein_list

            exons = re.findall(r"----- ------\n\n\n\n \d+\.\d+[\d\sA-Za-z+.]+\n\n\n\n", info)[0]

            if "Init" in exons:
                exons = exons.replace("----- ------\n\n\n\n ", "").replace("\n\n\n\n", "").split("\n\n ")
                exons_list = []
                for el in exons:
                    info_elements = el.split()
                    n, start, end, ex_type = info_elements[0], info_elements[3], info_elements[4], info_elements[1]
                    exons_list.append(ExonInfo(n, start, end, ex_type))
                out.exon_list = exons_list

                introns_list = []
                n_introns = len(exons_list) - 1
                for i in range(n_introns):
                    n, start, end = exons_list[i].gene_exon_number, int(exons_list[i].stop) + 1, int(
                        exons_list[i + 1].start) - 1
                    introns_list.append(IntronInfo(n, start, end))
                out.intron_list = introns_list
    return out


def main(organism, exon_cutoff, out_file, sequence, sequence_file, sequence_name=""):
    results = run_genscan(sequence, sequence_file, organism, exon_cutoff, sequence_name)
    with open(out_file, "w") as outfile:
        outfile.write(str(results))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Get GENSCAN results")
    parser.add_argument('--sequence', help='DNA sequence (upper or lower case, spaces/numbers ignored). '
                                           'Either this parameter or "sequence_file" must be indicated',
                        type=str)
    parser.add_argument('--sequence_file', type=Path,
                        help='Path to file containing the sequence (upper or lower case, spaces/numbers ignored). '
                             'Either this parameter or "sequence" must be indicated')
    parser.add_argument('--organism', type=str, choices=["Vertebrate", "Arabidopsis", "Maize"], default='Vertebrate',
                        help='Select the organism that is the DNA sequence source. Default: Vertebrate')
    parser.add_argument('--exon_cutoff', type=str,
                        choices=['0.01', '0.02', '0.05', '0.10', '0.25', '0.50', '1.00'], default='1.00',
                        help='The probability cutoff used to determine which potential exons qualify as suboptimal'
                             ' exons. Default 1.00')
    parser.add_argument('--sequence_name', type=str, help='Name of the DNA sequence (optional)')
    parser.add_argument('--output_file', type=Path, help='Path to output file', default="genscan_output.txt")
    args = parser.parse_args()

    main(out_file=args.output_file, sequence=args.sequence, sequence_file=args.sequence_file, organism=args.organism,
         exon_cutoff=args.exon_cutoff, sequence_name=args.sequence_name)
