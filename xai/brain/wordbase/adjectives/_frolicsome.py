

#calss header
class _FROLICSOME():
	def __init__(self,): 
		self.name = "FROLICSOME"
		self.definitions = [u'enthusiastic and liking to play']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
