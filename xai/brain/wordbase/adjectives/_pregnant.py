

#calss header
class _PREGNANT():
	def __init__(self,): 
		self.name = "PREGNANT"
		self.definitions = [u'(of a woman and some female animals) having a baby or babies developing inside the womb: ', u'filled with meaning or importance that has not yet been expressed or understood: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
