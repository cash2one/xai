

#calss header
class _HACKNEYED():
	def __init__(self,): 
		self.name = "HACKNEYED"
		self.definitions = [u'A hackneyed phrase or idea has been said or used so often that it has become boring and has no meaning: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
