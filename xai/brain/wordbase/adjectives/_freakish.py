

#calss header
class _FREAKISH():
	def __init__(self,): 
		self.name = "FREAKISH"
		self.definitions = [u'very unusual or unexpected, especially in an unpleasant or strange way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
