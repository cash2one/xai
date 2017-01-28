

#calss header
class _COUNTABLE():
	def __init__(self,): 
		self.name = "COUNTABLE"
		self.definitions = [u'a countable noun can be used with "a" or "an" and can be made plural: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
