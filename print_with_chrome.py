#!/usr/bin/env python3


# Author: Alex Baranowski <ab at euro-linux.com>

import PyChromeDevTools
import time
import argparse
import base64


TIMEOUT_TIME=120
WAIT_TIME=10

default_args={
    "print_to": "output.pdf",
    "landscape": False,
    "displayHeaderFooter": False,
    "printBackground": False,
    "paperWidth": 8.5,  # inch
    "paperHeight": 11.0,  # inch
    "marginTop": 1.0,  # 1cm
    "marginBottom": 1.0,
    "marginLeft": 1.0,
    "marginRight": 1.0,
    "pageRanges": "",
    "ignoreInvalidPageRanges": False,
    "headerTemplate": "",
    "footerTemplate": "",
    "preferCSSPageSize": False
}


def str2bool(val):
    if isinstance(val, bool):
        return val
    exception_message = 'Boolean value expected. Supported values (ignorecased) yes/no true/false t/f y/n 1/0'
    try: 
        val = val.lower()
        if val in ('yes', 'true', 't', 'y', '1'):
            return True
        elif val in ('no', 'false', 'f', 'n', '0'):
            return False
    except:
        raise argparse.ArgumentTypeError(exception_message + f"Unkown value type: {type(val)}")
    raise argparse.ArgumentTypeError(exception_message)

def main(args_dict):
    url = args_dict['url']
    del(args_dict['url'])
    print_to = args_dict['print_to']
    del(args_dict['print_to'])
    chrome = PyChromeDevTools.ChromeInterface(timeout=TIMEOUT_TIME)
    chrome.Network.enable()
    chrome.Page.enable()
    print("Loading page... ")
    chrome.Page.navigate(url=url)
    time.sleep(WAIT_TIME)
    chrome.wait_event("Page.frameStoppedLoading", timeout=60)
    print(f"Making PDF (this might take some time) timeout set to - {TIMEOUT_TIME}...")
    response = chrome.Page.printToPDF(**args_dict)
    with open(print_to, 'wb') as f:
        f.write(base64.decodebytes(str.encode(response['result']['data'])))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=f"Set printing values. Default values: {default_args}")
    parser.add_argument('url', help='url to print')
    for k in default_args:
        if isinstance(default_args[k], bool):
            parser.add_argument(f'--{k}', type=str2bool, help=f"[boolean] default value: {default_args[k]}")
        elif isinstance(default_args[k], float):
            parser.add_argument(f'--{k}', type=float, help=f"[float] default value: {default_args[k]}")
        elif isinstance(default_args[k], str):
            parser.add_argument(f'--{k}', type=str, help=f"[string] default value: {default_args[k]}")
        else:
            raise Exception(f"Check default arguments {k}")
    parsed_args = parser.parse_args()
    args={}
    args['url']=parsed_args.url
    # This sucks
    del(parsed_args.url)
    for k in vars(parsed_args):
        print(f"default for {k} is {default_args[k]}")
        parsed_arg = getattr(parsed_args, k)
        args[k] = parsed_arg if parsed_arg is not None else default_args[k]
    print("Printing args", args)
    main(args)
