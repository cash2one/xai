

#calss header
class _WITHERING():
	def __init__(self,): 
		self.name = "WITHERING"
		self.definitions = [u'A withering look, remark, etc. is one that is intended to make someone feel ashamed: ', u'severe and extremely critical: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
