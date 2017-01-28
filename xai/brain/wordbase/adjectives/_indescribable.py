

#calss header
class _INDESCRIBABLE():
	def __init__(self,): 
		self.name = "INDESCRIBABLE"
		self.definitions = [u'impossible to describe, especially because of being extremely good or bad: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
