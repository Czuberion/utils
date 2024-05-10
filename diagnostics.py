#!/usr/bin/env python3

import argparse
import subprocess
import os

def run_scc(path, context):
    if context.get('verbose', False):
        print(f"Running 'scc -c --no-cocomo' on {path}")
    subprocess.run(['scc', '-c', '--no-cocomo', path])
    return True

def run_tree(path, context):
    is_only_command = context['total_requested'] == 1
    if os.path.isfile(path):
        # The "skipped" message for the `tree` command is shown based on specific conditions
        # and is not affected by the verbose option.
        if is_only_command and context['commands']['tree']:
            print("'tree' command skipped because the target is a file.")
        return False
    if context.get('verbose', False):
        print(f"Running 'tree --gitignore' on {path}")
    subprocess.run(['tree', '--gitignore', path])
    return True

def main():
    parser = argparse.ArgumentParser(description="Run diagnostics on a specified path.")
    parser.add_argument('path', type=str, help="The file or directory to run diagnostics on.")
    parser.add_argument('-s', '--sloc', action='store_true', help="Run 'scc -c --no-cocomo'")
    parser.add_argument('-t', '--tree', action='store_true', help="Run 'tree --gitignore'")
    parser.add_argument('-v', '--verbose', action='store_true', help="Print details about command execution.")
    args = parser.parse_args()

    commands = {
        'sloc': run_scc,
        'tree': run_tree,
    }

    requested_commands = {k: v for k, v in vars(args).items() if k in commands and v}

    context = {
        'commands': requested_commands,
        'total_requested': sum(requested_commands.values()),
        'verbose': args.verbose,
    }

    if not requested_commands:
        # When no commands are specifically requested, `run_scc` and `run_tree` are executed.
        run_scc(args.path, context)
        run_tree(args.path, context)
    else:
        for name, command in commands.items():
            if name in requested_commands:
                command(args.path, context)

if __name__ == "__main__":
    main()

