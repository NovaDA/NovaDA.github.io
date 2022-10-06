class SocialMediaData():

    def __init__(self, data):
        self.verifydata(data)

    def verifydata(self, data):
        if 'job_id' in data:
            self._job_id = data['job_id']
        if 'result_url' in data:
            self._result_url = data['result_url']
        if 'files' in data:
             self._files = data['files']

    @property
    def jobID(self):
        if hasattr(self, '_job_id'):
            return self._job_id

    @property
    def result_url(self):
        if hasattr(self, '_result_url'):
            return self._result_url

    @property
    def files(self):
        if hasattr(self, '_files'):
            return self._files
