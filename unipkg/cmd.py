import unipkg
import argparse

def run():
    parser = argparse.ArgumentParser()
    parser.add_argument('--verbose', action='store_true', help='Increase output verbosity')
    parser.add_argument('--provider', type=str, default='yay', choices=unipkg.all_providers.keys(), help='Select the package management provider')

    subparsers = parser.add_subparsers(
        title=argparse.SUPPRESS,
        dest='command',
        description=None,
        required=True,
        metavar='command',
    )

    install_psr = subparsers.add_parser('install', help='install the specified packages',)
    install_psr.add_argument('package', nargs='+')

    remove_psr = subparsers.add_parser('remove', help='uninstall the specified packages')
    remove_psr.add_argument('package', nargs='+')

    search_psr = subparsers.add_parser('search', help='query the package database')
    search_psr.add_argument('query', help='search string')  

    info_psr = subparsers.add_parser('info', help='view the package metadata')
    info_psr.add_argument('package', help='package of interest')

    subparsers.add_parser('stats', help='show installation stats')
    subparsers.add_parser('clean', help='clean the package database')
    subparsers.add_parser('update', help='update the local package database')
    subparsers.add_parser('upgrade', help='perform an upgrade of installed packages')
    subparsers.add_parser('list-installed', help='show installed packages')
    subparsers.add_parser('list-providers', help='show available providers')

    provider = unipkg.YayProvider()

    args = parser.parse_args()
    if args.command == 'install':
        provider.install(*args.package)
    elif args.command == 'remove':
        provider.remove(*args.package)
    elif args.command == 'upgrade':
        provider.upgrade()
    elif args.command == 'search':
        provider.search(args.query)
    elif args.command == 'info':
        provider.info(args.package)
    elif args.command == 'stats':
        provider.stats()
    elif args.command == 'clean':
        provider.clean()
    elif args.command == 'update':
        provider.update()
    elif args.command == 'list-installed':
        provider.list_installed()
    elif args.command == 'list-providers':
        for provider in unipkg.all_providers.keys():
            print(provider)