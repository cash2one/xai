

#calss header
class _QUITS():
	def __init__(self,): 
		self.name = "QUITS"
		self.definitions = [u'to not owe money to someone or to each other now: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
