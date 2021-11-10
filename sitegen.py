import os
import json
import html

def files_to_json(folder, output):
  temp_json = {}
  for dir in os.listdir(folder):
    temp_json[dir] = {}
    temp_json[dir]['files'] = []
    for file in os.listdir(folder + '/' + dir):
      temp_json[dir]['files'].append(folder + '/' + dir + '/' + file)
  with open(output, 'w') as f:
    json.dump(temp_json, f)

def generate_html():
  with open('files.json') as f:
    data = json.load(f)
  
  with open('index.html', 'w') as f:
    f.write('<!DOCTYPE html>\n')
    f.write('<html>\n')
    f.write('<head>\n')
    f.write('<title>MyUsU</title>\n')
    f.write('<link rel="stylesheet" href="style.css">\n')
    f.write('</head>\n')
    f.write('<body>\n')
    f.write('<div class="container">\n')
    f.write('<div class="header">\n')
    f.write('<h1>MyUsU</h1>\n')
    f.write('</div>\n')
    f.write('<div class="content">\n')
    for dir in data:
      f.write('<div class="dir">\n')
      f.write('<h2>' + dir + '</h2>\n')
      f.write('<div class="files">\n')
      for file in data[dir]['files']:
        f.write('<img src="' + file + '">\n')
      f.write('</div>\n')
      f.write('</div>\n')
    f.write('</div>\n')
    f.write('</div>\n')
    f.write('</body>\n')
    f.write('</html>\n')

def main():
  files_to_json('res/images/myusu', 'res/data/files.json')
  #generate_html()
  return

if __name__ == '__main__':
  main()