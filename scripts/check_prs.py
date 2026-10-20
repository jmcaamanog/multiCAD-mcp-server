import urllib.request
import json

url = 'https://api.github.com/repos/AnCode666/multiCAD-mcp/pulls?state=open&per_page=50'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))

    my_prs = [p for p in data if p['user']['login'] == 'jmcaamanog']
    print(f"Total Open PRs by jmcaamanog: {len(my_prs)}")
    # sort by number ascending
    my_prs.sort(key=lambda x: x['number'])
    for p in my_prs:
        num = p['number']
        title = p['title']
        branch = p['head']['ref']
        pr_url = p['html_url']
        has_body = "YES" if p.get('body') else "EMPTY"
        print(f"PR #{num:02d} | Branch: {branch} | Body: {has_body} | URL: {pr_url}")
        print(f"       Title: {title}")
except Exception as e:
    print(f"Error: {e}")
