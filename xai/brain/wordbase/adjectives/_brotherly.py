

#calss header
class _BROTHERLY():
	def __init__(self,): 
		self.name = "BROTHERLY"
		self.definitions = [u'showing the kindness, interest, or love that you would expect a brother to show: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
