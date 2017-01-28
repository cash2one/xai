

#calss header
class _UNENVIABLE():
	def __init__(self,): 
		self.name = "UNENVIABLE"
		self.definitions = [u'An unenviable duty or necessary action is unpleasant or difficult: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
