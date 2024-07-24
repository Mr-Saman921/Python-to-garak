def check_url(link):
    if link.startswith("http://") or link.startswith("https://"):
        try:
            print(f"URL {link} mavjud")
        except link.exceptions.RequestException as error:
            print(f"URL {link} mavjud emas. Xatolik: {e}")
if __name__ == "__main__":
    link = "http://uzum.uz"
    check_url(link)
