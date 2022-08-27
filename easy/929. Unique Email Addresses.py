def num_unique_emails(emails):

    unique = set()

    for email in emails:
        name, domain = email.split('@')

        name = name.split('+')[0]
        name = name.replace('.', '')

        unique.add(f'{name}@{domain}')

    return len(unique)
