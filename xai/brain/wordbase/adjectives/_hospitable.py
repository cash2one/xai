

#calss header
class _HOSPITABLE():
	def __init__(self,): 
		self.name = "HOSPITABLE"
		self.definitions = [u'friendly and welcoming to guests and visitors: ', u'providing good conditions for living or growing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
