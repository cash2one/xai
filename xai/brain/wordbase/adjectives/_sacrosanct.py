

#calss header
class _SACROSANCT():
	def __init__(self,): 
		self.name = "SACROSANCT"
		self.definitions = [u'thought to be too important or too special to be changed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
