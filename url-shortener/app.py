import pyshorteners
import pyshorteners.exceptions
import requests
def create_short_url():
    long_url = input("Input your long URL: ")
    if not long_url.startswith(("http://","https://")):
        print("Invalid URL! The URL requires http:// or http://.")
        return

    try:
        type_tiny = pyshorteners.Shortener()

        short_url = type_tiny.tinyurl.short(long_url)

        print("Short Url is: " + short_url)
    except requests.exceptions.RequestException as e:
        print("Network error! Please check your internet connection.")
    except pyshorteners.exceptions.ShorteningErrorException as e:
        print("Error shortening URL", e)
    except Exception as e:
        print("An unexpected error occured.", e)
def exit_app():
    print("Thank you for using the URL shortener!")

def main():
    while True:
        try:
            option_menu = int(input("If you want to create a short URL enter [1].\nIf you want to exit press [2].\nEnter option: "))
        except ValueError as e:
            print("The program ran into and error:", e )
        if option_menu == 1:
            create_short_url()
        elif option_menu == 2:
            exit_app()
            break
        else:
            print("Invalid option")
if __name__ == "__main__":
    main()
