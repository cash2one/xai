

#calss header
class _LIFELIKE():
	def __init__(self,): 
		self.name = "LIFELIKE"
		self.definitions = [u'used to describe something that appears real or very similar to what is real: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
