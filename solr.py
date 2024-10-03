import pysolr
import json
solr_url = 'http://localhost:8983/solr/employee_data'
solr = pysolr.Solr(solr_url, always_commit=True)

def create_collection(collection_name):
    print(f"Collection {collection_name} already created.")

def index_data(data):
    # Index data into Solr
    solr.add(data)
    print("Data indexed successfully.")

def search_all():
    # Search all documents
    results = solr.search('*:*')
    return results

def main():
    # Step 1: Create collection (optional)
    collection_name = 'employee_data'
    create_collection(collection_name)

    # Step 2: Index employee data
    employee_data = [
        {"id": "1", "name": "John Doe", "department": "IT"},
        {"id": "2", "name": "Jane Doe", "department": "HR"},
    ]
    
    index_data(employee_data)

    # Step 3: Search all indexed documents
    print("Searching all documents:")
    results = search_all()
    
    for result in results:
        print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
