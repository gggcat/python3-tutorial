import pkg_resources

def main():
    print(pkg_resources.resource_filename('packagedata', 'config'))
    print(pkg_resources.resource_string('packagedata', 'config/test.ini').decode())

if __name__ == '__main__':
    main()