

#calss header
class _ANCIENT():
	def __init__(self,): 
		self.name = "ANCIENT"
		self.definitions = [u'of or from a long time ago, having lasted for a very long time: ', u'very old: ', u'used to refer to the period in European history from the earliest known societies to the end of the Roman Empire: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
