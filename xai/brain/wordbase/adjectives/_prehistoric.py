

#calss header
class _PREHISTORIC():
	def __init__(self,): 
		self.name = "PREHISTORIC"
		self.definitions = [u'describing the period before there were written records: ', u'very old-fashioned: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
