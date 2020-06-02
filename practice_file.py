class File(object):
    def __init__(self,file_name, file_extention, content, lock, parent_folder):
        self.file_name = file_name
        self.file_extension = file_extention  #ex)org
        self.content = content
        self.lock = lock
        self.parent_folder = parent_folder

class Operation(object):
    def __init__(self):
        pass

    def get_file_time_band_width_size(self,text_size):
        file_size = text_size * 10
        if file_size >= 1000:
            return str(file_size/1000) + 'GB'
        else:
            return str(file_size) + 'MB'

    def get_file_type(self,file_object):
        if file_object.file_extension == '.pdf' or '.word' or '.txt':
            return 'document'
        elif file_object.file_extension == '.js' or '.css' or 'html':
            return 'source-dode'
        elif file_object.file_extension == '.mp4':
            return 'video'
        elif file_object.file_extension == '.mp3':
            return 'music'

    def prepend_content(self,new_content,file_object):
        if file_object.lock == True:
            return new_content + file_object.content
        else:
            return 'Error'
    def append_content(self,new_content,file_object):
        if file_object.lock == True:
            return file_object.content + new_content
        else:
            return 'Error'

    def add_content(self,index,add_sentence,file_object):
        if file_object.lock == True:
            return file_object.content[:index] + add_sentence + file_object.content[index:]
        else:
            return 'Error'

file1 = File('abcde','text','introducing of this story',True,'practice')
operation = Operation()
print(operation.add_content(30,'hello',file1))