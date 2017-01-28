

#calss header
class _REPORTED():
	def __init__(self,): 
		self.name = "REPORTED"
		self.definitions = [u'described by people although there is no proof yet: ', u'formally mentioned to someone in authority, for example the police: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
