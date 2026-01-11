from send_email import send_email
import sys


def main():
    # Read error message safely
    if len(sys.argv) > 1:
        error_message = sys.argv[1]
    else:
        error_message = "Unknown pipeline error"

    send_email(
        subject="Exchange Rate Pipeline Failed",
        body=f"The GitHub Actions pipeline failed.\n\nError:\n{error_message}"
    )


if __name__ == "__main__":
    main()

