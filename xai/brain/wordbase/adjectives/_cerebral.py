

#calss header
class _CEREBRAL():
	def __init__(self,): 
		self.name = "CEREBRAL"
		self.definitions = [u'relating to the brain or the cerebrum', u'demanding or involving careful thinking and mental effort rather than feelings: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
