#!/usr/bin/env python3

"Command-line entrypoint"

import argparse
import json

import fredhutch_batch_wrapper

# to test this without installing the package, run:
# python -c 'from fredhutch_batch_wrapper.cmdline import cmdline; cmdline()'
# that can be followed by arguments.

def cmdline():
    "Command-line entrypoint"
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.description = """Wrapper for submitting/terminating AWS Batch jobs.

Type

{} <subcommand> --help

for help on each subcommand.""".format(parser.prog)
    subparsers = parser.add_subparsers(help='sub-command help')
    parser_submit = subparsers.add_parser('submit', help='submit a job')
    parser_submit.set_defaults(func=submit)
    parser_submit.add_argument('--cli-input-json', metavar='JSONFILE', type=str,
                               help="provide name of a JSON file containing arguments")
    parser_cancel = subparsers.add_parser('cancel', help='cancel a job')
    parser_cancel.set_defaults(func=cancel)
    parser_cancel.add_argument('--job-id', help='job ID')
    parser_cancel.add_argument('--reason', help='reason for canceling job')
    parser_terminate = subparsers.add_parser('terminate', help='terminate a job')
    parser_terminate.set_defaults(func=terminate)
    parser_terminate.add_argument('--job-id', help='job ID')
    parser_terminate.add_argument('--reason', help='reason for terminating job')

    args = parser.parse_args()
    args.func(args)

# TODO make exceptions tidier?
# TODO exit code > 0 on error

def clean(obj):
    "strip out response metadata and use pretty json formatting"
    del obj['ResponseMetadata']
    ret = json.dumps(obj, indent=4)
    return ret

def submit(args):
    "submit function"
    with open(args.cli_input_json) as jsonfile:
        obj = json.load(jsonfile)
    client = fredhutch_batch_wrapper.get_client()
    print(clean(client.submit_job(**obj)))


def cancel(args):
    "cancel function"
    client = fredhutch_batch_wrapper.get_client()
    print(clean(client.cancel_job(jobId=args.job_id, reason=args.reason)))

def terminate(args):
    "terminate function"
    client = fredhutch_batch_wrapper.get_client()
    print(clean(client.terminate_job(jobId=args.job_id, reason=args.reason)))
