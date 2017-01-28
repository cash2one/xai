

#calss header
class _RAGGED():
	def __init__(self,): 
		self.name = "RAGGED"
		self.definitions = [u'(of clothes) torn and not in good condition: ', u'(of a person) untidy, dirty, and wearing old, torn clothes: ', u'(especially of an edge) rough and not smooth: ', u'not performing well, because of not being organized: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
