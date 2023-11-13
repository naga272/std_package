
from ansic import *
import ansic

import platform
import sys
import os
import re


def head_html(f_in:object):
    fprintf(f_in, f"<!DOCTYPE html>\n")
    fprintf(f_in, f"<html>\n")
    fprintf(f_in, "\t<head>\n")
    fprintf(f_in, "\t\t<title>usage</title>\n")
    fprintf(f_in, "\t\t<meta charset='UTF-8'>\n")
    fprintf(f_in, "\t\t<meta name='viewport' content='width=device-width, initial-scale=1.0'>\n")
    fprintf(f_in, f"\t\t<meta name='author' content='{os.environ['USERNAME']}'>\n")
    fprintf(f_in, f"\t\t<link href='css/style.css' rel='StyleSheet'>\n")
    fprintf(f_in, f"\t\t<style></style>\n")
    fprintf(f_in, "\t</head>\n")
