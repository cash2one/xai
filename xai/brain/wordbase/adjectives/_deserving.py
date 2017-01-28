

#calss header
class _DESERVING():
	def __init__(self,): 
		self.name = "DESERVING"
		self.definitions = [u'If people or things are deserving, they should be helped because they have good qualities: ', u'to deserve to get something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
