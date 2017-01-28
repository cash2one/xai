

#calss header
class _NORTHWESTERLY():
	def __init__(self,): 
		self.name = "NORTHWESTERLY"
		self.definitions = [u'towards the northwest: ', u'a wind that comes from the northwest']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
