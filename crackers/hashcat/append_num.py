import os
n = 0

def wait():
  wait = input('PRESS ENTER TO CONTINUE')

def home():
  global n
  print("                                                __                                   ")
  print("    ____ _   ____     ____   ___    ____   ____/ /          ____   __  __   ____ ___ ")
  print('   / __  /  / __ \   / __ \ / _ \  / __ \ / __  /          / __ \ / / / /  / __  __ \)')
  print('  / /_/ /  / /_/ /  / /_/ //  __/ / / / // /_/ /          / / / // /_/ /  / / / / / /')
  print("  \__,_/  / .___/  / .___/ \___/ /_/ /_/ \__,_/  ______  /_/ /_/ \__,_/  /_/ /_/ /_/ ")
  print("         /_/      /_/                           /_____/                         v1.0 ")
  print('======================================================================================')
  print('*[1] Import words from wordlist                                                      *')
  print('*[2] Single word                                                                     *')
  print('*[3] Exit                                                                            *')
  print('======================================================================================')
  in_put = input(': ')
  if in_put == '1':
    fp = input("Enter filepath (/####/) of wordlist or type 'local' for local: ")
    if fp == 'local':
      fpl = input('Enter filename: ')
      try:
        with open(fpl, 'r') as f:
          contents = f.read().splitlines()
          n += 1
          with open('num_output' + str(n) + '.txt', 'a+') as n:
            for w in contents:
              n.write(str(w) + '\n')
              for i in range(0,100):
                n.write(str(w) + str(i) + '\n')
        os.system('mv num_output' + str(n) + '.txt Hashlists')
        print('num_output' + str(n) + '.txt generated and moved to Hashlists!')
        wait()
      except:
        print(':ERROR: [1] Incorrect filepath, [2] Incorrect filename, [3] Wordlist empty, [4]Wordlist not formatted into seperate lines.')
        wait()
        home()
    else:
      os.chdir(fp)
      fpl = input('Enter filename: ')
      try:
        with open(fpl, 'r') as f:
          contents = f.read().splitlines()
          n += 1
          with open('num_output' + str(n) + '.txt', 'a+') as n:
            for w in contents:
              n.write(str(w) + '\n')
              for i in range(0,100):
                n.write(str(w) + str(i) + '\n')
        os.system('mv num_output' + str(n) + '.txt Hashlists')
        print('num_output' + str(n) + '.txt generated and moved to Hashlists!')
        wait()
      except:
        print(':ERROR: [1] Incorrect filepath, [2] Incorrect filename, [3] Wordlist empty, [4]Wordlist not formatted into seperate lines.')
        wait()
        home()
  elif in_put == '2':
    word = input('Enter word for wordlist: ')
    try:
      n += 1
      with open('num_output' + str(n) + '.txt', 'a+') as f:
        for i in range(1,100):
          f.write(str(word) + str(i) + '\n')
      os.system('mv num_output' + str(n) + '.txt Hashlists')
      print('num_output' + str(n) + '.txt generated and moved to Hashlists!')
      wait()
    except:
      print(':ERROR: [1] Incorrect filepath, [2] Incorrect filename, [3] Wordlist empty, [4]Wordlist not formatted into seperate lines.')
      wait()
      home()
  elif in_put == '3':
    exit()
  home()

home()
