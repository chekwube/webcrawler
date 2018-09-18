import os

#each site crawled is a project
def create_project_dir(directory):
    if not os.path.exists(directory):
        print("creating a new project" + directory)
        os.makedirs(directory)

#Create queue and Crawled files(if not created)
def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
        write_file(crawled, '')

#Create a new file
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

#Add data onto an existing fle
def append_file_contents(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')

#Delete contents of a file
def delete_file_contents(path):
    with open(path, 'w') as file:
        pass

#read afile and convert each line to set items
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results

#iterate through a set, each item will be a new line in the file
def set_to_file(links, file):
    delete_file_contents(file)
    for link in sorted(links):
        append_file_contents(file, link)
        