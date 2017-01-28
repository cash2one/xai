

#calss header
class _PALATAL():
	def __init__(self,): 
		self.name = "PALATAL"
		self.definitions = [u'(of a consonant) made by the tongue touching the highest part of the mouth']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
