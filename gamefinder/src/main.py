from utils.scraper import Scraper

def main():
    query = "Games"
    
    print("Fetching results...")
    scraper = Scraper(query)
    scraper.fetch_results(num_pages=3)  # Fetch results from multiple pages
    
    print("Parsing results...")
    ai_links = scraper.results
    
    print(f"Number of AI-related websites found: {len(ai_links)}")
    for link in ai_links:
        print(link)
    
    # Save the links to a text file
    with open("ai_links.txt", "w") as file:
        for link in ai_links:
            file.write(link + "\n")

if __name__ == "__main__":
    main()