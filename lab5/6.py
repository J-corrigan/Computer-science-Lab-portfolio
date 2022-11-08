import shutil
import sys

filename_in = sys.argv
filename, extension = filename_in.split('.')
filename_out = f'{filename}-copy.{extension}'
shutil.copyfile(filename_in, filename_out)
