

#calss header
class _MELTING():
	def __init__(self,): 
		self.name = "MELTING"
		self.definitions = [u'A melting look or voice makes you feel sympathy or love.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
