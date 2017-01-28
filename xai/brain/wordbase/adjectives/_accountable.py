

#calss header
class _ACCOUNTABLE():
	def __init__(self,): 
		self.name = "ACCOUNTABLE"
		self.definitions = [u'Someone who is accountable is completely responsible for what they do and must be able to give a satisfactory reason for it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
