

#calss header
class _IMPATIENT():
	def __init__(self,): 
		self.name = "IMPATIENT"
		self.definitions = [u"easily annoyed by someone's mistakes or because you have to wait: ", u'wanting something to happen as soon as possible: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
