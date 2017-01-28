

#calss header
class _THANKLESS():
	def __init__(self,): 
		self.name = "THANKLESS"
		self.definitions = [u'A thankless job is difficult or unpleasant, and people do not thank you for it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
