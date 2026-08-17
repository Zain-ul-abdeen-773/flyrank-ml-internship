import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import json
import time

def print_agent_step(step_name, delay=1.5):
    """Simulates agent processing time for the terminal output."""
    print(f"\n[Agent] {step_name}...")
    time.sleep(delay)

def fetch_arxiv_papers(query="all:\"machine learning pipeline\" OR all:\"MLOps\"", max_results=2):
    """Tool: Fetches recent papers from the live arXiv API."""
    print_agent_step(f"Accessing arXiv API with query: {query}")
    
    url = f"http://export.arxiv.org/api/query?search_query={urllib.parse.quote(query)}&sortBy=submittedDate&sortOrder=descending&max_results={max_results}"
    
    try:
        response = urllib.request.urlopen(url)
        xml_data = response.read().decode('utf-8')
        root = ET.fromstring(xml_data)
        
        papers = []
        # Parse the XML response from arXiv
        for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
            title = entry.find('{http://www.w3.org/2005/Atom}title').text.replace('\n', ' ').strip()
            summary = entry.find('{http://www.w3.org/2005/Atom}summary').text.replace('\n', ' ').strip()
            papers.append({"title": title, "summary": summary[:200] + "..."})
            
        print(f"        -> Retrieved {len(papers)} papers.")
        return papers
    except Exception as e:
        print(f"        -> Error fetching from arXiv: {e}")
        return []

def search_github_repo(keywords):
    """Tool: Searches the live GitHub API for code repositories."""
    import re
    # Strip punctuation (like colons, hyphens) which break GitHub search syntax
    sanitized = re.sub(r'[^a-zA-Z0-9 ]', ' ', keywords[:50])
    clean_query = urllib.parse.quote(sanitized) 
    print_agent_step(f"Executing GitHub API search for code related to: '{keywords[:50]}...'")
    
    url = f"https://api.github.com/search/repositories?q={clean_query}&sort=stars&order=desc"
    
    # GitHub requires a User-Agent header for unauthenticated requests
    req = urllib.request.Request(url, headers={'User-Agent': 'AI-Research-Scout-Agent'})
    
    try:
        response = urllib.request.urlopen(req)
        data = json.loads(response.read().decode('utf-8'))
        
        if data.get('items') and len(data['items']) > 0:
            top_repo = data['items'][0]
            repo_url = top_repo.get('html_url')
            stars = top_repo.get('stargazers_count')
            print(f"        -> Found repository: {repo_url} (⭐ {stars})")
            return repo_url, stars
        else:
            print("        -> No open-source implementations found on GitHub.")
            return None, 0
    except Exception as e:
        print(f"        -> GitHub API Rate Limit / Error: {e}")
        return None, 0

def run_agent_loop():
    print("==================================================")
    print("🤖 INITIALIZING AI RESEARCH SCOUT (SCRIPTED AGENT)")
    print("==================================================")
    
    # Step 1: Query arXiv
    papers = fetch_arxiv_papers(query="all:\"FastAPI\" OR all:\"PyTorch\" OR all:\"Docker\"", max_results=2)
    
    # Step 2: Loop through papers and query GitHub
    briefing = []
    for idx, paper in enumerate(papers):
        print_agent_step(f"Analyzing Paper {idx+1}: {paper['title']}")
        
        # Extract a few key words from the title to search GitHub
        search_terms = " ".join(paper['title'].split()[:4])
        repo_url, stars = search_github_repo(search_terms)
        
        briefing.append({
            "title": paper['title'],
            "summary": paper['summary'],
            "repo": repo_url,
            "stars": stars
        })
        
        time.sleep(2) # Prevent rapid API calls
        
    # Step 3: Output the Final Briefing
    print_agent_step("Synthesizing Daily Morning Briefing", delay=2.0)
    
    print("\n\n📋 ================= MORNING BRIEFING ================= 📋")
    for i, item in enumerate(briefing):
        print(f"\n[{i+1}] {item['title']}")
        print(f"Abstract Snippet: {item['summary']}")
        if item['repo']:
            print(f"Code Found: {item['repo']} (⭐ {item['stars']} stars)")
        else:
            print("Code Found: Not available or closed-source.")
    print("\n========================================================\n")
    print("✅ Agent run completed successfully.")

if __name__ == "__main__":
    run_agent_loop()