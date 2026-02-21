# David Zellhöfer 2026
import os
import sys
import time
from datetime import datetime
from bs4 import BeautifulSoup

html_base_path = "/Users/david/src/__datasets/2025_llm_forschung/2025_10_02_fb3_web/www.hwr-berlin.de/hwr-berlin/fachbereiche-und-bps/fb-3-allgemeine-verwaltung/"
# set to True if we have to deal with HWR pages
HWR_specific_parsing=True

# utility method that displays a given text and the current time
def printLog(text):
    now = str(datetime.now())
    print("[" + now + "]\t" + text)
    # forces to output the result of the print command immediately, see: http://stackoverflow.com/questions/230751/how-to-flush-output-of-python-print
    sys.stdout.flush()

# utility method that checks if certain directories exist and tries to create them if they are missing
# the function will also create all intermediate-level directories for each required directory
def requireDirectory(directories):
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)

# create required directories
data_directory="./data/"
req_dirs=[data_directory]
requireDirectory(req_dirs)

def write_text_file(txt_file_name, content):
    filename = data_directory + txt_file_name + '.txt'
    with open(filename, 'w', encoding='utf-8') as f:
        lines = content.split('\n')
        non_blank_lines = [line for line in lines if line.strip() != '']
        f.write('\n'.join(non_blank_lines))

def process_html():
    printLog(f"Crawling of '{html_base_path}' started.")
    start1 = time.process_time()

    # get the list of directories below html_base_path
    relevant_dirs = []
    for x in os.listdir(html_base_path):
        relevant_dirs.append(x)

    html_files = []
    total_files_in_dataset = 0
    # browse all directories below html_base_path
    for crawl in relevant_dirs:
        # print("Processing: " + (html_base_path+crawl)[-80:])
        # if we have a single HTML file, add it to the list
        if crawl.endswith('.html'):
            html_files.append(os.path.join(html_base_path, crawl))
            total_files_in_dataset = total_files_in_dataset + 1

        total_files_in_dataset = total_files_in_dataset + 1

        # check for HTML files below the current directory
        for dirpath, dirnames, files in os.walk(html_base_path + crawl):
            for dirname in dirnames:
                # print("\tProcessing: " + str(os.path.join(dirpath, dirname))[-80:])
                pass
            for name in files:
                # print("\t\tProcessing: " + str(os.path.join(dirpath, name))[-80:])
                # only consider HTML files
                if name.endswith('.html'):
                    html_file = os.path.join(dirpath, name)
                    html_files.append(html_file)
                total_files_in_dataset = total_files_in_dataset + 1
    printLog(f"Found {len(html_files):,} HTML files of {total_files_in_dataset:,} files in crawled directory.")

    printLog("Processing HTML files and extracting document links...")
    if HWR_specific_parsing:
        print("\t\t\t\t\t\t\t\tHWR specific parsing enabled.")

    running_index=0
    for html_file in html_files:
        if not os.path.exists(html_file):
            print("File not found: " + html_file)
        else:
            running_index = running_index + 1
            raw_html_text = open(html_file).read()
            soup = BeautifulSoup(raw_html_text, "html.parser")
            #title = soup.title.string if soup.title else "untitled"
            title="from_html"
            txt_name=f"{running_index}_{title}"

            if HWR_specific_parsing:
                real_contents=soup.find_all(class_="inner stack--xl")
                raw_text = ""
                for r in real_contents:
                    raw_text = raw_text + r.get_text()
                write_text_file(txt_name, raw_text)
            else:
                raw_text = soup.get_text()
                write_text_file(txt_name, raw_text)

if __name__ == "__main__":
    process_html()
    printLog("Done.")