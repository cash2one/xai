

#calss header
class _IMPENDING():
	def __init__(self,): 
		self.name = "IMPENDING"
		self.definitions = [u'used to refer to an event, usually something unpleasant or unwanted, that is going to happen soon: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
