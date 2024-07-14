import argparse

def manim_argparse():
    args = argparse.ArgumentParser(description="Render all Manim scripts in the current folder. example command: python ./renderall.py -q h -f SawOsc")
    args.add_argument("-f", "--folder", type=str,  help="The directory containing the manim scripts to be rendered")
    args.add_argument("-q", "--quality", type=str, default="l", help="Set the rendering quality (l, m, h, k)")
    args.add_argument("-p", "--preview", action="store_true", help="Preview the rendered video after rendering")
    args.add_argument("--other_args", type=str, default="", help="Other arguments to pass to Manim")
    
    return args    
    
def build_manim_command(fname, args):
    command = 'manim '

    if(args.preview) :
        command += '-p '
    
    if(args.quality) :
        command += '-q'
        command += args.quality

    if(args.other_args) :
        command += ' '
        command += args.other_args    
    
    command += ' '

    return command

