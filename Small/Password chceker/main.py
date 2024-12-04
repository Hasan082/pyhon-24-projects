def check_password(password: str):
    with open('common_password.txt', 'r') as f:
        common_password = f.read().splitlines()

        for i, file_password in enumerate(common_password, start=1):
            if password == file_password:
                print(f"Your password {password} is too common : ❌ (#{i})")
                return
        print(f"Your password {password} : ✅ (Unique)")


def main():
    check_password(input('Enter your password: '))


if __name__ == '__main__':
    main()

