

#calss header
class _UNMANNED():
	def __init__(self,): 
		self.name = "UNMANNED"
		self.definitions = [u'used to refer to a spacecraft, or a place where military guards work, that has no people present to operate or be in charge of it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
