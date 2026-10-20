from pymango.mango_client import MangoClient 

url = "mongodb+srv://krishaitechnologies:<@password>@cluster0.wnqb6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(url) 

try: 
    client.admin.command("ping") 
    print("Pinged your deployment. You successfully connnected to MongoDB") 

except Exception as e: 
    print(e) 