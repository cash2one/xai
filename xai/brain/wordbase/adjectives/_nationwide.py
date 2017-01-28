

#calss header
class _NATIONWIDE():
	def __init__(self,): 
		self.name = "NATIONWIDE"
		self.definitions = [u'existing or happening in all parts of a particular country: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
