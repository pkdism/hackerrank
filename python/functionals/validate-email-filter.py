def fun(s):
    if '@' not in s:
        return False
    if '.' not in s:
        return False

    username = s.split('@')[0]
    website = s.split('@')[1].split('.')[0]
    extension = s.split('.')[1]

    if len(username) == 0 or len(website) == 0 or len(extension) == 0:
        return False

    valid_username = all([i.isalnum() or i == '_' or i == '-' for i in username])
    valid_website = all([i.isalnum() for i in website])
    valid_extension = len(extension) <= 3

    return valid_username and valid_website and valid_extension and username + '@' + website + '.' + extension == s

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
