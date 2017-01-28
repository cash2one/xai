

#calss header
class _BOUFFANT():
	def __init__(self,): 
		self.name = "BOUFFANT"
		self.definitions = [u'A bouffant hairstyle has the hair arranged in a high rounded shape.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
