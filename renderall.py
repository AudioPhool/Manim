import argparse 
from renderHelper import *
import os
import subprocess
import re
from natsort import natsorted
def main():
    # Set up argument parser
    parser = manim_argparse()
    args = parser.parse_args()
    
    #get dir for render
    current_dir = os.getcwd()
    render_dir = current_dir + '/project/' + args.folder + '/'
    media_dir = current_dir + '/media/videos/'
    if(__debug__) :
        print('@D: render dir is: ' + render_dir)
    
    #build manim command
    command = build_manim_command('test', args)
    if(__debug__) :
        print('@D: manim command is: ' + command)
    
    #get a list of all Python files in the render directory & sort alphabetically
    script_files = natsorted([f for f in os.listdir(render_dir) if f.endswith('.py')])


    #regex to find numbers or number patterns
    pattern = re.compile(r'\d+[-_]\d+|\d+')

    for fname in script_files :
        temp_cmd = command + str(render_dir) + fname

        # Search for the pattern in the filename
        extracted_num = pattern.search(fname).group()
        if(__debug__) :
            print('@D: executing command: ' + temp_cmd)
        subprocess.run(temp_cmd, shell=True)
        new_filename = '/anim' + str(extracted_num) + '.mp4'
        if(__debug__) :
            print('@D: render complete! renaming anim.mp4 to ' + new_filename)

        #remove extension from filepath
        fname = os.path.splitext(fname)[0]

        #detect quality
        if args.quality == 'l':
            quality_fp = '/480p15'
        elif args.quality == 'm':
            quality_fp = '/720p30'
        elif args.quality == 'h':
            quality_fp = '/1080p60'
        elif args.quality == 'k':
            quality_fp = '/2160p60'
        
        #create new & old filepaths to rename output file
        old_fpath = media_dir + fname + quality_fp + '/anim.mp4'
        new_fpath = media_dir + fname + quality_fp + new_filename
        if(__debug__) :
            print('@D: renaming ' + old_fpath + ' to ' + new_fpath)
        
        #rename the files
        try:
            os.rename(src=old_fpath, dst=new_fpath)
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    if __debug__:
        print('You are running me with debug (@D) ENABLED. Run with -O to DISABLE.')
    else:
        print('Debug (@D) is DISABLED due to -O flag')
    main()