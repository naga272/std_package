
from ansic import *
import ansic
import to_html


import pandas as pd
import wmi


import platform
import time
import sys
import os
import re


"""
    author:      Bastianello Federico
    consegna:    Titolo
    descrizione: descrizione
    date:        30 / 09 / 2023

"""


def main(argv, argc) -> int:
    try:
        return EXIT_SUCCESS

    except Exception as e:
        perror(e)
        return EXIT_FAILURE


if __name__ == "__main__":
    if ansic.log("../log/trace.csv", ansic.__FILE__) == EXIT_SUCCESS:
        if main(ansic.argv, argc) == EXIT_SUCCESS:
            printf(f"uscita dal programma con valore: {EXIT_SUCCESS}")
            ansic._exit(EXIT_SUCCESS)
        else:
            printf(f"uscita dal programma con valore: {EXIT_FAILURE}")
    else:
        printf(f"errore nella creazione del log! uscita dal programma con valore: {EXIT_FAILURE}")

    ansic._exit(EXIT_FAILURE)
