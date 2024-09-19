import unipkg
import argparse
import inspect

def list_providers():
    for provider in unipkg.all_providers.keys():
        print(provider)

def members_to_subparsers(subparsers, obj):
    mem = {}
    for member_name, member_value in inspect.getmembers(obj):
        if member_name.startswith('_'):
            continue
        mem[member_name] = []
        p = subparsers.add_parser(member_name.replace('_', '-'), help=member_value.__doc__)
        for param in inspect.signature(member_value).parameters.values():
            mem[member_name].append(param)
            if param.kind == inspect.Parameter.POSITIONAL_OR_KEYWORD and param.default != inspect.Parameter.empty:
                opts = {
                    "default": param.default,
                }
                
                if param.annotation == bool:
                    opts['action'] = 'store_true'
                elif param.annotation:
                    opts['type'] = param.annotation
                p.add_argument(f'--{param.name}', **opts)
            else:
                p.add_argument(param.name, type=param.annotation)
    return mem

def run():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--provider', '-p', type=str, default='yay', choices=['auto', *unipkg.all_providers.keys()], help='Select the package management provider')

    args, remaining_args = parser.parse_known_args()
    provider = unipkg.all_providers[args.provider]()
    
    subparsers = parser.add_subparsers(
        title=argparse.SUPPRESS,
        dest='command',
        description=None,
        required=True,
        metavar='command',
    )
    
    mem = members_to_subparsers(subparsers, provider)
    
    subparsers.add_parser('help', help='show help')
    subparsers.add_parser('list-providers', help='list the available package manager providers')
    
    args = parser.parse_args(remaining_args)
    
    command = args.command.replace('-', '_')
    method = getattr(provider, command, None)
    
    if method is None or args.command == 'help':
        parser.print_help()
        raise SystemExit
    elif args.command == 'list-providers':
        list_providers()
        raise SystemExit
    else:
        method(**dict([(arg.name, getattr(args, arg.name)) for arg in mem[command]]))
        