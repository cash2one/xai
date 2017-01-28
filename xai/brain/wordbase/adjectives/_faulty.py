

#calss header
class _FAULTY():
	def __init__(self,): 
		self.name = "FAULTY"
		self.definitions = [u'A faulty machine or device is not perfectly made or does not work correctly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
