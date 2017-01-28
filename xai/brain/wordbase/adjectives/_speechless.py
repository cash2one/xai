

#calss header
class _SPEECHLESS():
	def __init__(self,): 
		self.name = "SPEECHLESS"
		self.definitions = [u'unable to speak because you are so angry, shocked, surprised, etc.: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
