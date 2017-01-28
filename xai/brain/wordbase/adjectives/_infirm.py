

#calss header
class _INFIRM():
	def __init__(self,): 
		self.name = "INFIRM"
		self.definitions = [u'ill or needing care, especially for long periods and often because of old age: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
