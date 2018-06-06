#!/usr/bin/env python3
# This file will prompt the user for an .Xresources file in the style of 
# terminal.sexy's export option.
# It will then prompt the user for their bar script variable, 
# wallpaper, wallpaper style, font, and pixelsize for font.
# It will then output a squash theme using the colors and inputs entered.

filename = input("Please enter your .Xresources input file: ")
def parse_resources():
    """A function to parse xresources into hex only"""
    try:
        with open(filename) as f_obj:
            lines = f_obj.readlines()
            l = []
            for line in lines:
                l.append(line.rstrip().split(','))
            to_delete = [37,34,33,30,29,26,25,22,21,18,17,14,13,10,9,6,5,4,1]
            # by line number
            for item in to_delete:
                del l[item - 1] # by index
            # string[-7:] to slice the last seven of all
            only_hex = []
            for x in range(0,18):
                only_hex.append(str(l[x])[-9:-2])
            return only_hex
    except FileNotFoundError: 
        msg = "Sorry, the file " + filename + " does not exist." 
        print(msg) 
good_hex = parse_resources()

outfile = str(filename + ".squash")

def write_theme():
    """Write the good_hex to a squash theme"""
    with open(outfile, 'a') as f_obj:
        f_obj.write("#!/bin/bash\n\n")
        f_obj.write("#DEFINE COLORS\n")
        f_obj.write("BG=\"" + good_hex[1] + "\"\n")
        f_obj.write("FG=\"" + good_hex[0] + "\"\n\n")
        f_obj.write("BLK=\"" + good_hex[2] + "\"\n")
        f_obj.write("RED=\"" + good_hex[4] + "\"\n")
        f_obj.write("GRN=\"" + good_hex[6] + "\"\n")
        f_obj.write("YLW=\"" + good_hex[8] + "\"\n")
        f_obj.write("BLU=\"" + good_hex[10] + "\"\n")
        f_obj.write("MAG=\"" + good_hex[12] + "\"\n")
        f_obj.write("CYN=\"" + good_hex[14] + "\"\n")
        f_obj.write("WHT=\"" + good_hex[16] + "\"\n\n")

        f_obj.write("BBLK=\"" + good_hex[3] + "\"\n")
        f_obj.write("BRED=\"" + good_hex[5] + "\"\n")
        f_obj.write("BGRN=\"" + good_hex[7] + "\"\n")
        f_obj.write("BYLW=\"" + good_hex[9] + "\"\n")
        f_obj.write("BBLU=\"" + good_hex[11] + "\"\n")
        f_obj.write("BMAG=\"" + good_hex[13] + "\"\n")
        f_obj.write("BCYN=\"" + good_hex[15] + "\"\n")
        f_obj.write("BWHT=\"" + good_hex[17] + "\"\n\n")

        f_obj.write("# ROFI OPTIONS\n")
        f_obj.write("ACC=\"${RED}\"\n\n")
        
        f_obj.write("# BAR OPTIONS\n")
        bar_script = input("Please enter your bar script variable: ")
        f_obj.write("BAR_SCRIPT=\"" + bar_script + "\"\n\n")
        f_obj.write("# VIM COLORSCHEME\n")
        f_obj.write("VIM_SCHEME='" + filename + "'\n\n")
        
        f_obj.write("# WALLPAPER OPTIONS\n")
        wallpaper = input("Please enter the name of your wallpaper located in ~/Wallpapers/ : ")
        f_obj.write("WALLPAPER_PATH=\"$HOME/Wallpapers/" + wallpaper + "\"\n")
        wall_style = input("Please enter your wallpaper style: ")
        f_obj.write("WALLPAPER_STYLE=\"" + wall_style + "\"\n\n")

        f_obj.write("# 2BWM OPTIONS\n")
        f_obj.write("TWOBWM_FOCUS=\"${BBLK}\"\n")
        f_obj.write("TWOBWM_UNFOCUS=\"${BLK}\"\n")
        f_obj.write("TWOBWM_FIXED=\"${RED}\"\n")
        f_obj.write("TWOBWM_UNKILL=\"${CYN}\"\n")
        f_obj.write("TWOBWM_FIXEDUNK=\"${MAG}\"\n")
        f_obj.write("TWOBWM_OUTR=\"${BG}\"\n")
        f_obj.write("TWOBWM_EMP=\"${BG}\"\n\n")
        
        f_obj.write("# BSPWM OPTIONS\n")
        f_obj.write("BSPWM_NORMAL=\"${BBLK}\"\n")
        f_obj.write("BSPWM_FOCUSED=\"${CYN}\"\n")
        f_obj.write("BSPWM_URGENT=\"${RED}\"\n")
        f_obj.write("BSPWM_PRESEL=\"${GRN}\"\n\n")

        f_obj.write("# LEMONBAR OPTIONS\n")
        f_obj.write("LMNBAR_DARK=\"${BBLK}\"\n")
        f_obj.write("LMNBAR_DARKER=\"${BLK}\"\n\n")

        f_obj.write("OB_THEME=\"" + filename + "\"\n")
        font = input("Enter your font: ")
        pixelsize = input("Enter your pixelsize: ")
        f_obj.write("SQUASH_FONT=\"xft:" + font + ":pixelsize=" + pixelsize + "\"\n")

write_theme()
