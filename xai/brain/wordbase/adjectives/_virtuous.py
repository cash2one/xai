

#calss header
class _VIRTUOUS():
	def __init__(self,): 
		self.name = "VIRTUOUS"
		self.definitions = [u'having good moral qualities and behaviour: ', u'A virtuous person thinks himself or herself morally better than other people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
