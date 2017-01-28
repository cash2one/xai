

#calss header
class _SUNKEN():
	def __init__(self,): 
		self.name = "SUNKEN"
		self.definitions = [u'having fallen to the bottom of the sea: ', u'at a lower level than the surrounding area: ', u'(of eyes or cheeks) seeming to have fallen further into the face, especially because of tiredness, illness, or old age: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
