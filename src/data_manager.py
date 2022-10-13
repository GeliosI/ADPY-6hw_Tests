class DataManager:
    def __init__(self, documents=[], directories={}):
        self.documents = documents
        self.directories = directories

    def check_number_exist(self, doc_number):
        for doc in self.documents:
            if doc_number == doc['number']:
                return doc
        return False
        
    def check_dir_exist(self, dir_number):
        if dir_number in self.directories:
            return True
            
    def get_name_by_doc_number(self, doc_number):
        doc = self.check_number_exist(doc_number)
        if doc:
            return doc['name']
        return False
                
    def get_dir_number_by_doc_number(self, doc_number):
        if not self.check_number_exist(doc_number):
            return False
        for dir_number, self.documents in self.directories.items():
            if doc_number in self.documents:
                return dir_number

    def list_of_all_documents(self):
        for doc in self.documents:
            print(f'{doc["type"]} "{doc["number"]}" "{doc["name"]}"')

    def add_documents(self, doc_number, type_, name, dir_number):
        if not self.check_dir_exist(dir_number):
            return False
            
        if dir_number in self.directories:
            self.documents.append({'type': type_, 'number': doc_number, 'name': name})
            self.directories[dir_number].append(doc_number)
            return True
        
    def del_doc_by_number(self, doc_number):
        if not self.check_number_exist(doc_number):
            return False
            
        for doc in list(self.documents):
            if doc['number'] == doc_number:
                self.documents.remove(doc)
        
                for doc in self.directories.values():
                    if doc_number in doc:
                        doc.remove(doc_number)
                        return True

    def move_doc(self, doc_number, dir_number):
        if not self.check_number_exist(doc_number):
            return False
        if not self.check_dir_exist(dir_number):
            return False

        for dir_doc in self.directories.values():
            if doc_number in dir_doc:
                dir_doc.remove(doc_number)
                self.directories[dir_number].append(doc_number)
                return True

    def add_shelf(self, dir_number):
        if self.check_dir_exist(dir_number):
            return False
            
        self.directories[dir_number] = []
        return True