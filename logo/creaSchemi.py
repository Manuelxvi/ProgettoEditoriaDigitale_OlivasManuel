import yaml
import json
def load_yaml(yaml_file):
    """Carica il file YAML."""
    with open(yaml_file, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)
yaml_file = r"Metadati.YAML"
data = load_yaml(yaml_file)

def convert_to_onix(data):  #converte in onix
    """Converte i metadati YAML nel formato ONIX."""
    onix = []
    for item in data["distribuzione"]["onix"]:
        onix.append({
            "Product": {
                "Title": item["title"],
                "Contributor": {
                    "PrimaryAuthor": item["contributor"]["primary_author"],
                    "OtherAuthors": item["contributor"]["other_authors"],
                },
                "Publisher": item["publisher"],
                "PublicationDate": item["publication_date"],
                "Audience": item["audience"],
                "Format": item["format"],
                "Price": item["price"],
            }
        })
    return onix

def convert_to_schema_org(data): #la conversione su schema.org
    """Converte i metadati YAML nel formato Schema.org."""
    schema_org = []
    for key, value in data["schema_org"].items():
        schema_org.append(value)
    return schema_org

def save_to_file(data, file_path, format="json"):  #funzione per salvataggio finale
    """Salva i dati in un file (ONIX o Schema.org)."""
    with open(file_path, "w", encoding="utf-8") as file:
        if format == "json":
            json.dump(data, file, indent=4, ensure_ascii=False)
        else:
            file.write(str(data))  # Default string format
    print(f"Salvato in: {file_path}")

# Trasformazione ONIX
onix_data = convert_to_onix(data)
save_to_file(onix_data, "relazione_onix.json", format="json")

# Trasformazione Schema.org
schema_org_data = convert_to_schema_org(data)
save_to_file(schema_org_data, "relazione_schema_org.json", format="json")
