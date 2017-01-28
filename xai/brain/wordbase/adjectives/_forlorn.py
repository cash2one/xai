

#calss header
class _FORLORN():
	def __init__(self,): 
		self.name = "FORLORN"
		self.definitions = [u'alone and unhappy; left alone and not cared for: ', u'A forlorn place feels empty and sad: ', u'very unlikely to be achieved or to succeed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
