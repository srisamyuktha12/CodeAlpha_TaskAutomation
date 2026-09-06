import re


def extract_emails(input_file, output_file):
    """Extract email addresses from a text file."""

    try:
        with open(input_file, "r", encoding="utf-8") as file:
            text = file.read()

        # Regular expression for finding email addresses
        email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

        emails = re.findall(email_pattern, text)

        # Remove duplicates and sort the emails
        unique_emails = sorted(set(emails))

        with open(output_file, "w", encoding="utf-8") as file:
            for email in unique_emails:
                file.write(email + "\n")

        print("=" * 50)
        print("       EMAIL EXTRACTION COMPLETE")
        print("=" * 50)

        print(f"\nEmails found: {len(unique_emails)}")

        if unique_emails:
            print("\nExtracted email addresses:")

            for email in unique_emails:
                print(f"- {email}")

            print(f"\nSaved to: {output_file}")

        else:
            print("\nNo email addresses were found.")

    except FileNotFoundError:
        print(f"Error: '{input_file}' was not found.")

    except PermissionError:
        print("Error: Permission denied while accessing the file.")

    except Exception as error:
        print(f"An unexpected error occurred: {error}")


def main():
    input_file = "input.txt"
    output_file = "extracted_emails.txt"

    print("=" * 50)
    print("       📧 EMAIL EXTRACTOR")
    print("=" * 50)

    extract_emails(input_file, output_file)


if __name__ == "__main__":
    main()