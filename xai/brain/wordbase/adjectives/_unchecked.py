

#calss header
class _UNCHECKED():
	def __init__(self,): 
		self.name = "UNCHECKED"
		self.definitions = [u'If something harmful is unchecked, it is continuing or increasing without or despite any limits or attempts to prevent it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
