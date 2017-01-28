

#calss header
class _SOUTHWESTERLY():
	def __init__(self,): 
		self.name = "SOUTHWESTERLY"
		self.definitions = [u'towards the southwest: ', u'a wind that comes from the southwest']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
