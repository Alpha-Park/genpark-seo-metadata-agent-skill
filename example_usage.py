from client import SEOMetadataGeneratorClient
def main():
    c = SEOMetadataGeneratorClient()
    print(c.generate_metadata("Zenith Speaker", "High quality noise cancelling speaker with deep bass", ["speaker", "audio"]))
if __name__ == '__main__':
    main()
