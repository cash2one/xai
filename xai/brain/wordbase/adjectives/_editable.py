

#calss header
class _EDITABLE():
	def __init__(self,): 
		self.name = "EDITABLE"
		self.definitions = [u'an editable text, document, etc. can be changed : ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
