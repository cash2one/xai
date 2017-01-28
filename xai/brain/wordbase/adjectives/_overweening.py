

#calss header
class _OVERWEENING():
	def __init__(self,): 
		self.name = "OVERWEENING"
		self.definitions = [u'being too proud or confident in yourself: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
