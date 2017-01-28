

#calss header
class _INBUILT():
	def __init__(self,): 
		self.name = "INBUILT"
		self.definitions = [u'If something is inbuilt, it is an original part of something or someone and cannot be separated from it, him, or her: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
