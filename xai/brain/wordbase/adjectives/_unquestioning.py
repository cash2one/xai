

#calss header
class _UNQUESTIONING():
	def __init__(self,): 
		self.name = "UNQUESTIONING"
		self.definitions = [u'Unquestioning obedience is total, and given without thinking, asking questions, or doubting: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
