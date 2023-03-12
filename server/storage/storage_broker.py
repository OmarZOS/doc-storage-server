


class StorageBroker:
    
    # for concrete doc storage databases like scyllaDB
    def _get_document_provider():
        try:
            print("x")
        except:
            print('An exception occurred')
        
    def insert_document(self,attribs, vals):
        pass
    
    def get_document(doc_id):
        pass


    # for meta search engines like elasticsearch
    def _get_document_seeker():
        pass
    
    def insert_metadata(args):
        pass

    def search_for(search_tokens):
        pass