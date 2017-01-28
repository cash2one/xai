

#calss header
class _BENUMBED():
	def __init__(self,): 
		self.name = "BENUMBED"
		self.definitions = [u'unable to feel because of cold, shock, etc.: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
