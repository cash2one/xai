

#calss header
class _UNIDENTIFIED():
	def __init__(self,): 
		self.name = "UNIDENTIFIED"
		self.definitions = [u'whose name is not known or is being kept secret: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
